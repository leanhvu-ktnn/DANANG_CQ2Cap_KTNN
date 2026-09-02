---
okf_version: "0.2"
type: context
title: "Quy ước wikilink Obsidian — gói Đà Nẵng KTNN"
updated: 2026-09-02
tags: [Obsidian, wikilink, WISDOM, Da_Nang]
---

# Quy ước wikilink Obsidian

Áp dụng cho mọi note Wisdom/hub trong gói này: [[index]], [[TIMHIEU/index|TIMHIEU]], [[GIAOTRINH/index|GIAOTRINH]], [[TAILIEU/index|TAILIEU]], [[Vanbanquydinh/index|Vanbanquydinh]].

**Vault root** = thư mục gói (file này). Máy đọc *Open folder as vault* đúng thư mục clone — không phải root repo VBPL.

## Cú pháp

| Dạng | Dùng khi | Ví dụ |
|------|----------|--------|
| `[[đường/từ-gốc-gói]]` | Link ổn định | `[[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/index]]` |
| `[[đường\|nhãn]]` | Nhãn ngắn | `[[TIMHIEU/index\|TIMHIEU]]` |
| `[[#heading]]` | Trong cùng file | `[[#Prefix cấm]]` |
| `[[note#heading\|nhãn]]` | Heading ở note khác | `[[TIMHIEU/co-quan/index#Sở Tài chính\|Sở Tài chính]]` |

- **Không** ghi đuôi `.md` trong wikilink.
- **Không** dùng `../`.
- **Không** prefix `WISDOM/DANANG_CQ2cap_Kiemtoan/`.

## Prefix được phép

`index` · `TIMHIEU/` · `GIAOTRINH/` · `TAILIEU/` · `Vanbanquydinh/` · `quy-uoc-link`

File trùng tên (`Thucthe.md`, `Quanhe.md`, `quytrinh.md`) — **full path**, không `[[Thucthe]]` trần. Xem [[TAILIEU/ontology|ontology]].

## Prefix cấm (note Wisdom/hub)

`INF/` · `RAW/` · `KLG/` · `references/`

Không link leftover ở gốc gói: `khai-niem/`, `hang-ngay/`, `tiep-can-ktnn/`, `cach-dung/`, `can-cu/` — dùng bản trong `TIMHIEU/`.

| Cần | Dùng |
|-----|------|
| Văn bản đã copy | `[[Vanbanquydinh/…/index\|số hiệu]]` |
| Số hiệu chưa copy | `[[Vanbanquydinh/_chua-co/index#…\|số hiệu]]` |
| Cơ quan | `[[TIMHIEU/co-quan/index#…\|nhãn]]` |
| 2 cấp / sáp nhập QN→ĐN | `[[TIMHIEU/hang-ngay/chinh-quyen-2-cap-da-nang/index\|2 cấp]]` |
| TTHC dân sự | Câu chữ + trang 2 cấp — không giả catalog |

## YAML và URL

- `thuocVanBan` / `nguon_goi` giữ path INF gốc (không bọc `[[ ]]`).
- URL nguồn: markdown `[vbpl.vn](https://vbpl.vn)`.

## Liên kết

- Hub: [[index]]
- Cơ quan: [[TIMHIEU/co-quan/index|co-quan]]
- Chưa copy: [[Vanbanquydinh/_chua-co/index|_chua-co]]
