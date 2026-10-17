import hashlib
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/check_google_api_keys.py"
SPEC = importlib.util.spec_from_file_location("check_google_api_keys", SCRIPT)
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)
# 在运行时构造样本，避免常量折叠把密钥形态写入 .pyc。
SAMPLE = bytes([65, 73, 122, 97]) + bytes([65]) * 35


class CheckerTests(unittest.TestCase):
    def test_detects_maps_key_in_http_body(self):
        self.assertEqual([2], CHECKER.find_lines(b"<html>\n<script src='?key=" + SAMPLE + b"'></script>"))

    def test_detects_binary_content(self):
        self.assertEqual([1], CHECKER.find_lines(b"\x00\xff" + SAMPLE))

    def test_multiple_keys_report_individual_lines(self):
        self.assertEqual([1, 2], CHECKER.find_lines(SAMPLE + b"\r\n" + SAMPLE))

    def test_short_value_is_not_a_key(self):
        self.assertEqual([], CHECKER.find_lines(SAMPLE[:-1]))

    def test_redacted_marker_is_not_a_key(self):
        self.assertEqual([], CHECKER.find_lines(CHECKER.REDACTION))

    def test_redaction_is_idempotent(self):
        clean = CHECKER.redact(b"before=" + SAMPLE + b"&after")
        self.assertEqual(b"before=" + CHECKER.REDACTION + b"&after", clean)
        self.assertEqual(clean, CHECKER.redact(clean))

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        self.git("init", "--quiet")

    def git(self, *args):
        return subprocess.check_output(["git", "-c", "core.hooksPath=", "-C", str(self.repo), *args])

    def cli(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), "--repo", str(self.repo), *args],
                              capture_output=True, text=True, encoding="utf-8")

    def test_untracked_capture_is_checked_without_disclosing_key(self):
        (self.repo / "snapshot.body").write_bytes(SAMPLE)
        result = self.cli()
        self.assertEqual(1, result.returncode)
        self.assertNotIn(SAMPLE.decode(), result.stdout + result.stderr)
        self.assertEqual("snapshot.body", json.loads(result.stdout)["findings"][0]["path"])

    def test_key_in_filename_is_redacted_in_diagnostics(self):
        (self.repo / (SAMPLE.decode() + ".body")).write_bytes(SAMPLE)
        result = self.cli()
        self.assertEqual(1, result.returncode)
        self.assertNotIn(SAMPLE.decode(), result.stdout + result.stderr)
        self.assertIn(CHECKER.REDACTION.decode(), result.stdout)

    def test_staged_scan_reads_index_not_clean_worktree(self):
        capture = self.repo / "snapshot.body"
        capture.write_bytes(SAMPLE)
        self.git("add", "snapshot.body")
        capture.write_bytes(CHECKER.REDACTION)
        self.assertEqual(0, self.cli().returncode)
        result = self.cli("--staged")
        self.assertEqual(1, result.returncode)
        self.assertNotIn(SAMPLE.decode(), result.stdout + result.stderr)

    def test_staged_scan_does_not_read_unstaged_dirty_content(self):
        capture = self.repo / "snapshot.body"
        capture.write_bytes(CHECKER.REDACTION)
        self.git("add", "snapshot.body")
        capture.write_bytes(SAMPLE)
        self.assertEqual(0, self.cli("--staged").returncode)
        self.assertEqual(1, self.cli().returncode)

    def test_deleted_capture_does_not_break_current_scan(self):
        capture = self.repo / "snapshot.body"
        capture.write_bytes(b"clean")
        self.git("add", "snapshot.body")
        capture.unlink()
        self.assertEqual(0, self.cli().returncode)

    def test_non_repository_is_error_not_clean(self):
        nested = self.repo / "missing"
        result = subprocess.run([sys.executable, str(SCRIPT), "--repo", str(nested)],
                                capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(2, result.returncode)
        self.assertEqual("error", json.loads(result.stdout)["status"])


class RepositorySecurityTests(unittest.TestCase):
    def test_current_checkout_contains_no_google_api_keys(self):
        paths = subprocess.check_output(
            ["git", "-C", str(ROOT), "ls-files", "--cached", "--others", "--exclude-standard", "-z"]
        ).split(b"\0")
        findings = []
        for raw in set(paths) - {b""}:
            relative = raw.decode("utf-8")
            path = ROOT / relative
            if path.is_file() and re.search(rb"AIza[0-9A-Za-z_-]{35}", path.read_bytes()):
                findings.append(CHECKER.redact(raw).decode("utf-8"))
        self.assertEqual([], sorted(findings), "发现未脱敏的 Google API key，仅列出文件路径。")

    def test_all_existing_integrity_manifests_match(self):
        manifests = sorted(ROOT.glob("**/integrity-manifest.json")) + [
            ROOT / "organized-library/00_Index/manifest.json", ROOT / "research-collection/manifest.json"
        ]
        self.assertGreaterEqual(len(manifests), 14)
        for manifest in manifests:
            base = manifest.parent.parent if manifest.parent.name == "00_Index" else manifest.parent
            payload = json.loads(manifest.read_text(encoding="utf-8"))
            for relative, entry in payload["files"].items():
                with self.subTest(manifest=str(manifest.relative_to(ROOT)), path=relative):
                    data = (base / relative).read_bytes()
                    expected = entry["sha256"] if isinstance(entry, dict) else entry
                    self.assertEqual(expected, hashlib.sha256(data).hexdigest())
                    if isinstance(entry, dict) and "bytes" in entry:
                        self.assertEqual(entry["bytes"], len(data))

    def test_redacted_receipts_resolve_to_current_bytes(self):
        checked = 0
        for round_name in ("2026-10-15-03", "2026-10-15-09"):
            base = ROOT / "research-collection/rounds" / round_name
            def walk(value):
                nonlocal checked
                if isinstance(value, dict):
                    if "body_path" in value and "redaction" in value:
                        data = (base / value["body_path"]).read_bytes()
                        digest = hashlib.sha256(data).hexdigest()
                        self.assertEqual(value["sha256"], digest)
                        self.assertEqual(Path(value["body_path"]).stem, digest)
                        if "bytes" in value:
                            self.assertEqual(value["bytes"], len(data))
                        self.assertNotEqual(value["redaction"]["original_sha256"], digest)
                        self.assertEqual(1, data.count(CHECKER.REDACTION))
                        checked += 1
                    for child in value.values():
                        walk(child)
                elif isinstance(value, list):
                    for child in value:
                        walk(child)
            for path in base.rglob("*.json"):
                walk(json.loads(path.read_text(encoding="utf-8")))
        self.assertEqual(16, checked)


if __name__ == "__main__":
    unittest.main()
