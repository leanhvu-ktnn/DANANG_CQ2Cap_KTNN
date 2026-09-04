#!/usr/bin/env python3
"""Lập manifest SHA-256 cho các tệp nguồn PDF/DOCX trong vault."""

from __future__ import annotations

import hashlib
import json
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "reports" / "source-manifest.json"
EXTENSIONS = {".pdf", ".docx"}


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def main() -> int:
    records = []
    for path in sorted(ROOT.rglob("*")):
        if path.is_file() and path.suffix.lower() in EXTENSIONS:
            records.append(
                {
                    "path": path.relative_to(ROOT).as_posix(),
                    "size_bytes": path.stat().st_size,
                    "sha256": digest(path),
                }
            )
    payload = {
        "schema_version": "1.0",
        "generated_at": date.today().isoformat(),
        "algorithm": "sha256",
        "records": records,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Hashed {len(records)} source files -> {OUTPUT.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
