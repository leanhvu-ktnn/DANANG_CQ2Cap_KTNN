#!/usr/bin/env python3
"""Tạo ba chỉ mục chuyên đề cho hồ sơ pháp lý mà không di chuyển bản gốc."""

from __future__ import annotations

import json
import re
from collections import Counter
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEGAL_ROOT = ROOT / "Vanbanquydinh"
BRANCHES = {
    "NSNN": {
        "title": "Ngân sách nhà nước (NSNN)",
        "purpose": "Lập, chấp hành, kế toán, kiểm soát, quyết toán, kiểm toán và các nguồn lực tài chính công.",
    },
    "TSC": {
        "title": "Tài sản công (TSC)",
        "purpose": "Đầu tư, mua sắm, quản lý, sử dụng, hao mòn, xử lý tài sản công và hạ tầng.",
    },
    "Chinh_quyen_2_cap": {
        "title": "Chính quyền 2 cấp",
        "purpose": "Tổ chức bộ máy, địa giới, phân định/phân cấp thẩm quyền và áp dụng tại Đà Nẵng sau sắp xếp.",
    },
}

# Các tập dưới đây là phân loại phục vụ tra cứu khóa học, không phải phân loại
# pháp lý chính thức. Một văn bản được phép thuộc nhiều nhánh.
TSC_IDS = {
    "07/2022/QH15", "10/2026/QĐ-TTg", "14/2026/QĐ-UBND",
    "15/2017/QH14", "15/2025/QĐ-TTg", "22/2023/QH15",
    "24/2023/QH15", "31/2024/QH15", "43/2024/QH15",
    "56/2024/QH15", "58/2024/QH15", "61/2025/QĐ-CTUBND",
    "64/2020/QH14", "70/2024/TT-BTC", "90/2025/QH15",
    "127/2025/NĐ-CP", "135/2025/QH15", "141/2025/TT-BTC",
    "186/2025/NĐ-CP", "214/2025/NĐ-CP", "254/2025/NĐ-CP",
    "286/2025/NĐ-CP",
}

CQ2_IDS = {
    "14/NQ-HĐND", "19/2025/QĐ-TTg", "20/2025/TT-BYT",
    "27-NQ/TW", "57-NQ/TW", "57/2025/TT-BTC", "60/2021/NĐ-CP",
    "72/2025/QH15", "111/2022/NĐ-CP", "111/2025/NĐ-CP",
    "125/2025/NĐ-CP", "150/2025/NĐ-CP", "152/2025/NĐ-CP",
    "173/2025/NĐ-CP", "202/2025/QH15", "1659/NQ-UBTVQH15",
}

NSNN_IDS = {
    "01/2026/TT-KTNN", "11/2020/NĐ-CP", "11/2018/NQ-HĐND",
    "14/NQ-HĐND", "15/2025/NQ-HĐND", "19/2020/TT-BTC",
    "26/2026/TT-BTC", "27-NQ/TW", "28/2022/NQ-HĐND",
    "29/2022/NQ-HĐND", "52/2025/NQ-HĐND", "56/2022/TT-BTC",
    "56/2025/TT-BTC", "58/2024/QH15", "60/2021/NĐ-CP",
    "66/2026/TT-BTC", "71/2026/QĐ-UBND", "73/2024/NĐ-CP",
    "73/2026/NĐ-CP", "77/2017/TT-BTC", "79/2026/NQ-HĐND",
    "81/2015/QH13", "83/2015/QH13", "88/2015/QH13",
    "89/2025/QH15", "89/VBHN-VPQH", "90/2025/QH15",
    "111/2022/NĐ-CP", "111/2025/NĐ-CP", "125/2025/NĐ-CP",
    "130/2025/TT-BTC", "132/2025/TT-BTC", "133/2025/TT-BTC",
    "145/2025/QH15", "157/2025/TT-BTC", "161/2026/NĐ-CP",
    "185/2015/TT-BTC", "245/2025/QH15", "254/2025/NĐ-CP",
    "324/2016/TT-BTC", "347/2025/NĐ-CP",
}


def scalar(frontmatter: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.*?)\s*$", frontmatter)
    if not match:
        return ""
    return match.group(1).strip().strip("'\"")


def classify(record: dict[str, str]) -> list[str]:
    number = record["so_hieu"]
    relative = record["path"]
    branches: list[str] = []
    if number in NSNN_IDS:
        branches.append("NSNN")
    if number in TSC_IDS:
        branches.append("TSC")
    if number in CQ2_IDS or relative.startswith(("Vanbanquydinh/Da_Nang/", "Vanbanquydinh/Quang_Nam_cu/")):
        branches.append("Chinh_quyen_2_cap")
    # Mọi hồ sơ phải có một lối vào. Hồ sơ dẫn chiếu chung chưa thuộc TSC/CQ2
    # được đặt ở NSNN vì đây là trục chính của khóa học.
    if not branches:
        branches.append("NSNN")
    return branches


