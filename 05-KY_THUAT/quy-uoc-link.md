---
okf_version: "0.2"
type: context
title: "Quy ước wikilink Obsidian — gói Đà Nẵng KTNN"
updated: 2026-09-02
tags: [Obsidian, wikilink, WISDOM, Da_Nang]
---

# Quy ước wikilink Obsidian

Áp dụng cho mọi note Wisdom/hub trong gói này: [[hub-goi|Hub gói]], [[03-TIMHIEU/index|TIMHIEU]], [[01-GIAOTRINH/00-index|GIAOTRINH]], [[02-TAILIEU/index|TAILIEU]], [[04-Vanbanquydinh/index|Vanbanquydinh]].

**Không** `[[hub-goi]]` / `[[00-index]]` trần — nhiều folder note trùng tên; từ một trang con, Obsidian hay nhảy về chính trang đang mở. Hub gốc có alias `hub-goi`.

**Vault root** = thư mục gói (file này). Máy đọc *Open folder as vault* đúng thư mục clone — không phải root repo VBPL.

## Cú pháp

| Dạng | Dùng khi | Ví dụ |
|------|----------|--------|
| `[[đường/từ-gốc-gói]]` | Link ổn định | `[[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/index]]` |
| `[[đường\|nhãn]]` | Nhãn ngắn | `[[03-TIMHIEU/index\|TIMHIEU]]` |
| `[[#heading]]` | Trong cùng file | `[[#Prefix cấm]]` |
| `[[note#heading\|nhãn]]` | Heading ở note khác | `[[03-TIMHIEU/co-quan/index#Sở Tài chính\|Sở Tài chính]]` |

- **Không** ghi đuôi `.md` trong wikilink.
- **Không** dùng `../`.
- **Không** prefix `WISDOM/DANANG_CQ2cap_Kiemtoan/`.
- **Không** thư mục chỉ có 1 file `.md` — gộp thành `tên.md` (không `tên/index.md` / `tên/00-index.md`). Đã áp dụng `GIAOTRINH/cam-nang/` và `GIAOTRINH/hoc-vien/`.
- Trong `GIAOTRINH/cam-nang` và `GIAOTRINH/hoc-vien`: mọi số hiệu / Điều đã có trong `Vanbanquydinh/` phải wikilink **ngay chỗ nhắc** (kể cả «Nắm để làm» / «Kỹ năng»), không để plain text. Không có Dieudiem → `.../index`. CV chưa catalog giữ chữ.
- Trong `GIAOTRINH`, folder note là `00-index` (sắp xếp trước `00-triet-ly`, `01-…`, `buoi-01`, `cam-nang`); `Vanbanquydinh` / `TIMHIEU` / `TAILIEU` giữ `index`.

## Prefix được phép

`hub-goi` · `TIMHIEU/` · `GIAOTRINH/` · `TAILIEU/` · `Vanbanquydinh/` · `quy-uoc-link`

File trùng tên (`Thucthe.md`, `Quanhe.md`, `quytrinh.md`) — **full path**, không `[[Thucthe]]` trần. Xem [[02-TAILIEU/ontology|ontology]].

## Prefix cấm (note Wisdom/hub)

`INF/` · `RAW/` · `KLG/` · `references/`

Không link leftover ở gốc gói: `khai-niem/`, `hang-ngay/`, `tiep-can-ktnn/`, `cach-dung/`, `can-cu/` — dùng bản trong `TIMHIEU/`.

| Cần | Dùng |
|-----|------|
| Văn bản đã copy | `[[04-Vanbanquydinh/…/index\|số hiệu]]` |
| Cơ quan | `[[03-TIMHIEU/co-quan/index#…\|nhãn]]` |
| 2 cấp / sáp nhập QN→ĐN | `[[03-TIMHIEU/hang-ngay/chinh-quyen-2-cap-da-nang/index\|2 cấp]]` |
| TTHC dân sự | Câu chữ + trang 2 cấp — không giả catalog |

## YAML và URL

- `thuocVanBan` / `nguon_goi` giữ path INF gốc (không bọc `[[ ]]`).
- URL nguồn: markdown `[vbpl.vn](https://vbpl.vn)`.

## Liên kết

- Hub: [[hub-goi]]
- Cơ quan: [[03-TIMHIEU/co-quan/index|co-quan]]
- Văn bản: [[04-Vanbanquydinh/index|Vanbanquydinh]]
