"""Build a pinned Dalamud catalogue from released binaries; never load plugin code."""
import argparse
import hashlib
import io
import json
import re
import struct
import subprocess
import urllib.request
import zipfile
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "sources.json"
MAX_BYTES = 32 * 1024 * 1024
ALLOWED_REPOS = {"hotbar-atelier", "codex-monitor", "minimap-zoom"}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))

def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def fetch(url):
    if not url.startswith("https://"):
        raise ValueError("Only HTTPS downloads are allowed")
    request = urllib.request.Request(url, headers={"User-Agent": "Aleqsd-Dalamud-Catalogue", "Cache-Control": "no-cache"})
    with urllib.request.urlopen(request, timeout=60) as response:
        data = response.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise ValueError("Download exceeds limit")
    return data

def github(route):
    result = subprocess.run(["gh", "api", route], check=True, capture_output=True, text=True, encoding="utf-8")
    return json.loads(result.stdout)

def version(text):
    if not isinstance(text, str) or not re.fullmatch(r"\d+\.\d+\.\d+(?:\.\d+)?", text):
        raise ValueError(f"Invalid version: {text}")
    return tuple((list(map(int, text.split("."))) + [0])[:4])

def png(data):
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("Invalid PNG")
    width, height = struct.unpack(">II", data[16:24])
    if width != height or width < 64 or width > 512:
        raise ValueError("Icon must be square, 64 to 512 px")

def validate_install_zip(data, entry, expected_dll_hash):
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)):
            raise ValueError("Duplicate archive entries")
        if any("/" in n or "\\" in n or n in {".", ".."} for n in names):
            raise ValueError("Installer archive files must be at the root")
        internal = entry["InternalName"]
        local = json.loads(archive.read(internal + ".json"))
        if local["InternalName"] != internal or version(local["AssemblyVersion"]) != version(entry["AssemblyVersion"]):
            raise ValueError("Manifest identity/version mismatch")
        if local.get("WorkingPluginId") or local.get("InstalledFromUrl") or local.get("Testing"):
            raise ValueError("Local installation state cannot be distributed")
        if local["DalamudApiLevel"] != entry["DalamudApiLevel"]:
            raise ValueError("Manifest API mismatch")
        if digest(archive.read(internal + ".dll")) != expected_dll_hash:
            raise ValueError("DLL differs from the original release")
        if not archive.read("LICENSE").strip():
            raise ValueError("Missing license")
        png(archive.read("icon.png"))

