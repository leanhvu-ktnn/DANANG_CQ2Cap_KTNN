---
okf_version: "0.2"
type: research
title: "Quan hệ / quy tắc — 89/2025/QH15"
so_hieu: "89/2025/QH15"
updated: 2026-09-02
tags: [ontology, Vanbanquydinh, Da_Nang]
---

# Quanhe — 89/2025/QH15

Luật NSNN. TBox: [[TAILIEU/ontology|ontology]]. Cùng thư mục: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/Thucthe|Thucthe]] · [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/Quanhe|Quanhe]] · [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/quytrinh|quytrinh]] · [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/index|89/2025/QH15]] · [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/toan-van|toàn văn]].

### R:NganSachCapXa-khongDuoc-BoiChi
- triple: E:NganSachCapXa --khongDuoc--> E:BoiChiNganSachNhaNuoc
- constraint: Chỉ ngân sách địa phương **cấp tỉnh** được bội chi; bội chi chỉ dùng đầu tư dự án thuộc kế hoạch đầu tư công trung hạn đã được HĐND cấp tỉnh quyết định.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-07|Luật 89 Điều 7]] k5.a; NĐ 73 Điều 3 k1, k4
- diễn giải: Xã không được lập hoặc thực hiện bội chi.

### R:NganSachCapXa-khongQuyetToanChiLonHonThu
- triple: E:NganSachCapXa --khongQuyetToanChiLonHon--> E:QuyetToan
- constraint: Báo cáo quyết toán NS cấp xã không được quyết toán chi lớn hơn thu.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-67|Luật 89 Điều 67]] k5
- diễn giải: Khi xét duyệt/phê chuẩn QT xã, chi không được vượt thu thực hiện.

### R:VayBoiChi-chiDuocDungCho-ChiDauTuPhatTrien
- triple: E:BoiChiNganSachNhaNuoc --chiDuocSuDungCho--> E:ChiDauTuPhatTrien
- constraint: Không sử dụng vay bù đắp bội chi cho chi thường xuyên.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-07|Luật 89 Điều 7]] k3
- diễn giải: Vay bội chi chỉ tài trợ đầu tư phát triển.

### R:DuPhong-mucBoTri
- triple: E:DuPhongNganSachNhaNuoc --mucBoTri--> E:DuToan
- constraint: 2%–5% tổng chi mỗi cấp; chi cấp trên không gồm bổ sung cân đối cho cấp dưới; chi cấp dưới không gồm bổ sung có mục tiêu từ cấp trên.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-10|Luật 89 Điều 10]] k1
- diễn giải: Mỗi cấp phải để dự phòng trong khung 2–5% tổng chi (đã loại trừ bổ sung liên cấp).

### R:ThuNSNN-tongHopDayDu-KhongGanNhiemVuChi
- triple: E:NganSachNhaNuoc --tongHopThu--> E:DuToan
- constraint: Thu từ thuế, phí, lệ phí và khoản thu khác tổng hợp đầy đủ vào cân đối NSNN, nguyên tắc không gắn nhiệm vụ chi cụ thể (trừ trường hợp luật định).
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-07|Luật 89 Điều 7]] k1
- diễn giải: Không “ghi thu ghi chi” tùy tiện ngoài trường hợp pháp luật cho phép gắn thu–chi.

### R:HDNDTinh-phanCap-NganSachCapXa
- triple: E:HDNDTinh --phanCapThuChi--> E:NganSachCapXa
- constraint: Phù hợp phân cấp KT-XH, QP-AN và khả năng quản lý từng địa phương; quyết định tỷ lệ % phân chia thu tỉnh–xã.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-09|Luật 89 Điều 9]] k3; [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-31|Điều 31]] k9.d–đ; [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-41|Điều 41]]
- diễn giải: HĐND tỉnh là cấp duy nhất phân cấp nguồn thu, nhiệm vụ chi giữa tỉnh và xã.

