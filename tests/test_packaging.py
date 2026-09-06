import copy
import hashlib
import io
import json
import sys
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from build_repo import make_zip, validate_install_zip, version

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

if __name__ == "__main__":
    unittest.main()
