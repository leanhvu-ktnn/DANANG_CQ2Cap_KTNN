---
okf_version: "0.2"
type: research
title: "Quan hệ / quy tắc — 254/2025/NĐ-CP"
so_hieu: "254/2025/NĐ-CP"
updated: 2026-09-02
tags: [ontology, Vanbanquydinh, Da_Nang]
---

# Quanhe — 254/2025/NĐ-CP

Thanh toán vốn ĐTC. TBox: [[02-TAILIEU/ontology|ontology]]. Cùng thư mục: [[04-Vanbanquydinh/TW/Nghi_dinh/2025/254-2025-NĐ-CP/Thucthe|Thucthe]] · [[04-Vanbanquydinh/TW/Nghi_dinh/2025/254-2025-NĐ-CP/Quanhe|Quanhe]] · [[04-Vanbanquydinh/TW/Nghi_dinh/2025/254-2025-NĐ-CP/quytrinh|quytrinh]] · [[04-Vanbanquydinh/TW/Nghi_dinh/2025/254-2025-NĐ-CP/index|254/2025/NĐ-CP]] · [[04-Vanbanquydinh/TW/Nghi_dinh/2025/254-2025-NĐ-CP/toan-van|toàn văn]].

### R:ChuDauTu-quanLy-DuAnDauTuCong
- triple: E:ChuDauTu --duocGiaoQuanLy--> E:DuAnDauTuCong
- constraint: Được giao trực tiếp quản lý dự án đầu tư công; mở TK tại KBNN để thanh toán vốn.
- source: Luật 58/2024 Điều 4 k7; [[04-Vanbanquydinh/TW/Nghi_dinh/2025/254-2025-NĐ-CP/DieudiemDanchieu/Dieu-05|NĐ 254 Điều 5]]
- diễn giải: CĐT vừa quản lý dự án vừa là cửa giao dịch KBNN.

### R:KBNN-giaiNgan-VonDauTuCong
- triple: E:KhoBacNhaNuoc --giaiNgan--> E:VonDauTuCong
- constraint: Giải ngân vốn ĐTC nguồn NSNN và nguồn thu hợp pháp CQNN dành để đầu tư; kiểm soát hồ sơ tạm ứng / khối lượng hoàn thành.
- source: NĐ 254 Điều 4 k1; [[04-Vanbanquydinh/TW/Nghi_dinh/2025/254-2025-NĐ-CP/DieudiemDanchieu/Dieu-09|Điều 9]]; [[04-Vanbanquydinh/TW/Nghi_dinh/2025/254-2025-NĐ-CP/DieudiemDanchieu/Dieu-10|Điều 10]]
- diễn giải: Vốn ĐTC không chi tiền mặt ngoài KBNN.

### R:HoSoThanhToanVonDT-mustSatisfy-Dieu8
- triple: E:ChuDauTu --mustSatisfy--> E:VonDauTuCong
- constraint: Hồ sơ pháp lý gửi lần đầu (KH ĐTC năm, QĐ/VB giao nhiệm vụ hoặc QĐ phê duyệt DA, bảng thông tin HĐ / DT / BT-TĐC). Mỗi lần tạm ứng / thanh toán: giấy đề nghị + chứng từ theo khoản 2–3. Không lấy mẫu chi TX NĐ 347 thay bộ này.
- source: [[04-Vanbanquydinh/TW/Nghi_dinh/2025/254-2025-NĐ-CP/DieudiemDanchieu/Dieu-08|NĐ 254 Điều 8]]
- diễn giải: Thiếu thành phần Điều 8 = KBNN không giải ngân. Mở Điều, không nhớ miệng mẫu.

## Liên kết

- [[04-Vanbanquydinh/TW/Nghi_dinh/2025/254-2025-NĐ-CP/Thucthe|Thucthe]] · [[04-Vanbanquydinh/TW/Nghi_dinh/2025/254-2025-NĐ-CP/Quanhe|Quanhe]] · [[04-Vanbanquydinh/TW/Nghi_dinh/2025/254-2025-NĐ-CP/quytrinh|quytrinh]]
- TBox: [[02-TAILIEU/ontology|ontology]] · Hub VB: [[04-Vanbanquydinh/index|Vanbanquydinh]]
