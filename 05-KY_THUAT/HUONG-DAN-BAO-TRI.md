---
okf_version: "0.2"
type: huong-dan
title: "Hướng dẫn bảo trì và phát hành vault"
updated: 2026-09-04
tags: [bao-tri, QA, phat-hanh]
---

# Hướng dẫn bảo trì và phát hành vault

## Khi thêm/sửa văn bản

1. Giữ hồ sơ tại thư mục số hiệu; không di chuyển bản gốc chỉ để đổi chuyên đề.
2. Bổ sung metadata bắt buộc theo [[schemas/README|quy ước metadata]].
3. Có toan-van.md, Thucthe.md, Quanhe.md và quytrinh.md.
4. Cập nhật tập phân loại trong scripts/rebuild_legal_branches.py nếu cần.
5. Chạy lần lượt:
   - python scripts/rebuild_legal_branches.py
   - python scripts/build_source_manifest.py
   - python scripts/validate_vault.py
6. Đọc [[reports/bao-cao-kiem-tra|báo cáo kiểm tra]]; không phát hành khi còn lỗi.

## Chu kỳ hậu kiểm

- Trước mỗi đợt tập huấn/phát hành: kiểm tra 14 hồ sơ đang gắn cờ hậu kiểm hiệu lực.
- Khi có văn bản mới: kiểm tra văn bản sửa đổi, thay thế, bãi bỏ và cập nhật ngày/nguồn xác minh.
- Khi bộ máy thay đổi: đối chiếu danh sách cơ quan chính thức; không suy tổng số cơ quan từ số trang trong vault.
- Khi thay PDF/DOCX: chạy lại manifest SHA-256 và ghi thay đổi vào CHANGELOG.md.

## Gói chia sẻ

- Tuân thủ [[02-TAILIEU/CHINH-SACH-CHIA-SE|chính sách dữ liệu cá nhân]].
- Giữ nguyên cấu trúc đường dẫn Obsidian.
- Mở thử bản sao như một vault mới; kiểm tra các lối vào BAT-DAU-5-PHUT, ba nhánh văn bản, giáo trình và phụ lục.

## Tiêu chí phát hành

- Validator: 0 lỗi; cảnh báo đã được ghi nhận và có người xử lý.
- Manifest nguồn khớp đúng các PDF/DOCX phát hành.
- Không còn tệp restricted trong gói công khai.
- Các trang mới có metadata, liên kết về hub và ngày cập nhật.

