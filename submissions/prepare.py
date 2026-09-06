"""Assemble D17 drafts from pinned public sources. Does not publish anything."""

import argparse
import hashlib
import json
import re
import struct
import subprocess
import tomllib
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "Aleqsd-submission-preparation"})
    with urllib.request.urlopen(request, timeout=45) as response:
        data = response.read(15_000_001)
    if len(data) > 15_000_000:
        raise ValueError(f"Asset too large: {url}")
    return data


def gh_json(endpoint):
    return json.loads(subprocess.check_output(["gh", "api", endpoint], text=True, encoding="utf-8"))


def png_size(data):
    if data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        raise ValueError("Expected a PNG image")
    return struct.unpack(">II", data[16:24])


def assemble(check):
    config = json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))
    expected_assets = []
    for plugin in config["plugins"]:
        plugin_id, repo, commit = plugin["id"], plugin["repository"], plugin["commit"]
        if not re.fullmatch(r"[A-Za-z][A-Za-z0-9]+", plugin_id):
            raise ValueError("Unexpected plugin ID")
        if repo not in ("Aleqsd/hotbar-atelier", "Aleqsd/codex-monitor", "Aleqsd/minimap-zoom"):
            raise ValueError("Unexpected source repository")
        if not re.fullmatch(r"[0-9a-f]{40}", commit):
            raise ValueError(f"Missing exact public commit for {plugin_id}")
        if gh_json(f"repos/{repo}/commits/{commit}")["sha"] != commit:
            raise ValueError(f"Commit mismatch for {plugin_id}")

        source_url = f"https://raw.githubusercontent.com/{repo}/{commit}"
        project = fetch(f"{source_url}/src/{plugin_id}.csproj").decode("utf-8-sig")
        if 'Sdk="Dalamud.NET.Sdk/15.0.0"' not in project:
            raise ValueError(f"Recheck the D17 SDK choice for {plugin_id}")
        json.loads(fetch(f"{source_url}/src/packages.lock.json"))
        if plugin.get("dotnetSdkFile"):
            json.loads(fetch(f"{source_url}/{plugin['dotnetSdkFile']}"))
        description = ET.fromstring(project).findtext(".//Description", default="")
        if plugin.get("descriptionFile"):
            description = json.loads(fetch(f"{source_url}/{plugin['descriptionFile']}"))["Description"]
        if "codex" not in description.casefold() or "icône" not in description.casefold():
            raise ValueError(f"Missing asset disclosure for {plugin_id}")

        folder = ROOT / plugin_id / "testing" / "live" / plugin_id
        manifest = (
            '[plugin]\n'
            f'repository = "https://github.com/{repo}.git"\n'
            f'commit = "{commit}"\n'
            'owners = ["Aleqsd"]\n'
            'project_path = "src"\n'
            f'changelog = {json.dumps(plugin["changelog"], ensure_ascii=False)}\n'
        )
        tomllib.loads(manifest)
        manifest_path = folder / "manifest.toml"
        if check:
            if manifest_path.read_text(encoding="utf-8") != manifest:
                raise ValueError(f"Manifest differs: {plugin_id}")
        else:
            folder.mkdir(parents=True, exist_ok=True)
            manifest_path.write_text(manifest, encoding="utf-8", newline="\n")

        icon_url = config["iconBaseUrl"] + f"/{plugin_id}.png"
        assets = [("icon.png", icon_url, "Icon created with Codex; MIT licence.")]
        if len(plugin["images"]) > 5:
            raise ValueError("D17 accepts at most five preview images")
        assets += [(f"image{i}.png", f"{source_url}/{item['path']}", item["caption"])
                   for i, item in enumerate(plugin["images"], 1)]
        for name, url, caption in assets:
            data = fetch(url)
            width, height = png_size(data)
            if name == "icon.png" and not (width == height and 64 <= width <= 512):
                raise ValueError(f"Invalid icon dimensions: {plugin_id}")
            path = folder / "images" / name
            if check:
                if path.read_bytes() != data:
                    raise ValueError(f"Local asset differs from public source: {path.name}")
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
            expected_assets.append({"file": path.relative_to(ROOT).as_posix(), "source": url,
                                    "sha256": hashlib.sha256(data).hexdigest(),
                                    "width": width, "height": height, "caption": caption})
        print(f"{plugin_id}: public source, metadata, TOML and {len(assets)} PNG files verified")

    provenance = json.dumps(expected_assets, ensure_ascii=False, indent=2) + "\n"
    provenance_path = ROOT / "assets.json"
    if check:
        if provenance_path.read_text(encoding="utf-8") != provenance:
            raise ValueError("Asset provenance differs")
    else:
        provenance_path.write_text(provenance, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify existing drafts against public sources")
    assemble(parser.parse_args().check)
