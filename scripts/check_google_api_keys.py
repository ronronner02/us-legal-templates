"""检查当前文件或暂存区中的 Google API key，输出只包含路径和行号。"""

import argparse
import json
import os
import re
import subprocess
from pathlib import Path


GOOGLE_API_KEY = re.compile(rb"AIza[0-9A-Za-z_-]{35}")
REDACTION = b"[REDACTED_GOOGLE_API_KEY]"


def find_lines(data):
    return [data.count(b"\n", 0, match.start()) + 1 for match in GOOGLE_API_KEY.finditer(data)]


def redact(data):
    return GOOGLE_API_KEY.sub(REDACTION, data)


def git(repo, *args):
    return subprocess.run(
        ["git", "-C", str(repo), *args], check=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    ).stdout


def scan(repo, staged=False):
    args = ("diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z") if staged else (
        "ls-files", "--cached", "--others", "--exclude-standard", "-z"
    )
    paths = sorted(set(git(repo, *args).split(b"\0")) - {b""})
    findings = []
    checked = 0
    for raw in paths:
        relative = raw.decode("utf-8")
        path = repo / relative
        if staged:
            data = git(repo, "show", ":" + relative)
        elif path.is_symlink():
            data = os.fsencode(os.readlink(path))
        else:
            try:
                data = path.read_bytes()
            except FileNotFoundError:
                continue
        checked += 1
        safe_path = redact(raw).decode("utf-8")
        findings.extend({"path": safe_path, "line": line, "rule": "google_api_key"}
                        for line in find_lines(data))
    return {"status": "failed" if findings else "passed", "files_checked": checked, "findings": findings}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--staged", action="store_true", help="读取暂存区内容，而非工作区内容")
    args = parser.parse_args()
    try:
        repo = Path(git(args.repo, "rev-parse", "--show-toplevel").decode("utf-8").strip())
        result = scan(repo, args.staged)
    except (OSError, UnicodeError, subprocess.CalledProcessError):
        print(json.dumps({"status": "error", "reason": "repository_or_file_read_failed"}))
        return 2
    print(json.dumps(result, ensure_ascii=False))
    return 1 if result["findings"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
