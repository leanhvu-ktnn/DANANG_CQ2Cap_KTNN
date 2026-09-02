---
okf_version: "0.2"
type: context
title: "Đóng gói — gói tự chứa (copy được)"
updated: 2026-09-02
tags: [dong-goi, Obsidian]
---

# Đóng gói

Thư mục này là **một vault Obsidian đủ dùng cho khóa học**. Copy cả thư mục sang chỗ khác, rồi *Open folder as vault* đúng thư mục này (không mở vault VBPL cha).

Gói **không** mang lớp `INF/` hay `RAW/` (corpus vault cha). Văn bản dẫn chiếu = [[Vanbanquydinh/index|Vanbanquydinh]].

## Wikilink

Path từ **gốc gói** (file [[index]] ở đây). Không `WISDOM/…`.

- Wisdom: [[index]] · [[khai-niem/index|khai-niem]] · [[tiep-can-ktnn/index|tiep-can]] · [[hang-ngay/index|hang-ngay]]
- Giáo trình (hai trục): [[GIAOTRINH/index|GIAOTRINH]] — không copy `KLG/` vào gói
- Tài liệu: [[TAILIEU/index|TAILIEU]] (`.md` + file gốc)
- Văn bản dẫn chiếu: [[Vanbanquydinh/index|Vanbanquydinh]] (metadata + toàn văn + `DieudiemDanchieu`)
- Bản đồ căn cứ: [[can-cu/index|can-cu]]

Khi gói còn nằm trong vault VBPL, `[[KLG/…]]` / `[[INF/…]]` / `[[RAW/…]]` trỏ **corpus cha**. Mở gói độc lập thì các link đó không còn (gói không copy tầng Knowledge).

## Copy

1. Copy nguyên thư mục `DANANG_CQ2cap_Kiemtoan`.
2. Không đổi tên `Vanbanquydinh` / `TAILIEU`.
3. Mở thư mục đã copy thành vault.

## GitHub private (kênh chia sẻ)

SSOT vẫn **thư mục này**. Kênh chia sẻ máy đọc = repo private [`leanhvu-ktnn/DANANG_CQ2Cap_KTNN`](https://github.com/leanhvu-ktnn/DANANG_CQ2Cap_KTNN) — clone sibling cạnh vault VBPL, **không** `git init` trong thư mục gói.

- Lần đầu (writer): `@danang-ktnn-github-init`
- Sau khi sửa gói local, cần đẩy: `@danang-ktnn-github-sync`

Máy đọc: clone/pull repo private, *Open folder as vault* đúng thư mục clone.
