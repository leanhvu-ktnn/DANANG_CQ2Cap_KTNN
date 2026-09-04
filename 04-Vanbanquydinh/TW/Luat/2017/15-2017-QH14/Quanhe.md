---
okf_version: "0.2"
type: research
title: "Quan hệ / quy tắc — 15/2017/QH14"
so_hieu: "15/2017/QH14"
updated: 2026-09-02
tags: [ontology, Vanbanquydinh, Da_Nang]
---

# Quanhe — 15/2017/QH14

Luật TSC. TBox: [[02-TAILIEU/ontology|ontology]]. Cùng thư mục: [[04-Vanbanquydinh/TW/Luat/2017/15-2017-QH14/Thucthe|Thucthe]] · [[04-Vanbanquydinh/TW/Luat/2017/15-2017-QH14/Quanhe|Quanhe]] · [[04-Vanbanquydinh/TW/Luat/2017/15-2017-QH14/quytrinh|quytrinh]] · [[04-Vanbanquydinh/TW/Luat/2017/15-2017-QH14/index|15/2017/QH14]] · [[04-Vanbanquydinh/TW/Luat/2017/15-2017-QH14/toan-van|toàn văn]].

### R:NhaNuoc-giaoQuyenQLSD-TaiSanCong
- triple: E:TaiSanCong --duocGiaoQuyenQLSD--> E:DonViSNCL
- constraint: Mọi TSC phải được Nhà nước giao quyền quản lý, quyền sử dụng hoặc hình thức trao quyền khác.
- source: [[04-Vanbanquydinh/TW/Luat/2017/15-2017-QH14/DieudiemDanchieu/Dieu-06|Luật 15 Điều 6]] k1
- diễn giải: Không “tự chiếm” TSC ngoài quyết định giao.

### R:KhaiThacTSC-phai-CoCheThiTruong
- triple: E:KhaiThacTSC --mustSatisfy--> E:NguonLucTaiChinhTuTSC
- constraint: Khai thác nguồn lực TC từ TSC phải theo cơ chế thị trường, hiệu quả, công khai, minh bạch, đúng pháp luật.
- source: [[04-Vanbanquydinh/TW/Luat/2017/15-2017-QH14/DieudiemDanchieu/Dieu-06|Luật 15 Điều 6]] k5
- diễn giải: Không cho thuê/LDLK nội bộ, giá cảm tính.

### R:DonViSNCL-khongDungNSNNMuaSamChiDeKinhDoanh
- triple: E:DonViSNCL --khongDuoc--> E:LienDoanhLienKetTSC
- constraint: Không bố trí NSNN mua sắm TSC chỉ để kinh doanh, cho thuê, liên doanh liên kết.
- source: [[04-Vanbanquydinh/TW/Luat/2017/15-2017-QH14/DieudiemDanchieu/Dieu-52|Luật 15 Điều 52]] k2
- diễn giải: Mua sắm từ NS phải phục vụ chức năng, nhiệm vụ — không “mua để kinh doanh”.

### R:BoTaiChinh-dauMoiQLNN-TSC
- triple: E:BoTaiChinh --hasDuty--> E:TaiSanCong
- constraint: Đầu mối giúp Chính phủ thống nhất QLNN về TSC; vận hành HTTT và CSDLQG TSC; công khai TSC cả nước.
- source: [[04-Vanbanquydinh/TW/Luat/2017/15-2017-QH14/DieudiemDanchieu/Dieu-15|Luật 15 Điều 15]]
- diễn giải: Bộ Tài chính là đầu mối TSC quốc gia.

### R:UBNDTinh-daiDienChuSoHuu-TSCDiaPhuong
- triple: E:UBNDTinh --daiDienChuSoHuu--> E:TaiSanCong
- constraint: Đại diện chủ sở hữu TSC thuộc địa phương; công khai, báo cáo BTC/HĐND.
- source: Luật 15 Điều 18 k1
- diễn giải: UBND tỉnh đại diện chủ sở hữu TSC địa phương.

### R:MatTranToQuoc-chuTriGiamSatCongDong-TSC
- triple: E:MatTranToQuoc --chuTriGiamSatCongDong--> E:TaiSanCong
- constraint: Trừ bí mật nhà nước; nội dung gồm chấp hành PL, tình hình ĐT/mua sắm/xử lý, khai thác nguồn lực, công khai TSC.
- source: [[04-Vanbanquydinh/TW/Luat/2017/15-2017-QH14/DieudiemDanchieu/Dieu-09|Luật 15 Điều 9]]
- diễn giải: MTTQ chủ trì GS cộng đồng TSC, song song GS NSNN (Luật 89 Đ.16).

### R:KiemToanNhaNuoc-kiemToan-QLSD-TSC
- triple: E:KiemToanNhaNuoc --kiemToan--> E:TaiSanCong
- constraint: Kiểm toán việc QLSĐ TSC; công khai kết quả theo Luật Kiểm toán nhà nước.
- source: Luật 15 Điều 14; [[04-Vanbanquydinh/TW/Luat/2017/15-2017-QH14/DieudiemDanchieu/Dieu-08|Điều 8]] k4.d
- diễn giải: KTNN kiểm toán cả NSNN và TSC.

### R:Cam-loiDungChucVu-TSC
- triple: E:NguoiDungDauCoQuanToChucDonVi --biCam--> E:TaiSanCong
- constraint: Cấm chiếm đoạt, chiếm giữ, sử dụng trái phép; ĐT/mua sắm/giao/thuê vượt định mức; KD/cho thuê/LDLK không phù hợp mục đích; xử lý TSC trái PL; hủy hoại.
- source: [[04-Vanbanquydinh/TW/Luat/2017/15-2017-QH14/DieudiemDanchieu/Dieu-10|Luật 15 Điều 10]]
- diễn giải: Mười nhóm hành vi bị cấm — checklist trước khi ký xử lý TSC.

## Liên kết

- [[04-Vanbanquydinh/TW/Luat/2017/15-2017-QH14/Thucthe|Thucthe]] · [[04-Vanbanquydinh/TW/Luat/2017/15-2017-QH14/Quanhe|Quanhe]] · [[04-Vanbanquydinh/TW/Luat/2017/15-2017-QH14/quytrinh|quytrinh]]
- TBox: [[02-TAILIEU/ontology|ontology]] · Hub VB: [[04-Vanbanquydinh/index|Vanbanquydinh]]
