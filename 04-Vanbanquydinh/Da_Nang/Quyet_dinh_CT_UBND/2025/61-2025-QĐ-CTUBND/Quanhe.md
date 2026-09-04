---
okf_version: "0.2"
type: research
title: "Quan hệ / quy tắc — 61/2025/QĐ-CTUBND"
so_hieu: "61/2025/QĐ-CTUBND"
updated: 2026-09-02
tags: [ontology, Vanbanquydinh, Da_Nang]
---

# Quanhe — 61/2025/QĐ-CTUBND

Phân cấp TSC Đà Nẵng. TBox: [[02-TAILIEU/ontology|ontology]]. Cùng thư mục: [[04-Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/Thucthe|Thucthe]] · [[04-Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/Quanhe|Quanhe]] · [[04-Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/quytrinh|quytrinh]] · [[04-Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/index|61/2025/QĐ-CTUBND]] · [[04-Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/toan-van|toàn văn]].

### R:ChuTichUBNDTP-hasAuthority-GiaoHienVatTruSo
- triple: E:ChuTichUBNDThanhPhoDaNang --hasAuthority--> E:TruSoLamViec
- constraint: Quyết định giao TSC bằng hiện vật là trụ sở cho cơ quan, tổ chức; cơ sở SN cho đơn vị, không phân biệt cấp.
- source: [[04-Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/DieudiemDanchieu/Dieu-04|QĐ 61 Điều 4]] k1.a
- diễn giải: Trụ sở/cơ sở SN — thẩm quyền Chủ tịch TP, không phải thủ trưởng đơn vị.

### R:ChuTichUBNDXa-hasAuthority-KhaiThacTSC
- triple: E:ChuTichUBNDXa --hasAuthority--> E:KhaiThacTSC
- constraint: Không gồm SNCL tự bảo đảm chi TX và chi ĐT, SNCL tự bảo đảm chi TX.
- source: [[04-Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/DieudiemDanchieu/Dieu-07|QĐ 61 Điều 7]]
- diễn giải: Phân cấp khai thác TSC cấp xã tại Đà Nẵng.

### R:NhaDat-khac-MayMoc-phanCapTSC
- triple: E:ChuTichUBNDThanhPhoDaNang --hasAuthority--> E:TruSoLamViec
- constraint: Trụ sở / cơ sở SN / xe ô tô (Điều 4 k1) ≠ TSC khác (máy móc, trang thiết bị — Điều 4 k2). Trụ sở: Chủ tịch TP giao hiện vật, không phân biệt cấp. Xe: Chủ tịch từng cấp. TSC khác: Sở TC / CQCM TP / Chủ tịch xã theo phạm vi quản lý. Không lấy thẩm quyền nhà đất áp cho máy móc.
- source: [[04-Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/DieudiemDanchieu/Dieu-04|QĐ 61 Điều 4]] k1–k2; [[04-Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/DieudiemDanchieu/Dieu-03|Điều 3]]
- diễn giải: Buổi 3 — nhà đất ≠ máy móc. Mở đúng khoản trước khi trình ký.

### R:GiaoTSCKhac-hasAuthority-CQCM-ChuTichXa
- triple: E:ChuTichUBNDXa --hasAuthority--> E:TaiSanCong
- constraint: TSC không phải trụ sở / cơ sở SN / xe: Chủ tịch xã giao cho cơ quan, tổ chức, đơn vị thuộc phạm vi quản lý. Sở TC giao cho CQCM TP, SNCL trực thuộc UBND TP và UBND xã.
- source: [[04-Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/DieudiemDanchieu/Dieu-04|QĐ 61 Điều 4]] k2
- diễn giải: Máy móc, trang thiết bị cấp xã — cửa Chủ tịch xã, không chờ Chủ tịch TP.

### R:SoTaiChinh-thamMuu-UBNDTinh
- triple: E:SoTaiChinh --hasDuty--> E:NganSachNhaNuoc
- constraint: Tham mưu QLNN về NSNN, ĐTC, đấu thầu, TSC cho UBND cấp tỉnh.
- source: TT 57/2025 Điều 1.1; QĐ 61 Điều 18 k3
- diễn giải: Sở Tài chính là cửa kỹ thuật của UBND tỉnh/TP.

## Liên kết

- [[04-Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/Thucthe|Thucthe]] · [[04-Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/Quanhe|Quanhe]] · [[04-Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/quytrinh|quytrinh]]
- TBox: [[02-TAILIEU/ontology|ontology]] · Hub VB: [[04-Vanbanquydinh/index|Vanbanquydinh]]
