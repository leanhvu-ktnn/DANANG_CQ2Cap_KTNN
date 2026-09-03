---
okf_version: "0.2"
type: research
title: "Quan hệ / quy tắc — 185/2015/TT-BTC"
so_hieu: "185/2015/TT-BTC"
updated: 2026-09-02
tags: [ontology, Vanbanquydinh, Da_Nang]
---

# Quanhe — 185/2015/TT-BTC

Mã ĐVQHNS. TBox: [[TAILIEU/ontology|ontology]]. Cùng thư mục: [[Vanbanquydinh/TW/Thong_tu/2015/185-2015-TT-BTC/Thucthe|Thucthe]] · [[Vanbanquydinh/TW/Thong_tu/2015/185-2015-TT-BTC/Quanhe|Quanhe]] · [[Vanbanquydinh/TW/Thong_tu/2015/185-2015-TT-BTC/quytrinh|quytrinh]] · [[Vanbanquydinh/TW/Thong_tu/2015/185-2015-TT-BTC/index|185/2015/TT-BTC]] · [[Vanbanquydinh/TW/Thong_tu/2015/185-2015-TT-BTC/toan-van|toàn văn]].

### R:MotDonVi-motMaDVQHNS
- triple: E:DonViCoQuanHeVoiNganSach --mustSatisfy--> E:DonViCoQuanHeVoiNganSach
- constraint: Mỗi đơn vị chỉ được cấp **một mã số duy nhất**; ghi trên mọi chứng từ giao dịch NS. Xã đăng ký tại Sở Tài chính. Không tái sử dụng mã đã đóng.
- source: [[Vanbanquydinh/TW/Thong_tu/2015/185-2015-TT-BTC/DieudiemDanchieu/Dieu-03|TT 185 Điều 3]] k1; [[Vanbanquydinh/TW/Thong_tu/2015/185-2015-TT-BTC/DieudiemDanchieu/Dieu-04|Điều 4]]
- diễn giải: Một đơn vị một mã suốt đời.

### R:SapNhap-dongMa-DonViBiSapNhap
- triple: E:SoTaiChinh --hasDuty--> E:DonViCoQuanHeVoiNganSach
- constraint: Sáp nhập: đơn vị nhận giữ mã cũ (đổi thông tin nếu cần); đơn vị bị sáp nhập — STC đóng mã (Điều 13). Chia tách: đơn vị mới = mã mới; đơn vị bị chia tách giữ mã cũ. Hạch toán mã đã đóng = sai cả chuỗi QT.
- source: [[Vanbanquydinh/TW/Thong_tu/2015/185-2015-TT-BTC/DieudiemDanchieu/Dieu-14|TT 185 Điều 14]]
- diễn giải: Sau sắp xếp 2 cấp — rà mã từng trường / trạm y tế trước khi gửi chứng từ.

## Liên kết

- [[Vanbanquydinh/TW/Thong_tu/2015/185-2015-TT-BTC/Thucthe|Thucthe]] · [[Vanbanquydinh/TW/Thong_tu/2015/185-2015-TT-BTC/Quanhe|Quanhe]] · [[Vanbanquydinh/TW/Thong_tu/2015/185-2015-TT-BTC/quytrinh|quytrinh]]
- TBox: [[TAILIEU/ontology|ontology]] · Hub VB: [[Vanbanquydinh/index|Vanbanquydinh]]
