---
okf_version: "0.2"
type: research
title: "Quan hệ / quy tắc — 157/2025/TT-BTC"
so_hieu: "157/2025/TT-BTC"
updated: 2026-09-02
tags: [ontology, Vanbanquydinh, Da_Nang]
---

# Quanhe — 157/2025/TT-BTC

Tài khoản KBNN. TBox: [[02-TAILIEU/ontology|ontology]]. Cùng thư mục: [[04-Vanbanquydinh/TW/Thong_tu/2025/157-2025-TT-BTC/Thucthe|Thucthe]] · [[04-Vanbanquydinh/TW/Thong_tu/2025/157-2025-TT-BTC/Quanhe|Quanhe]] · [[04-Vanbanquydinh/TW/Thong_tu/2025/157-2025-TT-BTC/quytrinh|quytrinh]] · [[04-Vanbanquydinh/TW/Thong_tu/2025/157-2025-TT-BTC/index|157/2025/TT-BTC]] · [[04-Vanbanquydinh/TW/Thong_tu/2025/157-2025-TT-BTC/toan-van|toàn văn]].

### R:ChuKyXa-ChuTich-va-KeToan
- triple: E:ChuTichUBNDXa --mustSatisfy--> E:TaiKhoanDuToanKBNN
- constraint: NS cấp xã — chữ ký 1: Chủ tịch / Phó CT hoặc Trưởng phòng Kinh tế được phân công Chủ TK bằng văn bản (tối đa 4 người). Chữ ký 2: kế toán / ủy quyền (tối đa 3). Thủ trưởng không ủy quyền chữ ký 2 làm Chủ TK. Đăng ký lại khi đổi người.
- source: [[04-Vanbanquydinh/TW/Thong_tu/2025/157-2025-TT-BTC/DieudiemDanchieu/Dieu-07|TT 157 Điều 7]] k1.b
- diễn giải: Chữ ký trên chứng từ phải khớp mẫu đã đăng ký với KBNN.

### R:TKDuToan-khongNhanTienNgoai
- triple: E:TaiKhoanDuToanKBNN --khongDuoc--> E:TaiKhoanTienGuiKBNN
- constraint: TK DT chỉ rút DT; không nhận tiền đơn vị khác (trừ trả lại / khôi phục DT / thu hồi). Không chuyển tiền tự nguyện / thôn vào TK DT — phải đúng TK tiền gửi đã đăng ký nội dung. Không cho thuê / cho mượn TK.
- source: [[04-Vanbanquydinh/TW/Thong_tu/2025/157-2025-TT-BTC/DieudiemDanchieu/Dieu-09|TT 157 Điều 9]]
- diễn giải: DT ≠ tiền gửi ≠ TK tính chất tiền gửi.

### R:DoiChieuSoDu-truocChuyenNguon
- triple: E:DonViGiaoDichKBNN --mustSatisfy--> E:KhoBacNhaNuoc
- constraint: Tiền gửi: chậm nhất ngày 10 tháng sau (tháng 12 không bắt buộc); năm 10/02. DT cấp 4 / tạm ứng: quý (trừ quý 4) ngày 10 tháng đầu quý sau; năm 10/02. Lệch thì thống nhất điều chỉnh *trước* khóa sổ / chuyển nguồn.
- source: [[04-Vanbanquydinh/TW/Thong_tu/2025/157-2025-TT-BTC/DieudiemDanchieu/Dieu-11|TT 157 Điều 11]]
- diễn giải: Chuyển nguồn chỉ sau khi đối chiếu khớp.

## Liên kết

- [[04-Vanbanquydinh/TW/Thong_tu/2025/157-2025-TT-BTC/Thucthe|Thucthe]] · [[04-Vanbanquydinh/TW/Thong_tu/2025/157-2025-TT-BTC/Quanhe|Quanhe]] · [[04-Vanbanquydinh/TW/Thong_tu/2025/157-2025-TT-BTC/quytrinh|quytrinh]]
- TBox: [[02-TAILIEU/ontology|ontology]] · Hub VB: [[04-Vanbanquydinh/index|Vanbanquydinh]]
