---
okf_version: "0.2"
type: research
title: "Quan hệ / quy tắc — 73/2026/NĐ-CP"
so_hieu: "73/2026/NĐ-CP"
updated: 2026-09-02
tags: [ontology, Vanbanquydinh, Da_Nang]
---

# Quanhe — 73/2026/NĐ-CP

Chi tiết Luật NSNN. TBox: [[02-TAILIEU/ontology|ontology]]. Cùng thư mục: [[04-Vanbanquydinh/TW/Nghi_dinh/2026/73-2026-NĐ-CP/Thucthe|Thucthe]] · [[04-Vanbanquydinh/TW/Nghi_dinh/2026/73-2026-NĐ-CP/Quanhe|Quanhe]] · [[04-Vanbanquydinh/TW/Nghi_dinh/2026/73-2026-NĐ-CP/quytrinh|quytrinh]] · [[04-Vanbanquydinh/TW/Nghi_dinh/2026/73-2026-NĐ-CP/index|73/2026/NĐ-CP]] · [[04-Vanbanquydinh/TW/Nghi_dinh/2026/73-2026-NĐ-CP/toan-van|toàn văn]].

### R:NganSachCapXa-khongDuoc-BoiChi
- triple: E:NganSachCapXa --khongDuoc--> E:BoiChiNganSachNhaNuoc
- constraint: Chỉ ngân sách địa phương **cấp tỉnh** được bội chi; bội chi chỉ dùng đầu tư dự án thuộc kế hoạch đầu tư công trung hạn đã được HĐND cấp tỉnh quyết định.
- source: [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-07|Luật 89 Điều 7]] k5.a; NĐ 73 Điều 3 k1, k4
- diễn giải: Xã không được lập hoặc thực hiện bội chi.

### R:ChiNSNN-bonLopKiemSoat
- triple: E:ThuTruongDonVi --quyetDinhChi--> E:DonViSuDungNganSach
- constraint: (1) có DT được giao trừ tạm cấp; (2) thủ trưởng/CĐT/ủy quyền quyết định chi; (3) đủ điều kiện theo loại chi — ĐTC / TX / DTQG / đấu thầu / đặt hàng; (4) KBNN kiểm tra hồ sơ–đối chiếu DT.
- source: [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-12|Luật 89 Điều 12]] k2.a–đ; NĐ 73 Điều 21 k1–k2
- diễn giải: Chi chỉ hợp pháp khi đồng thời đủ bốn lớp.

### R:KBNN-tuChoiThanhToan-KhiKhongCoDuToan
- triple: E:KhoBacNhaNuoc --tuChoiThanhToan--> E:DonViSuDungNganSach
- constraint: Trừ tạm cấp Điều 53; hoặc từ chối theo TTHC KBNN / quản lý thanh toán vốn ĐTC.
- source: NĐ 73 Điều 21 k2
- diễn giải: KBNN là lớp kiểm soát cuối: không DT thì không chi.

### R:CoQuanTaiChinh-tamDinhChiChi-KhiViPhamBaoCao
- triple: E:CoQuanTaiChinh --tamDinhChiChi--> E:DonViDuToanNganSach
- constraint: Không chấp hành báo cáo/QT; trừ lương, phụ cấp, trợ cấp XH, học bổng và một số chi thiết yếu.
- source: Luật 89 Điều 65 k2; NĐ 73 Điều 21 k4; [[04-Vanbanquydinh/TW/Thong_tu/2026/26-2026-TT-BTC/DieudiemDanchieu/Dieu-15|TT 26 Điều 15]] k1
- diễn giải: Tài chính có thể khóa chi (trừ chi con người/thiết yếu) nếu đơn vị không báo cáo/QT đúng hạn.

## 3. Lập, giao, điều chỉnh dự toán

### R:ThuTuong-giaoDuToan-DonViDuToanCapI
- triple: E:ThuTuongChinhPhu --giaoDuToan--> E:DonViDuToanCapI
- constraint: Trước 20/11 giao DT thu–chi năm sau cho từng bộ, cơ quan TW và từng tỉnh.
- source: Luật 89 Điều 26 k2; [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-46|Điều 46]] k5; NĐ 73 Điều 15 k9
- diễn giải: Thủ tướng giao DT cấp I trung ương và NS tỉnh sau nghị quyết Quốc hội.

### R:BoTaiChinh-giaoChiTiet-DuToan
- triple: E:BoTaiChinh --giaoChiTiet--> E:DuToan
- constraint: Chậm nhất 05 ngày làm việc kể từ quyết định giao của Thủ tướng.
- source: Luật 89 Điều 27 k6; NĐ 73 Điều 15 k10
- diễn giải: BTC cụ thể hóa quyết định Thủ tướng thành nhiệm vụ thu–chi chi tiết.

