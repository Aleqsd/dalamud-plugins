import copy
import hashlib
import io
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from build_repo import make_zip, validate_install_zip, version
import build_repo

class InstallerPackagingChecks(unittest.TestCase):
    def setUp(self):
        self.entry = {"InternalName": "Example", "AssemblyVersion": "1.2.3.0", "DalamudApiLevel": 15}
        self.files = {
            "Example.dll": b"original released DLL",
            "Example.json": json.dumps(self.entry).encode(),
            "LICENSE": b"MIT",
            "icon.png": (Path(__file__).resolve().parents[1] / "icons/HotbarAtelier.png").read_bytes()
        }
        self.hash = hashlib.sha256(self.files["Example.dll"]).hexdigest()

    def check(self, files=None, entry=None):
        validate_install_zip(make_zip(self.files if files is None else files), self.entry if entry is None else entry, self.hash)

    def test_flat_package_and_version_normalization(self):
        self.check()
        self.assertEqual(version("1.2.3"), version("1.2.3.0"))

    def test_developer_folder_is_rejected(self):
        files = {"plugin/" + key: data for key, data in self.files.items()}
        with self.assertRaises(ValueError): self.check(files)

    def test_mismatched_manifest_version_is_rejected(self):
        entry = dict(self.entry, AssemblyVersion="1.2.4.0")
        with self.assertRaises(ValueError): self.check(entry=entry)

    def test_changed_dll_is_rejected(self):
        files = dict(self.files, **{"Example.dll": b"another DLL"})
        with self.assertRaises(ValueError): self.check(files)

    def test_private_local_state_is_rejected(self):
        manifest = dict(self.entry, InstalledFromUrl="local development")
        files = dict(self.files, **{"Example.json": json.dumps(manifest).encode()})
        with self.assertRaises(ValueError): self.check(files)

    def test_parent_path_is_rejected(self):
        files = dict(self.files, **{"../outside.txt": b"outside"})
        with self.assertRaises(ValueError): self.check(files)

    def test_invalid_icon_is_rejected(self):
        files = dict(self.files, **{"icon.png": b"<html>404</html>"})
        with self.assertRaises(ValueError): self.check(files)

    def test_incompatible_api_is_rejected(self):
        entry = dict(self.entry, DalamudApiLevel=16)
        with self.assertRaises(ValueError): self.check(entry=entry)

    def test_archives_are_reproducible(self):
        self.assertEqual(make_zip(self.files), make_zip(self.files))

class ReleasedArchiveChecks(unittest.TestCase):
    original_dll = b"original released DLL"

    def build_release(self, dll=None, standalone_digest=None, archive_digest=None):
        internal = "HotbarAtelier"
        manifest = {"InternalName": internal, "AssemblyVersion": "1.2.3.0",
                    "DalamudApiLevel": 15, "Description": "Example plugin"}
        archive = make_zip({internal + ".dll": self.original_dll if dll is None else dll,
                            internal + ".json": json.dumps(manifest).encode(), "LICENSE": b"MIT"})
        archive_hash = hashlib.sha256(archive).hexdigest()
        assets = [{"name": "release.zip", "digest": "sha256:" + (archive_digest or archive_hash),
                   "browser_download_url": "https://example.invalid/release.zip"}]
        if standalone_digest is not None:
            assets.append({"name": internal + ".dll", "digest": standalone_digest})
        metadata = {"draft": False, "assets": assets, "published_at": "2026-09-07T00:00:00Z",
                    "html_url": "https://example.invalid/release"}
        config = {"repository": "Aleqsd/dalamud-plugins", "packageRelease": "test-release", "plugins": [{
            "repo": "hotbar-atelier", "id": internal, "tag": "v1.2.3", "commit": "a" * 40,
            "archive": "release.zip", "archiveSha256": archive_hash,
            "dllSha256": hashlib.sha256(self.original_dll).hexdigest(),
            "prefix": "", "files": [internal + ".dll", internal + ".json"],
            "icon": "icon.png", "image": "preview.png", "changelog": "Example update"}]}
        icon = (Path(__file__).resolve().parents[1] / "icons/HotbarAtelier.png").read_bytes()
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "LICENSE").write_bytes(b"MIT")
            (root / "icon.png").write_bytes(icon)
            with patch.object(build_repo, "ROOT", root), \
                 patch.object(build_repo, "github", side_effect=[metadata, {"sha": "a" * 40}]), \
                 patch.object(build_repo, "fetch", return_value=archive), patch("builtins.print"):
                output = build_repo.build(config)
            return (output / "HotbarAtelier-1.2.3-dalamud.zip").read_bytes()

    def test_zip_only_release_keeps_the_pinned_dll(self):
        with zipfile.ZipFile(io.BytesIO(self.build_release())) as archive:
            self.assertEqual(archive.read("HotbarAtelier.dll"), self.original_dll)

    def test_zip_only_release_still_rejects_changed_dll(self):
        with self.assertRaisesRegex(ValueError, "pinned DLL hash"):
            self.build_release(dll=b"unexpected replacement")

    def test_conflicting_standalone_dll_is_not_ignored(self):
        with self.assertRaisesRegex(ValueError, "Standalone DLL digest"):
            self.build_release(standalone_digest="sha256:" + "0" * 64)

    def test_zip_only_release_requires_the_archive_digest(self):
        with self.assertRaisesRegex(ValueError, "Source release digest"):
            self.build_release(archive_digest="0" * 64)

if __name__ == "__main__":
    unittest.main()