### R:NhiemVuChi-thuocCapNao-doCapDoBaoDam
- triple: E:NganSachCapXa --baoDam--> E:ChiThuongXuyen
- constraint: Nhiệm vụ chi thuộc ngân sách cấp nào do ngân sách cấp đó bảo đảm, trừ hỗ trợ khẩn cấp, kết hợp nhiệm vụ, dự phòng hỗ trợ địa phương khác, vốn ĐTPT cho công trình cấp trên trên địa bàn.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-09|Luật 89 Điều 9]] k5
- diễn giải: Không chuyển việc của cấp mình sang cấp khác nếu không thuộc ngoại lệ k5.

## 2. Chi — bốn lớp kiểm soát

### R:ChiNSNN-phaiCo-DuToanGiao
- triple: E:ChiThuongXuyen --mustSatisfy--> E:DuToan
- constraint: Trừ tạm cấp theo Điều 53; đồng thời phải có quyết định chi của thủ trưởng ĐVSDNS, chủ đầu tư hoặc người được ủy quyền.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-08|Luật 89 Điều 8]] k4; [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-12|Điều 12]] k2
- diễn giải: Không có dự toán được giao (trừ tạm cấp) thì không được chi.

### R:ChiNSNN-bonLopKiemSoat
- triple: E:ThuTruongDonVi --quyetDinhChi--> E:DonViSuDungNganSach
- constraint: (1) có DT được giao trừ tạm cấp; (2) thủ trưởng/CĐT/ủy quyền quyết định chi; (3) đủ điều kiện theo loại chi — ĐTC / TX / DTQG / đấu thầu / đặt hàng; (4) KBNN kiểm tra hồ sơ–đối chiếu DT.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-12|Luật 89 Điều 12]] k2.a–đ; NĐ 73 Điều 21 k1–k2
- diễn giải: Chi chỉ hợp pháp khi đồng thời đủ bốn lớp.

### R:ChiDauTu-mustSatisfy-LuatDauTuCong
- triple: E:ChiDauTuPhatTrien --mustSatisfy--> E:DauTuCong
- constraint: Chi đầu tư phát triển phải đáp ứng điều kiện Luật Đầu tư công và pháp luật liên quan.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-12|Luật 89 Điều 12]] k2.a
- diễn giải: Có DT chưa đủ — còn phải đủ thủ tục ĐTC.

### R:ChiThuongXuyen-mustSatisfy-CheDoTieuChuanDinhMuc
- triple: E:ChiThuongXuyen --mustSatisfy--> E:TieuChuanDinhMucTSC
- constraint: Chi TX đúng chế độ, tiêu chuẩn, định mức; đơn vị tự chủ theo quy chế chi tiêu nội bộ và DT được giao tự chủ.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-12|Luật 89 Điều 12]] k2.b
- diễn giải: Chi TX không “tự nghĩ ra” ngoài chế độ/định mức hoặc QCTN đã duyệt.

### R:GoiThau-mustSatisfy-PhapLuatDauThau
- triple: E:GoiThau --mustSatisfy--> E:DauThau
- constraint: Gói thầu tư vấn, mua sắm hàng hóa, xây lắp phải tổ chức theo pháp luật đấu thầu.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-12|Luật 89 Điều 12]] k2.d
- diễn giải: Chi có DT vẫn sai nếu bỏ qua LCNT.

### R:CoQuanTaiChinh-tamDinhChiChi-KhiViPhamBaoCao
- triple: E:CoQuanTaiChinh --tamDinhChiChi--> E:DonViDuToanNganSach
- constraint: Không chấp hành báo cáo/QT; trừ lương, phụ cấp, trợ cấp XH, học bổng và một số chi thiết yếu.
- source: Luật 89 Điều 65 k2; NĐ 73 Điều 21 k4; [[Vanbanquydinh/TW/Thong_tu/2026/26-2026-TT-BTC/DieudiemDanchieu/Dieu-15|TT 26 Điều 15]] k1
- diễn giải: Tài chính có thể khóa chi (trừ chi con người/thiết yếu) nếu đơn vị không báo cáo/QT đúng hạn.

## 3. Lập, giao, điều chỉnh dự toán