def make_zip(files):
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in sorted(files):
            info = zipfile.ZipInfo(name, (2020, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, files[name])
    return output.getvalue()

def build(config):
    if config["repository"] != "Aleqsd/dalamud-plugins":
        raise ValueError("Unexpected catalogue owner/repository")
    release_tag = config["packageRelease"]
    if not re.fullmatch(r"[A-Za-z0-9._-]+", release_tag):
        raise ValueError("Invalid package release tag")
    output = ROOT / ".artifacts" / release_tag
    output.mkdir(parents=True, exist_ok=True)
    cache = ROOT / ".artifacts" / "cache"
    cache.mkdir(parents=True, exist_ok=True)
    entries, records = [], []
    for item in config["plugins"]:
        repo, internal, tag = item["repo"], item["id"], item["tag"]
        if repo not in ALLOWED_REPOS or not re.fullmatch(r"[A-Za-z0-9]+", internal):
            raise ValueError("Unexpected plugin")
        metadata = github(f"repos/Aleqsd/{repo}/releases/tags/{tag}")
        commit = github(f"repos/Aleqsd/{repo}/commits/{tag}")["sha"]
        if metadata["draft"] or commit != item["commit"]:
            raise ValueError(f"Unpublished or moved source tag: {repo}")
        original_asset = next(a for a in metadata["assets"] if a["name"] == item["archive"])
        dll_asset = next(a for a in metadata["assets"] if a["name"] == internal + ".dll")
        if original_asset.get("digest") != "sha256:" + item["archiveSha256"] or dll_asset.get("digest") != "sha256:" + item["dllSha256"]:
            raise ValueError(f"Source release digest changed: {repo}")
        cached = cache / item["archiveSha256"]
        data = cached.read_bytes() if cached.exists() else fetch(original_asset["browser_download_url"])
        if digest(data) != item["archiveSha256"]:
            raise ValueError(f"Wrong downloaded source archive: {repo}")
        cached.write_bytes(data)
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            if len(archive.namelist()) != len(set(archive.namelist())):
                raise ValueError("Duplicate source entries")
            files = {name: archive.read(item["prefix"] + name) for name in item["files"]}
            files["LICENSE"] = archive.read("LICENSE")
        local = json.loads(files[internal + ".json"])
        if local["InternalName"] != internal or version(local["AssemblyVersion"]) != version(tag.removeprefix("v")):
            raise ValueError(f"Tag/manifest mismatch: {repo}")
        if local.get("WorkingPluginId") or local.get("InstalledFromUrl") or local.get("Testing"):
            raise ValueError("Source manifest contains local installation state")
        if digest(files[internal + ".dll"]) != item["dllSha256"]:
            raise ValueError("Archive DLL differs from individually released DLL")
        icon = ROOT / item["icon"]
        icon_data = icon.read_bytes()
        png(icon_data)
        repo_url = f"https://github.com/Aleqsd/{repo}"
        icon_url = f"https://raw.githubusercontent.com/{config['repository']}/main/{item['icon']}"
        local["RepoUrl"] = repo_url
        local["IconUrl"] = icon_url
        files[internal + ".json"] = (json.dumps(local, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        files["icon.png"] = icon_data
        files["CATALOGUE-LICENSE.txt"] = (ROOT / "LICENSE").read_bytes()
        files["SOURCE.txt"] = (f"Source and build instructions: {repo_url}/tree/{commit}\n"
                               f"Original release: {metadata['html_url']}\n"
                               f"Original archive SHA256: {item['archiveSha256']}\n"
                               f"Unmodified DLL SHA256: {item['dllSha256']}\n"
                               "This installation archive keeps the original DLL and license.\n"
                               "Only package layout and public icon/repository metadata are adapted.\n").encode("utf-8")
        name = f"{internal}-{tag.removeprefix('v')}-dalamud.zip"
        download = f"https://github.com/{config['repository']}/releases/download/{release_tag}/{name}"
        entry = dict(local)
        entry.update({
            "Description": local["Description"] + " Version expérimentale ; essais en jeu encore à confirmer.",
            "RepoUrl": repo_url,
            "IconUrl": icon_url,
            "ImageUrls": [f"https://raw.githubusercontent.com/Aleqsd/{repo}/{commit}/{item['image']}"],
            "LastUpdate": int(datetime.fromisoformat(metadata["published_at"].replace("Z", "+00:00")).timestamp()),
            "IsHide": False, "IsTestingExclusive": False,
            "TestingAssemblyVersion": local["AssemblyVersion"],
            "TestingDalamudApiLevel": local["DalamudApiLevel"],
            "DownloadLinkInstall": download, "DownloadLinkUpdate": download, "DownloadLinkTesting": download,
            "Changelog": item["changelog"]
        })
        if item.get("installationNote"):
            entry["Description"] += " " + item["installationNote"]
        package = make_zip(files)
        validate_install_zip(package, entry, item["dllSha256"])
        (output / name).write_bytes(package)
        entries.append(entry)
        records.append({
            "InternalName": internal, "AssemblyVersion": local["AssemblyVersion"],
            "DalamudApiLevel": local["DalamudApiLevel"],
            "SourceCommit": commit, "SourceRelease": metadata["html_url"],
            "SourceArchiveSha256": item["archiveSha256"], "DllSha256": item["dllSha256"],
            "Package": name, "PackageSha256": digest(package),
            "Icon": item["icon"], "IconSha256": digest(icon_data), "ImageUrl": entry["ImageUrls"][0]
        })
        print(f"{internal} {local['AssemblyVersion']}: flat ZIP, manifest, unchanged DLL and icon validated")
    if len({e["InternalName"] for e in entries}) != len(entries):
        raise ValueError("Duplicate plugin IDs")
    if (ROOT / "repo.json").exists():
        old = {e["InternalName"]: e for e in read_json(ROOT / "repo.json")}
        for current in entries:
            previous = old.get(current["InternalName"])
            if previous and version(current["AssemblyVersion"]) < version(previous["AssemblyVersion"]):
                raise ValueError("Version rollback is not an update")
    if (ROOT / "catalogue.lock.json").exists():
        old_records = {r["InternalName"]: r for r in read_json(ROOT / "catalogue.lock.json")["plugins"]}
        for current in records:
            previous = old_records.get(current["InternalName"])
            if previous and version(current["AssemblyVersion"]) == version(previous["AssemblyVersion"]) and current["DllSha256"] != previous["DllSha256"]:
                raise ValueError("A changed DLL requires a higher assembly version")
    write_json(output / "repo.json", entries)
    write_json(output / "catalogue.lock.json", {"packageRelease": release_tag, "plugins": records})
    (output / "SHA256SUMS.txt").write_text("".join(f"{r['PackageSha256']}  {r['Package']}\n" for r in records), encoding="utf-8")
    print(f"Candidate ready: .artifacts/{release_tag}/repo.json")
    return output

def verify_public(config, check_index=False):
    output = ROOT / ".artifacts" / config["packageRelease"]
    entries = read_json(output / "repo.json")
    lock = read_json(output / "catalogue.lock.json")
    for entry, record in zip(entries, lock["plugins"], strict=True):
        package = fetch(entry["DownloadLinkInstall"])
        if digest(package) != record["PackageSha256"]:
            raise ValueError("Public package hash mismatch")
        validate_install_zip(package, entry, record["DllSha256"])
        icon_data = fetch(entry["IconUrl"])
        png(icon_data)
        if digest(icon_data) != record["IconSha256"]:
            raise ValueError("Public icon hash mismatch")
        preview = fetch(record["ImageUrl"])
        if preview[:8] != b"\x89PNG\r\n\x1a\n":
            raise ValueError("Public preview is not a PNG")
        print(f"{entry['InternalName']}: public ZIP, DLL, icon and preview verified")
    if check_index:
        raw = f"https://raw.githubusercontent.com/{config['repository']}/main/repo.json"
        if json.loads(fetch(raw)) != entries:
            raise ValueError("Published index differs from the validated candidate")
        print("Public repo.json matches the validated candidate exactly")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify-public", action="store_true")
    parser.add_argument("--verify-index", action="store_true")
    args = parser.parse_args()
    config = read_json(CONFIG)
    if args.verify_public or args.verify_index:
        verify_public(config, args.verify_index)
    else:
        build(config)