### R:HDNDTinh-quyetDinhDuToan-truoc10Thang12
- triple: E:HDNDTinh --quyetDinh--> E:DuToan
- constraint: Trước ngày 10/12.
- source: [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-46|Luật 89 Điều 46]] k6; NĐ 73 Điều 15 k11
- diễn giải: HĐND tỉnh khóa DT và phân bổ NS cấp tỉnh trước 10/12.

### R:HDNDXa-quyetDinhDuToan-sauHDNDTinh
- triple: E:HDNDXa --quyetDinh--> E:DuToan
- constraint: Chậm nhất 10 ngày kể từ ngày HĐND tỉnh quyết định DT và phân bổ.
- source: [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-46|Luật 89 Điều 46]] k6; NĐ 73 Điều 15 k12
- diễn giải: Xã quyết định DT sau khi đã có số giao từ tỉnh.

### R:DonViDuToanCapI-phanBo-DonViSuDungNS
- triple: E:DonViDuToanCapI --allocatesTo--> E:DonViSuDungNganSach
- constraint: Đúng tổng mức và chi tiết lĩnh vực; cơ quan tài chính kiểm tra, yêu cầu điều chỉnh chậm nhất 10 ngày làm việc nếu sai.
- source: [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-51|Luật 89 Điều 51]]; [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-52|Điều 52]]; NĐ 73 Điều 19
- diễn giải: Chỉ cấp I được phân bổ DT cho ĐVSDNS.

### R:ChinhPhu-xuLyTangThu-DuToanChiConLai
- triple: E:ChinhPhu --quyetDinhSuDung--> E:DuToanChiConLaiCuaCapNganSach
- constraint: Dùng cho giảm bội chi/trả nợ, tăng dự phòng và quỹ DT (trong trần Đ.10, Đ.11), nguồn lương, tăng ĐT, an sinh; BTC trình trước 28/02 năm sau.
- source: [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-61|Luật 89 Điều 61]] k2; NĐ 73 Điều 26 k1
- diễn giải: Tăng thu và DT chi còn lại NSTW do Chính phủ phân bổ, không tự động chi.

### R:UBND-xuLyTangThu-CapMinh
- triple: E:UBNDCacCap --quyetDinhSuDung--> E:DuToanChiConLaiCuaCapNganSach
- constraint: Cùng nội dung ưu tiên Điều 61 k2; cơ quan tài chính trình trước 28/02; báo cáo Thường trực HĐND và HĐND kỳ gần nhất.
- source: [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-32|Luật 89 Điều 32]] k3; [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-61|Điều 61]] k2; NĐ 73 Điều 26 k2
- diễn giải: UBND (không phải HĐND) quyết định phương án tăng thu/DT còn lại của cấp mình.

### R:NganSachCapTren-hoTroHutThu-CapDuoi
- triple: E:NganSachDiaPhuong --hoTroKhiHutThu--> E:NganSachCapXa
- constraint: Chỉ khi hụt thu do nguyên nhân khách quan, đã điều chỉnh giảm chi và dùng hết nguồn hợp pháp khác.
- source: [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-61|Luật 89 Điều 61]] k5; NĐ 73 Điều 26 k6
- diễn giải: Hụt thu khách quan mới được cấp trên hỗ trợ cân đối.

## 4. Dự phòng

### R:ThuTuong-quyetDinhSuDung-DuPhongNSTW
- triple: E:ThuTuongChinhPhu --hasAuthority--> E:DuPhongNganSachNhaNuoc
- constraint: Định kỳ báo cáo Chính phủ → UBTVQH và báo cáo Quốc hội kỳ họp gần nhất; BTC chủ trì tổng hợp trình; báo cáo quý chậm nhất ngày 20 sau hết quý.
- source: [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-10|Luật 89 Điều 10]] k4.a; NĐ 73 Điều 25 k2.a, k4
- diễn giải: Chỉ Thủ tướng được quyết định dùng dự phòng NSTW.

### R:UBND-quyetDinhSuDung-DuPhongCapMinh
- triple: E:UBNDCacCap --hasAuthority--> E:DuPhongNganSachNhaNuoc
- constraint: Định kỳ báo cáo Thường trực HĐND và HĐND cùng cấp kỳ họp gần nhất; cơ quan tài chính trình UBND.
- source: [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-10|Luật 89 Điều 10]] k4.b; NĐ 73 Điều 25 k2.b, k4
- diễn giải: UBND cấp nào quyết định dự phòng cấp đó.