### R:QuocHoi-quyetDinh-DuToanNSNN
- triple: E:QuocHoi --quyetDinh--> E:DuToan
- constraint: Trước ngày 10/11 quyết định DT NSNN và phân bổ NSTW năm sau.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-19|Luật 89 Điều 19]] k4–k5; [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-46|Điều 46]] k4
- diễn giải: Quốc hội khóa DT quốc gia trước 10/11.

### R:ThuTuong-giaoDuToan-DonViDuToanCapI
- triple: E:ThuTuongChinhPhu --giaoDuToan--> E:DonViDuToanCapI
- constraint: Trước 20/11 giao DT thu–chi năm sau cho từng bộ, cơ quan TW và từng tỉnh.
- source: Luật 89 Điều 26 k2; [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-46|Điều 46]] k5; NĐ 73 Điều 15 k9
- diễn giải: Thủ tướng giao DT cấp I trung ương và NS tỉnh sau nghị quyết Quốc hội.

### R:BoTaiChinh-giaoChiTiet-DuToan
- triple: E:BoTaiChinh --giaoChiTiet--> E:DuToan
- constraint: Chậm nhất 05 ngày làm việc kể từ quyết định giao của Thủ tướng.
- source: Luật 89 Điều 27 k6; NĐ 73 Điều 15 k10
- diễn giải: BTC cụ thể hóa quyết định Thủ tướng thành nhiệm vụ thu–chi chi tiết.

### R:HDNDTinh-quyetDinhDuToan-truoc10Thang12
- triple: E:HDNDTinh --quyetDinh--> E:DuToan
- constraint: Trước ngày 10/12.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-46|Luật 89 Điều 46]] k6; NĐ 73 Điều 15 k11
- diễn giải: HĐND tỉnh khóa DT và phân bổ NS cấp tỉnh trước 10/12.

### R:HDNDXa-quyetDinhDuToan-sauHDNDTinh
- triple: E:HDNDXa --quyetDinh--> E:DuToan
- constraint: Chậm nhất 10 ngày kể từ ngày HĐND tỉnh quyết định DT và phân bổ.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-46|Luật 89 Điều 46]] k6; NĐ 73 Điều 15 k12
- diễn giải: Xã quyết định DT sau khi đã có số giao từ tỉnh.

### R:UBND-giaoDuToan-sauHDND
- triple: E:UBNDCacCap --giaoDuToan--> E:DonViDuToanCapI
- constraint: Chậm nhất 05 ngày làm việc kể từ ngày HĐND quyết định DT; hoàn thành giao đến ĐVSDNS trước 31/12.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-46|Luật 89 Điều 46]] k7–k8; [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-52|Điều 52]] k2.a
- diễn giải: UBND giao DT ngay sau nghị quyết HĐND.

### R:DonViDuToanCapI-phanBo-DonViSuDungNS
- triple: E:DonViDuToanCapI --allocatesTo--> E:DonViSuDungNganSach
- constraint: Đúng tổng mức và chi tiết lĩnh vực; cơ quan tài chính kiểm tra, yêu cầu điều chỉnh chậm nhất 10 ngày làm việc nếu sai.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-51|Luật 89 Điều 51]]; [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-52|Điều 52]]; NĐ 73 Điều 19
- diễn giải: Chỉ cấp I được phân bổ DT cho ĐVSDNS.

### R:DieuChinhDTDonVi-hanChot15Thang12
- triple: E:DonViDuToanCapI --dieuChinhDuToan--> E:DonViSuDungNganSach
- constraint: Hoàn thành trước ngày 15/12 năm hiện hành (trừ kế hoạch ĐTC theo Luật ĐTC).
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-55|Luật 89 Điều 55]] k3
- diễn giải: Không điều chỉnh DT đã giao ĐVSDNS sau 15/12.

### R:ChinhPhu-xuLyTangThu-DuToanChiConLai
- triple: E:ChinhPhu --quyetDinhSuDung--> E:DuToanChiConLaiCuaCapNganSach
- constraint: Dùng cho giảm bội chi/trả nợ, tăng dự phòng và quỹ DT (trong trần Đ.10, Đ.11), nguồn lương, tăng ĐT, an sinh; BTC trình trước 28/02 năm sau.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-61|Luật 89 Điều 61]] k2; NĐ 73 Điều 26 k1
- diễn giải: Tăng thu và DT chi còn lại NSTW do Chính phủ phân bổ, không tự động chi.

