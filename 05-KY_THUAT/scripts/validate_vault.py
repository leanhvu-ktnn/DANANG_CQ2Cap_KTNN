#!/usr/bin/env python3
"""Kiểm tra cấu trúc, metadata, phân nhánh và wikilink của vault."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEGAL_ROOT = ROOT / "Vanbanquydinh"
REPORT = ROOT / "reports" / "bao-cao-kiem-tra.md"
ALLOWED_STATUS = {
    "Còn hiệu lực",
    "Hết hiệu lực một phần",
    "Hết hiệu lực toàn bộ",
    "khong_xac_dinh",
}
GENERATED_BRANCHES = {"NSNN", "TSC", "Chinh_quyen_2_cap"}


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    result: dict[str, str] = {}
    for line in parts[1].splitlines():
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*?)\s*$", line)
        if match:
            result[match.group(1)] = match.group(2).strip().strip("'\"")
    return result


def markdown_files() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)


def strip_code(text: str) -> str:
    text = re.sub(r"(?s)(?:~~~.*?~~~|```.*?```)", "", text)
    return re.sub(r"`[^`\n]*`", "", text)


def resolve_wikilink(target: str) -> bool:
    target = target.strip().replace("\\|", "|")
    if not target or target.startswith("#"):
        return True
    target = target.split("#", 1)[0].strip()
    if target == "hub-goi":
        return (ROOT / "index.md").exists()
    candidate = ROOT / target
    if candidate.exists():
        return True
    # Tên note có thể chứa dấu chấm (ví dụ 23.8.2026) nhưng Obsidian vẫn bỏ
    # đuôi .md; vì vậy nối chuỗi trước khi xét như một tệp có phần mở rộng.
    if Path(str(candidate) + ".md").exists():
        return True
    if candidate.suffix:
        return False
    if (candidate / "index.md").exists() or (candidate / "00-index.md").exists():
        return True
    return False


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    files = markdown_files()

    legal_records: list[tuple[Path, dict[str, str]]] = []
    for path in sorted(LEGAL_ROOT.rglob("index.md")):
        if any(part in GENERATED_BRANCHES for part in path.relative_to(LEGAL_ROOT).parts):
            continue
        text = path.read_text(encoding="utf-8")
        meta = frontmatter(text)
        if meta.get("type") == "legal_instance":
            legal_records.append((path, meta))

    identifiers = [meta.get("van_ban_id", "") for _, meta in legal_records]
    missing_id = [path for path, meta in legal_records if not meta.get("van_ban_id")]
    for path in missing_id:
        errors.append(f"Thiếu van_ban_id: {path.relative_to(ROOT).as_posix()}")
    for identifier, count in Counter(item for item in identifiers if item).items():
        if count > 1:
            errors.append(f"Trùng van_ban_id {identifier}: {count} hồ sơ")

    ontology_stub_counts: Counter[str] = Counter()
    for path, meta in legal_records:
        relative = path.relative_to(ROOT).as_posix()
        if not meta.get("so_hieu"):
            errors.append(f"Thiếu so_hieu: {relative}")
        status = meta.get("tinh_trang_hieu_luc", "")
        if status not in ALLOWED_STATUS:
            errors.append(f"Trạng thái hiệu lực không hợp lệ ({status or 'trống'}): {relative}")
        if status == "khong_xac_dinh" and meta.get("hieu_luc_can_hau_kiem") != "true":
            errors.append(f"Thiếu cờ hậu kiểm hiệu lực: {relative}")
        if not (path.parent / "toan-van.md").exists():
            errors.append(f"Thiếu toan-van.md: {relative}")
        for ontology_name in ("Thucthe.md", "Quanhe.md", "quytrinh.md"):
            ontology_path = path.parent / ontology_name
            if not ontology_path.exists():
                errors.append(f"Thiếu {ontology_name}: {relative}")
            elif "Chưa tách" in ontology_path.read_text(encoding="utf-8"):
                ontology_stub_counts[ontology_name] += 1
    for ontology_name, count in ontology_stub_counts.items():
        warnings.append(f"{count} tệp {ontology_name} còn là stub Chưa tách")

    manifest_path = LEGAL_ROOT / "phan-nhanh.json"
    branch_counts: Counter[str] = Counter()
    if not manifest_path.exists():
        errors.append("Thiếu Vanbanquydinh/phan-nhanh.json")
        manifest_records: list[dict[str, object]] = []
    else:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest_records = manifest.get("records", [])
        except (json.JSONDecodeError, AttributeError) as exc:
            errors.append(f"Manifest phân nhánh không đọc được: {exc}")
            manifest_records = []
    manifest_ids = {str(item.get("van_ban_id", "")) for item in manifest_records if item.get("van_ban_id")}
    legal_ids = {item for item in identifiers if item}
    for item in sorted(legal_ids - manifest_ids):
        errors.append(f"Hồ sơ chưa có trong manifest phân nhánh: {item}")
    for item in sorted(manifest_ids - legal_ids):
        errors.append(f"Manifest tham chiếu hồ sơ không tồn tại: {item}")
    for item in manifest_records:
        branches = item.get("branches", [])
        if not isinstance(branches, list) or not branches:
            errors.append(f"Hồ sơ chưa được gán nhánh: {item.get('so_hieu', '<không số>')}")
            continue
        for branch in branches:
            if branch not in GENERATED_BRANCHES:
                errors.append(f"Nhánh không hợp lệ {branch}: {item.get('so_hieu', '<không số>')}")
            else:
                branch_counts[str(branch)] += 1
    for branch in sorted(GENERATED_BRANCHES):
        if not (LEGAL_ROOT / branch / "index.md").exists():
            errors.append(f"Thiếu chỉ mục nhánh: Vanbanquydinh/{branch}/index.md")

    source_manifest = ROOT / "reports" / "source-manifest.json"
    if not source_manifest.exists():
        errors.append("Thiếu reports/source-manifest.json")
    else:
        try:
            source_records = json.loads(source_manifest.read_text(encoding="utf-8")).get("records", [])
            for item in source_records:
                source_path = ROOT / str(item.get("path", ""))
                if not source_path.exists():
                    errors.append(f"Manifest nguồn trỏ tệp không tồn tại: {item.get('path', '')}")
                if len(str(item.get("sha256", ""))) != 64:
                    errors.append(f"SHA-256 không hợp lệ: {item.get('path', '')}")
        except (json.JSONDecodeError, AttributeError) as exc:
            errors.append(f"Manifest nguồn không đọc được: {exc}")

    link_pattern = re.compile(r"\[\[([^\]]+)\]\]")
    broken: list[str] = []
    shortened_pattern = re.compile(
        r"^GIAOTRINH/hoc-vien/05-phan-ii/chuyen-de-0[1-5]$"
    )
    for path in files:
        cleaned = strip_code(path.read_text(encoding="utf-8"))
        for number, line in enumerate(cleaned.splitlines(), start=1):
            for match in link_pattern.finditer(line):
                raw = match.group(1)
                target = raw.split("|", 1)[0].strip()
                bare = target.split("#", 1)[0]
                if bare == "index":
                    errors.append(f"Wikilink index trần: {path.relative_to(ROOT).as_posix()}:{number}")
                if shortened_pattern.match(bare):
                    errors.append(f"Wikilink chuyên đề rút gọn: {path.relative_to(ROOT).as_posix()}:{number}")
                if not resolve_wikilink(target):
                    broken.append(f"{path.relative_to(ROOT).as_posix()}:{number} -> {target}")
    if broken:
        errors.extend(f"Wikilink gãy: {item}" for item in broken)

    unknown_status = sum(
        1 for _, meta in legal_records if meta.get("tinh_trang_hieu_luc") == "khong_xac_dinh"
    )
    personal_files = sum(
        1 for path in files if frontmatter(path.read_text(encoding="utf-8")).get("personal_data") == "true"
    )
    lines = [
        "---",
        'okf_version: "0.2"',
        "type: report",
        'title: "Báo cáo kiểm tra vault"',
        f"updated: {date.today().isoformat()}",
        "tags: [QA, validator, report]",
        "---",
        "",
        "# Báo cáo kiểm tra vault",
        "",
        f"- Markdown đã quét: {len(files)}",
        f"- Hồ sơ pháp lý: {len(legal_records)}",
        f"- Trạng thái hiệu lực cần hậu kiểm: {unknown_status}",
        f"- Phân nhánh: NSNN {branch_counts['NSNN']} · TSC {branch_counts['TSC']} · Chính quyền 2 cấp {branch_counts['Chinh_quyen_2_cap']}",
        f"- Tệp Markdown gắn dữ liệu cá nhân: {personal_files}",
        f"- Lỗi: {len(errors)}",
        f"- Cảnh báo: {len(warnings)}",
        "",
        "## Lỗi",
        "",
    ]
    lines.extend([f"- {item}" for item in errors] or ["- Không có."])
    lines.extend(["", "## Cảnh báo", ""])
    lines.extend([f"- {item}" for item in warnings] or ["- Không có."])
    lines.extend(["", "## Hồ sơ cần hậu kiểm hiệu lực", ""])
    unknown_records = [
        (path, meta) for path, meta in legal_records
        if meta.get("tinh_trang_hieu_luc") == "khong_xac_dinh"
    ]
    for path, meta in unknown_records:
        target = path.relative_to(ROOT).as_posix()[:-3]
        lines.append(f"- [[{target}|{meta.get('so_hieu', path.parent.name)}]]")
    lines.extend([
        "",
        "## Cách chạy lại",
        "",
        "Từ gốc vault, chạy: python scripts/validate_vault.py",
        "",
        "Ba chỉ mục văn bản được tái tạo bằng: python scripts/rebuild_legal_branches.py",
        "",
    ])
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8")

    print(
        f"Checked {len(files)} markdown files and {len(legal_records)} legal records; "
        f"errors={len(errors)}, warnings={len(warnings)}"
    )
    print(f"Report: {REPORT.relative_to(ROOT).as_posix()}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