## 5. Quyết toán

### R:HDNDXa-pheChuanQuyetToan-truoc31Thang3
- triple: E:HDNDXa --pheChuan--> E:QuyetToan
- constraint: Trước 31/3 năm sau; gửi UBND cấp tỉnh chậm nhất 05 ngày làm việc sau phê chuẩn; nếu chưa chuẩn thì trình lại chậm nhất 10 ngày làm việc.
- source: [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-71|Luật 89 Điều 71]] k3–k4; NĐ 73 Điều 32 k5
- swrl: HDNDXa(?x) ∧ BaoCaoQT(?y) ∧ cuaCap(?y,?x) → pheChuanTruoc(?x,?y,"31-03-N+1")
- diễn giải: QT xã phải được HĐND xã phê chuẩn trong quý I năm sau.

### R:UBNDTinh-guiQT-truoc01Thang5
- triple: E:UBNDTinh --reportsTo--> E:BoTaiChinh
- constraint: UBND cấp tỉnh gửi BTC và KTNN trước 01/5; QT đã HĐND tỉnh phê chuẩn gửi lại trước 05/7.
- source: [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-71|Luật 89 Điều 71]] k3; [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-72|Điều 72]] k2; NĐ 73 Điều 32 k6–k7
- diễn giải: Tỉnh gửi hồ sơ QT cho BTC/KTNN hai mốc 01/5 và 05/7.

### R:DonViDuToanCapTren-xetDuyetQT-DonViSuDungNS
- triple: E:DonViDuToanNganSach --xetDuyetQuyetToan--> E:DonViSuDungNganSach
- constraint: Khớp sổ kế toán với xác nhận KBNN; đủ điều kiện chi Điều 12; được yêu cầu xuất toán chi sai.
- source: [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-69|Luật 89 Điều 69]]; NĐ 73 Điều 32 k3
- diễn giải: Xét duyệt QT là trách nhiệm cấp trên trực tiếp, không phải của HĐND.

### R:KetDuTWTinh-xuLy-QuyDuTruVaThuNamSau
- triple: E:KetDuNganSachTWVaCapTinh --xuLyBang--> E:QuyDuTruTaiChinh
- constraint: Ưu tiên trả nợ gốc và lãi chưa bố trí đủ; số còn lại 50% vào quỹ DT tài chính cùng cấp, 50% thu NS năm sau; nếu quỹ đã đủ 25% DT chi năm thì toàn bộ vào thu năm sau. Thực hiện sau khi Quốc hội/HĐND phê chuẩn QT.
- source: [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-74|Luật 89 Điều 74]] k1; NĐ 73 Điều 33 k2.a
- diễn giải: Kết dư TW/tỉnh: trả nợ trước, rồi chia quỹ DT và thu năm sau.

### R:KetDuXa-hachToan-ThuNamSau
- triple: E:KetDuNganSachCapXa --hachToanVao--> E:NganSachCapXa
- constraint: Toàn bộ kết dư xã hạch toán vào thu ngân sách năm sau (không trích quỹ DT tài chính).
- source: [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-74|Luật 89 Điều 74]] k1; NĐ 73 Điều 33 k2.b
- diễn giải: Xã không có quỹ dự trữ tài chính riêng từ kết dư.

### R:ChiSauQT-khongDieuChinhQTDaPheChuan
- triple: E:QuyetToan --xuLySaiPhamVaoNamXuLy--> E:NamNganSach
- constraint: Thu hồi/chi hoàn trả hạch toán vào năm xử lý; không điều chỉnh QT đã Quốc hội/HĐND phê chuẩn.
- source: [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-75|Luật 89 Điều 75]]; Điều 67 k8; NĐ 73 Điều 32 k8
- diễn giải: Phát hiện sai sau phê chuẩn thì xử lý trên NS năm hiện hành.

## 6. Tài sản công

## Liên kết

- [[04-Vanbanquydinh/TW/Nghi_dinh/2026/73-2026-NĐ-CP/Thucthe|Thucthe]] · [[04-Vanbanquydinh/TW/Nghi_dinh/2026/73-2026-NĐ-CP/Quanhe|Quanhe]] · [[04-Vanbanquydinh/TW/Nghi_dinh/2026/73-2026-NĐ-CP/quytrinh|quytrinh]]
- TBox: [[02-TAILIEU/ontology|ontology]] · Hub VB: [[04-Vanbanquydinh/index|Vanbanquydinh]]