def read_records() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    branch_roots = {LEGAL_ROOT / name for name in BRANCHES}
    for path in sorted(LEGAL_ROOT.rglob("index.md")):
        if any(parent in path.parents for parent in branch_roots):
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        frontmatter = text.split("---", 2)[1]
        if scalar(frontmatter, "type") != "legal_instance":
            continue
        relative = path.relative_to(ROOT).as_posix()
        title = scalar(frontmatter, "tom_tat") or scalar(frontmatter, "title")
        record: dict[str, object] = {
            "van_ban_id": scalar(frontmatter, "van_ban_id"),
            "so_hieu": scalar(frontmatter, "so_hieu"),
            "title": title,
            "path": relative,
        }
        record["branches"] = classify(record)  # type: ignore[arg-type]
        records.append(record)
    return records


def scope_group(record: dict[str, object]) -> str:
    number = str(record["so_hieu"])
    if number in {"202/2025/QH15", "1659/NQ-UBTVQH15", "19/2025/QĐ-TTg"}:
        return "bo-sung-chinh-quyen-2-cap"
    if number in {"83/2015/QH13", "81/2015/QH13", "55/2019/QH14", "01/2026/TT-KTNN"}:
        return "wisdom-bo-sung"
    return "catalog-khoa-hoc"


def write_branch(name: str, records: list[dict[str, object]]) -> None:
    info = BRANCHES[name]
    selected = [record for record in records if name in record["branches"]]
    groups: dict[str, list[dict[str, object]]] = {"Đà Nẵng": [], "Quảng Nam cũ": [], "Trung ương": []}
    for record in selected:
        path = str(record["path"])
        group = "Đà Nẵng" if "/Da_Nang/" in path else "Quảng Nam cũ" if "/Quang_Nam_cu/" in path else "Trung ương"
        groups[group].append(record)

    lines = [
        "---",
        'okf_version: "0.2"',
        "type: index",
        f'title: "{info["title"]}"',
        f"updated: {date.today().isoformat()}",
        f"tags: [Vanbanquydinh, {name}, phan-nhanh]",
        "generated: true",
        "generator: scripts/rebuild_legal_branches.py",
        "---",
        "",
        f'# {info["title"]}',
        "",
        str(info["purpose"]),
        "",
        "> [!NOTE]",
        "> Đây là lớp phân nhánh phục vụ tra cứu và học tập, không thay cho việc xác định lĩnh vực hoặc hiệu lực pháp lý chính thức. Một văn bản có thể xuất hiện ở nhiều nhánh; bản gốc không bị di chuyển.",
        "",
        f"**Số hồ sơ trong nhánh:** {len(selected)} / {len(records)}.",
        "",
    ]
    for group, items in groups.items():
        if not items:
            continue
        lines.extend([f"## {group} ({len(items)})", ""])
        for record in sorted(items, key=lambda item: (str(item["so_hieu"]), str(item["path"]))):
            target = str(record["path"])[:-3]
            summary = str(record["title"]).replace("\n", " ").strip()
            if len(summary) > 150:
                summary = summary[:147].rstrip() + "…"
            lines.append(f'- [[{target}|{record["so_hieu"]}]] — {summary}')
        lines.append("")
    lines.extend([
        "## Liên kết",
        "",
        "- [[Vanbanquydinh/index|Bản đồ văn bản quy định]]",
        "- [[Vanbanquydinh/NSNN/index|Nhánh NSNN]]",
        "- [[Vanbanquydinh/TSC/index|Nhánh TSC]]",
        "- [[Vanbanquydinh/Chinh_quyen_2_cap/index|Nhánh Chính quyền 2 cấp]]",
        "- [[hub-goi|Hub gói]]",
        "",
    ])
    destination = LEGAL_ROOT / name / "index.md"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    records = read_records()
    if not records:
        raise SystemExit("Không tìm thấy hồ sơ type: legal_instance")
    identifiers = [str(record["van_ban_id"]) for record in records if record["van_ban_id"]]
    duplicates = [item for item, count in Counter(identifiers).items() if count > 1]
    if duplicates:
        raise SystemExit(f"Trùng van_ban_id: {', '.join(duplicates)}")

    for record in records:
        record["scope_group"] = scope_group(record)
    manifest = {
        "schema_version": "1.0",
        "generated_at": date.today().isoformat(),
        "note": "Phân nhánh phục vụ tra cứu khóa học; không phải phân loại pháp lý chính thức.",
        "records": records,
    }
    (LEGAL_ROOT / "phan-nhanh.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    for name in BRANCHES:
        write_branch(name, records)

    branch_counts = Counter(branch for record in records for branch in record["branches"])
    print(f"Generated branches for {len(records)} records: " + ", ".join(f"{key}={branch_counts[key]}" for key in BRANCHES))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
