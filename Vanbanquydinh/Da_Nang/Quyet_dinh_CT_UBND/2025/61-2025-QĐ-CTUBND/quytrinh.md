---
okf_version: "0.2"
type: research
title: "Quy trình — 61/2025/QĐ-CTUBND"
so_hieu: "61/2025/QĐ-CTUBND"
updated: 2026-09-02
tags: [ontology, Vanbanquydinh, Da_Nang]
---

# quytrinh — 61/2025/QĐ-CTUBND

Phân cấp TSC Đà Nẵng. TBox: [[TAILIEU/ontology|ontology]]. Cùng thư mục: [[Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/Thucthe|Thucthe]] · [[Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/Quanhe|Quanhe]] · [[Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/quytrinh|quytrinh]] · [[Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/index|61/2025/QĐ-CTUBND]] · [[Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/toan-van|toàn văn]].

## P:thanh-ly-tsc

- rdf:type: QuyTrinh
- rdfs:label: Thanh lý tài sản công tại cơ quan nhà nước
- governs: E:ThanhLyTSC
- hasAgent: E:ChuTichUBNDThanhPhoDaNang, E:ChuTichUBNDXa, E:SoTaiChinh, E:NguoiDungDauCoQuanToChucDonVi
- source: [[Vanbanquydinh/TW/Luat/2017/15-2017-QH14/DieudiemDanchieu/Dieu-45|Luật 15 Điều 45]]; [[Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/DieudiemDanchieu/Dieu-13|QĐ 61 Điều 13]]

1. **Điều kiện.** Hết hạn sử dụng; hư hỏng không sửa được/không hiệu quả; hoặc phải phá dỡ theo quyết định CQNN.
2. **Thẩm quyền Đà Nẵng.** Chủ tịch UBND các cấp: TS gắn đất trụ sở; Sở TC: xe khối TP/xã; CQCM / Chủ tịch xã / SNCL theo ngưỡng 500 triệu nguyên giá / 50 triệu đánh giá lại (QĐ 61 Đ.13).
3. **Hình thức.** Phá dỡ, hủy bỏ (vật tư còn dùng được thì điều chuyển, bán hoặc tiếp tục sử dụng); hoặc bán theo Điều 43.
4. **Tiền thu.** Sau chi phí → nộp NSNN theo Luật 15 (Luật 90 sửa Điều 48).

## P:phan-cap-tham-quyen-tsc-da-nang

- rdf:type: QuyTrinh
- rdfs:label: Phân cấp thẩm quyền quyết định TSC tại Đà Nẵng
- governs: E:TaiSanCong
- hasAgent: E:ChuTichUBNDThanhPhoDaNang, E:ChuTichUBNDXa, E:SoTaiChinh, E:CoQuanChuyenMonUBND, E:DonViSNCL
- source: [[Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/DieudiemDanchieu/index|QĐ 61 Điều 3–18]]
- constraint: Sáu nguyên tắc Đ.3 (cùng Luật 15 Đ.6); loại trừ SNCL tự bảo đảm chi TX và chi ĐT ở một số Điều

| Việc | hasAuthority chính | Điều |
|------|-------------------|------|
| Giao hiện vật trụ sở, cơ sở SN | Chủ tịch UBND TP | 4 |
| Khoán nhà công vụ / máy móc | CQCM TP, Chủ tịch xã, SNCL | 5–6 |
| Khai thác | CQCM TP, Chủ tịch xã, SNCL | 7 |
| Đề án KD/cho thuê/LDLK | CQCM TP, Chủ tịch xã, SNCL | 8 |
| Thu hồi trụ sở, cơ sở SN | Chủ tịch TP | 9 |
| Điều chuyển trụ sở, cơ sở SN | Chủ tịch TP | 10 |
| Bán TSCĐ | CQ thu hồi Đ.9; CQCM, Chủ tịch xã; SNCL ngưỡng 250/50 tr | 11 |
| Thanh lý | Chủ tịch các cấp (TS gắn đất trụ sở); Sở TC (xe); CQCM/xã/SNCL ngưỡng 500/50 tr | 13 |
| Tiêu hủy | Chủ tịch các cấp (TS gắn đất); CQCM, xã, SNCL (TSC khác) | 14 |
| Mất/hủy hoại ≥ 02 tỷ | Chủ tịch UBND các cấp | 15 |
| PPP SNCL | Chủ tịch UBND các cấp | 16 |
| PA xử lý TS dự án | Chủ tịch TP / Chủ tịch xã | 17 |

Tổ chức thực hiện theo trình tự Luật TSC, NĐ hướng dẫn, Luật Đấu thầu (Đ.18 k2.c). Trách nhiệm Sở TC, CQCM cấp xã: Đ.18.

## P:khai-thac-tsc

- rdf:type: QuyTrinh
- rdfs:label: Khai thác tài sản công tại CQNN và SNCL
- governs: E:KhaiThacTSC
- hasAgent: E:ChuTichUBNDTinh, E:ChuTichUBNDXa, E:NguoiDungDauCoQuanToChucDonVi, E:KhoBacNhaNuoc
- source: [[Vanbanquydinh/TW/Nghi_dinh/2025/186-2025-NĐ-CP/DieudiemDanchieu/Dieu-14|NĐ 186 Điều 14]]; [[Vanbanquydinh/TW/Nghi_dinh/2025/186-2025-NĐ-CP/DieudiemDanchieu/Dieu-50|Điều 50]]; QĐ 61 Điều 7
- hasDeadline: CQNN — 30 ngày kể từ nhận hồ sơ; SNCL — 20 ngày kể từ nhận đầy đủ hồ sơ

**A. CQNN (Đ.14)**

1. Lập hồ sơ: sự cần thiết; danh mục TS (tên, số lượng, diện tích, nguyên giá, giá trị còn lại); hình thức; thời hạn; dự kiến số tiền.
2. Báo cáo CQQL cấp trên (nếu có) → người có thẩm quyền (Bộ trưởng / Chủ tịch UBND cấp tỉnh / Chánh VP HĐND cấp tỉnh). Đà Nẵng: phân cấp QĐ 61 Đ.7.
3. Trong 30 ngày: quyết định hoặc văn bản hồi đáp.
4. Tổ chức khai thác: tự khai thác / đấu thầu / đấu giá / thỏa thuận trực tiếp (ATM, VT) tùy nhóm TS.
5. Tiền thu: trừ chi phí và nghĩa vụ TC; **50%** giữ lại chi TX; **50%** nộp NS tại KBNN.

**B. SNCL (Đ.50)** — cùng khung, thời hạn 20 ngày; phần còn lại là nguồn thu của đơn vị theo cơ chế TC SNCL (không chia 50/50).

## Liên kết

- [[Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/Thucthe|Thucthe]] · [[Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/Quanhe|Quanhe]] · [[Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/quytrinh|quytrinh]]
- TBox: [[TAILIEU/ontology|ontology]] · Hub VB: [[Vanbanquydinh/index|Vanbanquydinh]]
