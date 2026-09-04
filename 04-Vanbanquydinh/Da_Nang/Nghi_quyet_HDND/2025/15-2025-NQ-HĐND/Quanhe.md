---
okf_version: "0.2"
type: research
title: "Quan hệ / quy tắc — 15/2025/NQ-HĐND"
so_hieu: "15/2025/NQ-HĐND"
updated: 2026-09-02
tags: [ontology, Vanbanquydinh, Da_Nang]
---

# Quanhe — 15/2025/NQ-HĐND

Phân cấp NS TP–xã 2026. TBox: [[02-TAILIEU/ontology|ontology]]. Cùng thư mục: [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2025/15-2025-NQ-HĐND/Thucthe|Thucthe]] · [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2025/15-2025-NQ-HĐND/Quanhe|Quanhe]] · [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2025/15-2025-NQ-HĐND/quytrinh|quytrinh]] · [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2025/15-2025-NQ-HĐND/index|15/2025/NQ-HĐND]] · [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2025/15-2025-NQ-HĐND/toan-van|toàn văn]].

### R:NS-TP-phanCap-NS-xa
- triple: E:NganSachThanhPho-DaNang --phanCapThuChi--> E:NganSachCapXa
- constraint: Phân cấp nguồn thu, nhiệm vụ chi, tỷ lệ % phân chia; định mức phân bổ chi TX cho UBND xã/phường/đặc khu.
- source: [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2025/15-2025-NQ-HĐND/DieudiemDanchieu/Dieu-06|NQ 15/2025 Điều 6]]; [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2025/15-2025-NQ-HĐND/DieudiemDanchieu/Dieu-07|Điều 7]]; [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2025/15-2025-NQ-HĐND/DieudiemDanchieu/Dieu-11|Điều 11]]
- diễn giải: Áp dụng Luật 89 Điều 9 k3 tại Đà Nẵng năm 2026.

### R:NganSachCapXa-chiKhi-TrongDieu6NQ15
- triple: E:NganSachCapXa --baoDam--> E:NhiemVuChiNSCapXa-DaNang
- constraint: Việc không có trong Điều 6 → không lập DT / không ký chi từ NS xã. Khoản thuộc nhiệm vụ TP mà xã «ứng» = ngoài phân cấp.
- source: [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2025/15-2025-NQ-HĐND/DieudiemDanchieu/Dieu-06|NQ 15/2025 Điều 6]]; [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-09|Luật 89 Điều 9]] k5; [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-41|Điều 41]]
- diễn giải: «Nhiệm vụ nào — ngân sách đó».

### R:ThuXa-baNhom
- triple: E:NganSachCapXa --tongHopThu--> E:ThuHuong100CapXa-DaNang
- constraint: Mọi khoản thu xã thuộc một trong ba nhóm: (1) hưởng 100% Điều 4 k1; (2) phân chia theo % Điều 7 — mở đúng dòng địa bàn, không nhớ miệng; (3) bổ sung cân đối / có mục tiêu từ NS TP (Điều 4 k3). Xã không tự đặt khoản ngoài danh mục.
- source: [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2025/15-2025-NQ-HĐND/toan-van|NQ 15 Điều 4]]; [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2025/15-2025-NQ-HĐND/DieudiemDanchieu/Dieu-07|Điều 7]]; [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/DieudiemDanchieu/Dieu-38|Luật 89 Điều 38]]
- diễn giải: Trước khi lập DT thu: hỏi 100% / phân chia / bổ sung, rồi mở dòng phường–xã trên Điều 7.

### R:ThuongVuotThu-khongQua20-guiTruoc31Thang01
- triple: E:UBNDXa --reportsTo--> E:SoTaiChinh
- constraint: TP không hụt thu so với DT; trích không quá 20% số tăng các khoản Điều 7 k1 điểm a, b, c, e (sau khi trích CCTL); không vượt số tăng so với thực hiện năm trước. UBND xã gửi STC báo cáo có xác nhận KBNN trước 31/01 năm sau. Dùng cho hạ tầng / nhiệm vụ quan trọng theo phân cấp — không chi TX tự do.
- source: [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2025/15-2025-NQ-HĐND/DieudiemDanchieu/Dieu-07|NQ 15/2025 Điều 7]] k3
- diễn giải: Thưởng vượt thu là nguồn có điều kiện và hạn gửi, không phải «tăng thu được chi».

### R:DinhMucDieu11-laTongChiTX-khongTranTungViec
- triple: E:HDNDTinh --allocatesTo--> E:DinhMucPhanBoChiTX-Xa
- constraint: Định mức Điều 11 xác định tổng chi TX (có chi tiết GDĐT, KHCN). UBND xã trình HĐND xã phân bổ theo lĩnh vực cho phù hợp thực tế. Không coi từng dòng định mức là hạn mức chi từng việc.
- source: [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2025/15-2025-NQ-HĐND/DieudiemDanchieu/Dieu-11|NQ 15/2025 Điều 11]]
- diễn giải: Tra số trên file Điều — ontology không chép bảng.

## Liên kết

- [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2025/15-2025-NQ-HĐND/Thucthe|Thucthe]] · [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2025/15-2025-NQ-HĐND/Quanhe|Quanhe]] · [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2025/15-2025-NQ-HĐND/quytrinh|quytrinh]]
- TBox: [[02-TAILIEU/ontology|ontology]] · Hub VB: [[04-Vanbanquydinh/index|Vanbanquydinh]]
