---
okf_version: "0.2"
type: context
title: "Quy ước metadata và kiểm tra vault"
updated: 2026-09-04
tags: [schema, metadata, QA]
---

# Quy ước metadata và kiểm tra vault

## Hồ sơ pháp lý

Schema tham chiếu: legal-instance.schema.json.

- Bắt buộc: type, van_ban_id, so_hieu, tinh_trang_hieu_luc.
- Giá trị hiệu lực được kiểm soát: Còn hiệu lực, Hết hiệu lực một phần, Hết hiệu lực toàn bộ, khong_xac_dinh.
- khong_xac_dinh phải đi kèm hieu_luc_can_hau_kiem: true.
- Khi xác minh, bổ sung verified_at, verified_source và verification_note; không suy đoán.
- Mỗi hồ sơ phải có toan-van.md và có mặt trong Vanbanquydinh/phan-nhanh.json.

## Trang cơ quan

Khuyến nghị cho lần chuẩn hóa tiếp theo: cq_id, status, valid_from, valid_to, verified_at và lienQuanVanBan. Không tự điền hàng loạt khi chưa xác định được nguồn chính thức và mốc hiệu lực.

## Tài liệu nguồn

Tệp chứa dữ liệu cá nhân phải có personal_data: true và distribution: restricted. Xem [[TAILIEU/CHINH-SACH-CHIA-SE|Chính sách chia sẻ]].

## Chạy kiểm tra

Chạy python scripts/validate_vault.py từ gốc vault. Báo cáo Markdown được ghi tại reports/bao-cao-kiem-tra.md.

## Liên kết

- [[Vanbanquydinh/index|Văn bản quy định]]
- [[Dexuat|Đề xuất hoàn thiện]]
- [[hub-goi|Hub gói]]