### R:UBND-xuLyTangThu-CapMinh
- triple: E:UBNDCacCap --quyetDinhSuDung--> E:DuToanChiConLaiCuaCapNganSach
- constraint: Cùng nội dung ưu tiên Điều 61 k2; cơ quan tài chính trình trước 28/02; báo cáo Thường trực HĐND và HĐND kỳ gần nhất.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-32|Luật 89 Điều 32]] k3; [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-61|Điều 61]] k2; NĐ 73 Điều 26 k2
- diễn giải: UBND (không phải HĐND) quyết định phương án tăng thu/DT còn lại của cấp mình.

### R:NganSachCapTren-hoTroHutThu-CapDuoi
- triple: E:NganSachDiaPhuong --hoTroKhiHutThu--> E:NganSachCapXa
- constraint: Chỉ khi hụt thu do nguyên nhân khách quan, đã điều chỉnh giảm chi và dùng hết nguồn hợp pháp khác.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-61|Luật 89 Điều 61]] k5; NĐ 73 Điều 26 k6
- diễn giải: Hụt thu khách quan mới được cấp trên hỗ trợ cân đối.

## 4. Dự phòng

### R:ThuTuong-quyetDinhSuDung-DuPhongNSTW
- triple: E:ThuTuongChinhPhu --hasAuthority--> E:DuPhongNganSachNhaNuoc
- constraint: Định kỳ báo cáo Chính phủ → UBTVQH và báo cáo Quốc hội kỳ họp gần nhất; BTC chủ trì tổng hợp trình; báo cáo quý chậm nhất ngày 20 sau hết quý.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-10|Luật 89 Điều 10]] k4.a; NĐ 73 Điều 25 k2.a, k4
- diễn giải: Chỉ Thủ tướng được quyết định dùng dự phòng NSTW.

### R:UBND-quyetDinhSuDung-DuPhongCapMinh
- triple: E:UBNDCacCap --hasAuthority--> E:DuPhongNganSachNhaNuoc
- constraint: Định kỳ báo cáo Thường trực HĐND và HĐND cùng cấp kỳ họp gần nhất; cơ quan tài chính trình UBND.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-10|Luật 89 Điều 10]] k4.b; NĐ 73 Điều 25 k2.b, k4
- diễn giải: UBND cấp nào quyết định dự phòng cấp đó.

## 5. Quyết toán

### R:HDNDXa-pheChuanQuyetToan-truoc31Thang3
- triple: E:HDNDXa --pheChuan--> E:QuyetToan
- constraint: Trước 31/3 năm sau; gửi UBND cấp tỉnh chậm nhất 05 ngày làm việc sau phê chuẩn; nếu chưa chuẩn thì trình lại chậm nhất 10 ngày làm việc.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-71|Luật 89 Điều 71]] k3–k4; NĐ 73 Điều 32 k5
- swrl: HDNDXa(?x) ∧ BaoCaoQT(?y) ∧ cuaCap(?y,?x) → pheChuanTruoc(?x,?y,"31-03-N+1")
- diễn giải: QT xã phải được HĐND xã phê chuẩn trong quý I năm sau.

### R:UBNDTinh-guiQT-truoc01Thang5
- triple: E:UBNDTinh --reportsTo--> E:BoTaiChinh
- constraint: UBND cấp tỉnh gửi BTC và KTNN trước 01/5; QT đã HĐND tỉnh phê chuẩn gửi lại trước 05/7.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-71|Luật 89 Điều 71]] k3; [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-72|Điều 72]] k2; NĐ 73 Điều 32 k6–k7
- diễn giải: Tỉnh gửi hồ sơ QT cho BTC/KTNN hai mốc 01/5 và 05/7.

