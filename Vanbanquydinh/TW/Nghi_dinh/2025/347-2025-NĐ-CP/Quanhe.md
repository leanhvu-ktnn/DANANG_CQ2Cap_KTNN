---
okf_version: "0.2"
type: research
title: "Quan hệ / quy tắc — 347/2025/NĐ-CP"
so_hieu: "347/2025/NĐ-CP"
updated: 2026-09-02
tags: [ontology, Vanbanquydinh, Da_Nang]
---

# Quanhe — 347/2025/NĐ-CP

TTHC Kho bạc (mới). TBox: [[TAILIEU/ontology|ontology]]. Cùng thư mục: [[Vanbanquydinh/TW/Nghi_dinh/2025/347-2025-NĐ-CP/Thucthe|Thucthe]] · [[Vanbanquydinh/TW/Nghi_dinh/2025/347-2025-NĐ-CP/Quanhe|Quanhe]] · [[Vanbanquydinh/TW/Nghi_dinh/2025/347-2025-NĐ-CP/quytrinh|quytrinh]] · [[Vanbanquydinh/TW/Nghi_dinh/2025/347-2025-NĐ-CP/index|347/2025/NĐ-CP]] · [[Vanbanquydinh/TW/Nghi_dinh/2025/347-2025-NĐ-CP/toan-van|toàn văn]].

### R:ChiTX-thanhToanQua-KBNN
- triple: E:ChiThuongXuyen --mustSatisfy--> E:KhoBacNhaNuoc
- constraint: Chi TX (và CTMTQG từ nguồn sự nghiệp, DTQG từ nguồn TX, viện trợ không hoàn lại bố trí từ TX) gửi hồ sơ KBNN nơi giao dịch — không chi tiền mặt ngoài kho. Cửa này **không** dùng cho vốn ĐT công (NĐ 254).
- source: [[Vanbanquydinh/TW/Nghi_dinh/2025/347-2025-NĐ-CP/DieudiemDanchieu/Dieu-06|NĐ 347 Điều 6]] k1–k2
- diễn giải: Tách cửa TX vs vốn ĐT trước khi lập hồ sơ.

### R:KBNN-kiemHoSo-ChiTX
- triple: E:KhoBacNhaNuoc --kiemTra--> E:ChungTuChuyenTien
- constraint: Hồ sơ hợp lệ (Điều 3 k4); chữ ký số / chữ ký–dấu khớp đăng ký; mã nội dung kinh tế Mục lục NSNN khớp nội dung chi; tiền mặt đúng chế độ; tổng các lần không vượt HĐ / QĐ hỗ trợ–đặt hàng; danh sách thụ hưởng khớp tổng chứng từ. Từ chối = Mẫu 33.
- source: [[Vanbanquydinh/TW/Nghi_dinh/2025/347-2025-NĐ-CP/DieudiemDanchieu/Dieu-06|NĐ 347 Điều 6]] k2.b, k2.k
- diễn giải: KBNN kiểm hồ sơ–mã–chữ ký, không duyệt chi thay thủ trưởng.

### R:ChiDieu40-dungHoSoTX-khongMauDTC
- triple: E:ChiThuongXuyen --mustSatisfy--> E:ChungTuChuyenTien
- constraint: Khoản bố trí từ hai nguồn ĐT+TX (Luật 89 Điều 40) — hồ sơ theo chế độ chi TX hai nguồn. Sửa chữa trong dự án đã xây dựng: không nộp bộ hồ sơ vốn ĐT NĐ 254.
- source: [[Vanbanquydinh/TW/Nghi_dinh/2025/347-2025-NĐ-CP/DieudiemDanchieu/Dieu-06|NĐ 347 Điều 6]] k3.a; [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-40|Luật 89 Điều 40]]
- diễn giải: Gửi nhầm mẫu ĐT = từ chối.

### R:KBNN-giaiQuyet-01NgayLV
- triple: E:KhoBacNhaNuoc --hasDeadline--> E:DonViGiaoDichKBNN
- constraint: Chậm nhất 01 ngày LV sau hồ sơ hợp lệ; 25–31/01 và 25–31/12: 02 ngày LV.
- source: [[Vanbanquydinh/TW/Nghi_dinh/2025/347-2025-NĐ-CP/DieudiemDanchieu/Dieu-06|NĐ 347 Điều 6]] k5
- diễn giải: Không dồn hồ sơ sau 25/12 nếu có thể.

## Liên kết

- [[Vanbanquydinh/TW/Nghi_dinh/2025/347-2025-NĐ-CP/Thucthe|Thucthe]] · [[Vanbanquydinh/TW/Nghi_dinh/2025/347-2025-NĐ-CP/Quanhe|Quanhe]] · [[Vanbanquydinh/TW/Nghi_dinh/2025/347-2025-NĐ-CP/quytrinh|quytrinh]]
- TBox: [[TAILIEU/ontology|ontology]] · Hub VB: [[Vanbanquydinh/index|Vanbanquydinh]]