### R:HDNDTinh-pheChuanQT-truoc01Thang7
- triple: E:HDNDTinh --pheChuan--> E:QuyetToan
- constraint: Trước ngày 01/7 năm sau; KTNN kiểm toán báo cáo QT địa phương **trước** khi gửi HĐND tỉnh phê chuẩn.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-71|Luật 89 Điều 71]] k3; [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-73|Điều 73]] k2
- diễn giải: Không phê chuẩn QT tỉnh khi chưa có kiểm toán KTNN.

### R:DonViDuToanCapTren-xetDuyetQT-DonViSuDungNS
- triple: E:DonViDuToanNganSach --xetDuyetQuyetToan--> E:DonViSuDungNganSach
- constraint: Khớp sổ kế toán với xác nhận KBNN; đủ điều kiện chi Điều 12; được yêu cầu xuất toán chi sai.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-69|Luật 89 Điều 69]]; NĐ 73 Điều 32 k3
- diễn giải: Xét duyệt QT là trách nhiệm cấp trên trực tiếp, không phải của HĐND.

### R:KTNN-kiemToanTruoc-PheChuanQT
- triple: E:KiemToanNhaNuoc --kiemToanTruoc--> E:QuyetToan
- constraint: QT NSNN: kiểm toán trước khi trình Quốc hội; QT địa phương: kiểm toán trước khi gửi HĐND cấp tỉnh.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-23|Luật 89 Điều 23]] k2; [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-73|Điều 73]]
- diễn giải: Phê chuẩn QT cấp quốc gia và cấp tỉnh bắt buộc có kiểm toán KTNN đi trước.

### R:QuocHoi-pheChuanQT-chamNhat12Thang
- triple: E:QuocHoi --pheChuan--> E:QuyetToan
- constraint: Chậm nhất 12 tháng sau khi kết thúc năm ngân sách; Chính phủ báo cáo UBTVQH chậm nhất 20/9 năm sau.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-19|Luật 89 Điều 19]] k9; [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-72|Điều 72]] k4–k5
- diễn giải: Quốc hội phê chuẩn QT NSNN không muộn hơn hết năm sau.

### R:KetDuTWTinh-xuLy-QuyDuTruVaThuNamSau
- triple: E:KetDuNganSachTWVaCapTinh --xuLyBang--> E:QuyDuTruTaiChinh
- constraint: Ưu tiên trả nợ gốc và lãi chưa bố trí đủ; số còn lại 50% vào quỹ DT tài chính cùng cấp, 50% thu NS năm sau; nếu quỹ đã đủ 25% DT chi năm thì toàn bộ vào thu năm sau. Thực hiện sau khi Quốc hội/HĐND phê chuẩn QT.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-74|Luật 89 Điều 74]] k1; NĐ 73 Điều 33 k2.a
- diễn giải: Kết dư TW/tỉnh: trả nợ trước, rồi chia quỹ DT và thu năm sau.

### R:KetDuXa-hachToan-ThuNamSau
- triple: E:KetDuNganSachCapXa --hachToanVao--> E:NganSachCapXa
- constraint: Toàn bộ kết dư xã hạch toán vào thu ngân sách năm sau (không trích quỹ DT tài chính).
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-74|Luật 89 Điều 74]] k1; NĐ 73 Điều 33 k2.b
- diễn giải: Xã không có quỹ dự trữ tài chính riêng từ kết dư.

### R:ChiSauQT-khongDieuChinhQTDaPheChuan
- triple: E:QuyetToan --xuLySaiPhamVaoNamXuLy--> E:NamNganSach
- constraint: Thu hồi/chi hoàn trả hạch toán vào năm xử lý; không điều chỉnh QT đã Quốc hội/HĐND phê chuẩn.
- source: [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-75|Luật 89 Điều 75]]; Điều 67 k8; NĐ 73 Điều 32 k8
- diễn giải: Phát hiện sai sau phê chuẩn thì xử lý trên NS năm hiện hành.

## 6. Tài sản công

## Liên kết

- [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/Thucthe|Thucthe]] · [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/Quanhe|Quanhe]] · [[Vanbanquydinh/TW/Luat/2025/89-2025-QH15/quytrinh|quytrinh]]
- TBox: [[TAILIEU/ontology|ontology]] · Hub VB: [[Vanbanquydinh/index|Vanbanquydinh]]
