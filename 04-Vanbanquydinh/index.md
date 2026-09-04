---
okf_version: "0.2"
type: index
title: "Văn bản quy định dẫn chiếu (copy INF + RAW)"
updated: 2026-09-04
tags: [Vanbanquydinh, Da_Nang, NSNN, TSC, chinh-quyen-2-cap]
---

# Văn bản quy định dẫn chiếu

## Ba nhánh tra cứu chính

| Nhánh | Dùng khi cần | Số hồ sơ hiện tại |
|---|---|---:|
| [[04-Vanbanquydinh/NSNN/index|NSNN]] | Dự toán, chấp hành, kế toán, quyết toán, kiểm toán, nguồn và nhiệm vụ chi | 42 |
| [[04-Vanbanquydinh/TSC/index|TSC]] | Đầu tư, mua sắm, quản lý, sử dụng, hao mòn và xử lý tài sản công | 22 |
| [[04-Vanbanquydinh/Chinh_quyen_2_cap/index|Chính quyền 2 cấp]] | Tổ chức bộ máy, địa giới, phân định/phân cấp thẩm quyền và chuyển tiếp | 25 |

Ba chỉ mục được sinh từ [[04-Vanbanquydinh/phan-nhanh.json|manifest phân nhánh]] bằng `scripts/rebuild_legal_branches.py`. Bản gốc của 71 hồ sơ vẫn ở nguyên thư mục số hiệu; một hồ sơ có thể xuất hiện ở nhiều nhánh.

## Đối tượng và mục đích

Công chức xã / đơn vị dự toán TP cần *một Điều, một số hiệu* — không đọc hết catalog. Trang này trả lời: *mở nhóm nào trên bản đồ căn cứ, rồi vào thư mục số hiệu*.

Phạm vi hiện có là **71 hồ sơ = 64 văn bản trong danh mục khóa học + 4 văn bản Wisdom bổ sung + 3 văn bản tổ chức chính quyền 2 cấp** (202/2025/QH15, 1659/NQ-UBTVQH15, 19/2025/QĐ-TTg). Metadata từ INF; toàn văn copy RAW vào `toan-van`. Không lấy văn bản cùng số của tỉnh khác. Văn bản có Điều được HV/CN nêu: thư mục con `DieudiemDanchieu` (một file / Điều; `index.md` liệt kê hết).

## Khi nào mở trang này

- Cần luật khung (NSNN, CQĐP, KTNN, ĐT công, đấu thầu, TSC, kế toán).
- Cần nghị quyết / quyết định Đà Nẵng (phân cấp, CCTL, lịch DT, TSC).
- Cần đúng số hiệu từ danh mục HV/CN — không đoán path.
- Trước khi trích: kiểm tra `tinh_trang_hieu_luc` trên trang văn bản.

**Cách dùng bản đồ:** chọn nhóm (Luật khung / Trục Đà Nẵng / Cơ quan) → mở số hiệu → `toan-van` hoặc `DieudiemDanchieu`. Không đọc hết catalog trước khi làm việc. Ngoài INF (nghị quyết Đảng / số hiệu thiếu năm): không thay bằng văn bản cùng số tỉnh khác.

## Bản đồ căn cứ

### Luật khung (TW)

- NSNN (từ 01/01/2026) — [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/index|89/2025/QH15 — Luật NSNN]] · VBHN [[04-Vanbanquydinh/TW/Van_ban_hop_nhat/2026/89-VBHN-VPQH/index|89/VBHN-VPQH — văn bản hợp nhất Luật 89]]
- Tổ chức CQĐP — [[04-Vanbanquydinh/TW/Luat/2025/72-2025-QH15/index|72/2025/QH15 — tổ chức chính quyền địa phương]]
- NSNN (luật trước) — [[04-Vanbanquydinh/TW/Luat/2015/83-2015-QH13/index|83/2015/QH13 — Luật NSNN (trước)]]
- Kiểm toán nhà nước — [[04-Vanbanquydinh/TW/Luat/2015/81-2015-QH13/index|81/2015/QH13 — Luật KTNN]]
- Sửa Luật KTNN — [[04-Vanbanquydinh/TW/Luat/2019/55-2019-QH14/index|55/2019/QH14 — sửa Luật KTNN]]
- Đầu tư công — [[04-Vanbanquydinh/TW/Luat/2024/58-2024-QH15/index|58/2024/QH15 — Luật Đầu tư công]]
- Đấu thầu — [[04-Vanbanquydinh/TW/Luat/2023/22-2023-QH15/index|22/2023/QH15 — Luật Đấu thầu]]
- Xây dựng (từ 01/7/2026) — [[04-Vanbanquydinh/TW/Luat/2025/135-2025-QH15/index|135/2025/QH15 — Luật Xây dựng]]
- Tài sản công — [[04-Vanbanquydinh/TW/Luat/2017/15-2017-QH14/index|15/2017/QH14 — Luật TSC]]
- Kế toán — [[04-Vanbanquydinh/TW/Luat/2015/88-2015-QH13/index|88/2015/QH13 — Luật Kế toán]]
- Sửa ĐT / ĐT công / … — [[04-Vanbanquydinh/TW/Luat/2025/90-2025-QH15/index|90/2025/QH15 — luật sửa đổi]]
- Chi tiết Luật NSNN — [[04-Vanbanquydinh/TW/Nghi_dinh/2026/73-2026-NĐ-CP/index|73/2026/NĐ-CP — nghị định chi tiết NSNN]]
- TT KTNN — [[04-Vanbanquydinh/TW/Thong_tu/2026/01-2026-TT-KTNN/index|01/2026/TT-KTNN — Thông tư KTNN]]

### Trục Đà Nẵng (từ TAILIEU)

- Phân cấp thu–chi — [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2025/15-2025-NQ-HĐND/index|15/2025/NQ-HĐND — phân cấp thu–chi]]
- Chi thu nhập tăng thêm / CCTL — [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2025/52-2025-NQ-HĐND/index|52/2025/NQ-HĐND — CCTL / thu nhập tăng thêm]]
- Phân bổ vốn ĐT công 2026–2030 — [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2026/79-2026-NQ-HĐND/index|79/2026/NQ-HĐND — vốn đầu tư công]]
- Lịch lập DT / quyết toán — [[04-Vanbanquydinh/Da_Nang/Quyet_dinh_UBND/2026/71-2026-QĐ-UBND/index|71/2026/QĐ-UBND — lịch DT / quyết toán]]
- Phân cấp TSC (Chủ tịch UBND) — [[04-Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/index|61/2025/QĐ-CTUBND — phân cấp TSC]]
- Định mức máy móc TP — [[04-Vanbanquydinh/Da_Nang/Quyet_dinh_UBND/2026/14-2026-QĐ-UBND/index|14/2026/QĐ-UBND — định mức máy móc]]
- HĐLĐ GDĐT 2025–2026 — [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2025/14-NQ-HĐND/index|14/NQ-HĐND — HĐLĐ GDĐT]] (12/8/2025; không phải `14/2025/NQ-HĐND`)

### Tổ chức bộ máy và địa giới Đà Nẵng (2 cấp)

- Sáp nhập tỉnh Quảng Nam vào Đà Nẵng — [[04-Vanbanquydinh/TW/Nghi_quyet_QH/2025/202-2025-QH15/index|202/2025/QH15 — sáp nhập tỉnh]]
- Danh mục 94 ĐVHC cấp xã TP Đà Nẵng — [[04-Vanbanquydinh/TW/Quyet_dinh_TTg/2025/19-2025-QĐ-TTg/index|19/2025/QĐ-TTg — danh mục ĐVHC]]
- Sắp xếp ĐVHC cấp xã TP Đà Nẵng năm 2025 — [[04-Vanbanquydinh/TW/Nghi_quyet_UBTVQH/2025/1659-NQ-UBTVQH15/index|1659/NQ-UBTVQH15 — sắp xếp ĐVHC cấp xã]]

CCTL / KHCN: [[04-Vanbanquydinh/TW/Nghi_quyet_TW/2018/27-NQ-TW/index|27-NQ/TW — CCTL]] · [[04-Vanbanquydinh/TW/Nghi_quyet_TW/2024/57-NQ-TW/index|57-NQ/TW — KHCN / ĐMST]].

### Cơ quan

- KTNN — [[03-TIMHIEU/co-quan/index#KTNN|KTNN — Kiểm toán Nhà nước]] (`TW.Chinh_phu.Kiem_Toan_Nha_Nuoc`)
- HĐND TP — [[03-TIMHIEU/co-quan/index#HĐND|HĐND TP Đà Nẵng]] (`Tinh.Da_Nang.HDND`)
- UBND TP — [[03-TIMHIEU/co-quan/index#UBND|UBND TP Đà Nẵng]] (`Tinh.Da_Nang.UBND`)
- Sở Tài chính — [[03-TIMHIEU/co-quan/index#Sở Tài chính|Sở Tài chính TP]] (`Tinh.Da_Nang.So_Tai_Chinh`)

Xã/phường: `Tinh.Da_Nang.Xa_*` — [[03-TIMHIEU/hang-ngay/chinh-quyen-2-cap-da-nang/index|Chính quyền 2 cấp Đà Nẵng]]. Cây cơ quan: [[03-TIMHIEU/co-quan/index#Đà Nẵng|Cây cơ quan Đà Nẵng]].

## Vận dụng

1. **Làm đúng** — mở đúng số hiệu trên bản đồ; không lấy văn bản cùng số của tỉnh khác.
2. **Tự kiểm** — đọc `tinh_trang_hieu_luc` + Điều trong `DieudiemDanchieu` trước khi trích vào tờ trình.
3. **Giải trình** — đưa path thư mục số hiệu + Điều; đối chiếu heading TAILIEU (buổi / CĐ) đã dẫn số đó.

Gốc gói: [[hub-goi|Hub gói — lối vào nhu cầu]].

## Tài liệu chính

- [[02-TAILIEU/Cẩm nang quản lý ngân sách xã - 23.8.2026|Cẩm nang quản lý ngân sách xã]] — trình tự buổi, phân cấp–chi–quyết toán xã.
- [[02-TAILIEU/Tài liệu in cho học viên|Tài liệu in cho học viên]] — góc KTNN, 05 chuyên đề, sổ tay tự kiểm.

Số hiệu dưới đây gồm catalog 64 HV/CN + 4 số Wisdom; ba hồ sơ tổ chức chính quyền 2 cấp được đặt ở bản đồ và [[04-Vanbanquydinh/Chinh_quyen_2_cap/index|nhánh riêng]]. Tổng phạm vi: 71 hồ sơ. Danh mục nguồn: [[02-TAILIEU/danh-muc-van-ban-dan-chieu|Danh mục văn bản dẫn chiếu]].

## Luật và văn bản hợp nhất

- [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/index|89/2025/QH15 — Luật NSNN]] — INF+RAW
- [[04-Vanbanquydinh/TW/Van_ban_hop_nhat/2026/89-VBHN-VPQH/index|89/VBHN-VPQH]] — INF+RAW
- [[04-Vanbanquydinh/TW/Luat/2025/72-2025-QH15/index|72/2025/QH15]] — INF+RAW
- [[04-Vanbanquydinh/TW/Luat/2017/15-2017-QH14/index|15/2017/QH14 — Luật TSC]] — INF+RAW
- [[04-Vanbanquydinh/TW/Luat/2024/58-2024-QH15/index|58/2024/QH15]] — INF+RAW
- [[04-Vanbanquydinh/TW/Luat/2025/145-2025-QH15/index|145/2025/QH15]] — INF+RAW
- [[04-Vanbanquydinh/TW/Luat/2020/64-2020-QH14/index|64/2020/QH14]] — INF+RAW
- [[04-Vanbanquydinh/TW/Luat/2022/07-2022-QH15/index|07/2022/QH15]] — INF+RAW
- [[04-Vanbanquydinh/TW/Luat/2023/24-2023-QH15/index|24/2023/QH15]] — INF+RAW
- [[04-Vanbanquydinh/TW/Luat/2024/31-2024-QH15/index|31/2024/QH15]] — INF+RAW
- [[04-Vanbanquydinh/TW/Luat/2024/43-2024-QH15/index|43/2024/QH15]] — INF+RAW
- [[04-Vanbanquydinh/TW/Luat/2024/56-2024-QH15/index|56/2024/QH15]] — INF+RAW
- [[04-Vanbanquydinh/TW/Luat/2025/90-2025-QH15/index|90/2025/QH15]] — INF+RAW
- [[04-Vanbanquydinh/TW/Luat/2023/22-2023-QH15/index|22/2023/QH15]] — INF+RAW
- [[04-Vanbanquydinh/TW/Luat/2015/88-2015-QH13/index|88/2015/QH13]] — INF+RAW
- [[04-Vanbanquydinh/TW/Luat/2025/135-2025-QH15/index|135/2025/QH15]] — INF+RAW
- [[04-Vanbanquydinh/TW/Luat/2015/83-2015-QH13/index|83/2015/QH13 — Luật NSNN (trước)]] — INF+RAW (Wisdom; ngoài 64 HV/CN)
- [[04-Vanbanquydinh/TW/Luat/2015/81-2015-QH13/index|81/2015/QH13 — Luật KTNN]] — INF+RAW (Wisdom; ngoài 64 HV/CN)
- [[04-Vanbanquydinh/TW/Luat/2019/55-2019-QH14/index|55/2019/QH14 — sửa Luật KTNN]] — INF+RAW (Wisdom; ngoài 64 HV/CN)

## Nghị quyết Quốc hội / Trung ương

- [[04-Vanbanquydinh/TW/Nghi_quyet_QH/2025/245-2025-QH15/index|245/2025/QH15]] — INF+RAW
- [[04-Vanbanquydinh/TW/Nghi_quyet_TW/2018/27-NQ-TW/index|27-NQ/TW]] — ngoài INF (toàn văn nguồn công khai)
- [[04-Vanbanquydinh/TW/Nghi_quyet_TW/2024/57-NQ-TW/index|57-NQ/TW]] — ngoài INF (toàn văn nguồn công khai)

## Nghị định

- [[04-Vanbanquydinh/TW/Nghi_dinh/2020/11-2020-NĐ-CP/index|11/2020/NĐ-CP]] — INF+RAW
- [[04-Vanbanquydinh/TW/Nghi_dinh/2021/60-2021-NĐ-CP/index|60/2021/NĐ-CP]] — INF+RAW
- [[04-Vanbanquydinh/TW/Nghi_dinh/2022/111-2022-NĐ-CP/index|111/2022/NĐ-CP]] — INF+RAW
- [[04-Vanbanquydinh/TW/Nghi_dinh/2024/73-2024-NĐ-CP/index|73/2024/NĐ-CP]] — INF+RAW
- [[04-Vanbanquydinh/TW/Nghi_dinh/2025/111-2025-NĐ-CP/index|111/2025/NĐ-CP]] — INF+RAW
- [[04-Vanbanquydinh/TW/Nghi_dinh/2025/125-2025-NĐ-CP/index|125/2025/NĐ-CP]] — INF+RAW
- [[04-Vanbanquydinh/TW/Nghi_dinh/2025/127-2025-NĐ-CP/index|127/2025/NĐ-CP]] — INF+RAW
- [[04-Vanbanquydinh/TW/Nghi_dinh/2025/150-2025-NĐ-CP/index|150/2025/NĐ-CP]] — INF+RAW
- [[04-Vanbanquydinh/TW/Nghi_dinh/2025/152-2025-NĐ-CP/index|152/2025/NĐ-CP]] — INF+RAW
- [[04-Vanbanquydinh/TW/Nghi_dinh/2025/173-2025-NĐ-CP/index|173/2025/NĐ-CP]] — INF+RAW
- [[04-Vanbanquydinh/TW/Nghi_dinh/2025/186-2025-NĐ-CP/index|186/2025/NĐ-CP]] — INF+RAW
- [[04-Vanbanquydinh/TW/Nghi_dinh/2025/214-2025-NĐ-CP/index|214/2025/NĐ-CP]] — INF+RAW
- [[04-Vanbanquydinh/TW/Nghi_dinh/2025/254-2025-NĐ-CP/index|254/2025/NĐ-CP]] — INF+RAW
- [[04-Vanbanquydinh/TW/Nghi_dinh/2025/286-2025-NĐ-CP/index|286/2025/NĐ-CP]] — INF+RAW
- [[04-Vanbanquydinh/TW/Nghi_dinh/2025/347-2025-NĐ-CP/index|347/2025/NĐ-CP]] — INF+RAW
- [[04-Vanbanquydinh/TW/Nghi_dinh/2026/73-2026-NĐ-CP/index|73/2026/NĐ-CP]] — INF+RAW
- [[04-Vanbanquydinh/TW/Nghi_dinh/2026/161-2026-NĐ-CP/index|161/2026/NĐ-CP]] — INF+RAW

## Thông tư

- [[04-Vanbanquydinh/TW/Thong_tu/2015/185-2015-TT-BTC/index|185/2015/TT-BTC]] — INF+RAW
- [[04-Vanbanquydinh/TW/Thong_tu/2016/324-2016-TT-BTC/index|324/2016/TT-BTC]] — INF+RAW
- [[04-Vanbanquydinh/TW/Thong_tu/2017/77-2017-TT-BTC/index|77/2017/TT-BTC]] — INF+RAW
- [[04-Vanbanquydinh/TW/Thong_tu/2020/19-2020-TT-BTC/index|19/2020/TT-BTC]] — INF+RAW
- [[04-Vanbanquydinh/TW/Thong_tu/2022/56-2022-TT-BTC/index|56/2022/TT-BTC]] — INF+RAW
- [[04-Vanbanquydinh/TW/Thong_tu/2024/70-2024-TT-BTC/index|70/2024/TT-BTC]] — INF+RAW
- [[04-Vanbanquydinh/TW/Thong_tu/2025/20-2025-TT-BYT/index|20/2025/TT-BYT]] — INF+RAW
- [[04-Vanbanquydinh/TW/Thong_tu/2025/56-2025-TT-BTC/index|56/2025/TT-BTC]] — INF+RAW
- [[04-Vanbanquydinh/TW/Thong_tu/2025/57-2025-TT-BTC/index|57/2025/TT-BTC]] — INF+RAW
- [[04-Vanbanquydinh/TW/Thong_tu/2025/130-2025-TT-BTC/index|130/2025/TT-BTC]] — INF+RAW
- [[04-Vanbanquydinh/TW/Thong_tu/2025/132-2025-TT-BTC/index|132/2025/TT-BTC]] — INF+RAW
- [[04-Vanbanquydinh/TW/Thong_tu/2025/133-2025-TT-BTC/index|133/2025/TT-BTC]] — INF+RAW
- [[04-Vanbanquydinh/TW/Thong_tu/2025/141-2025-TT-BTC/index|141/2025/TT-BTC]] — INF+RAW
- [[04-Vanbanquydinh/TW/Thong_tu/2025/157-2025-TT-BTC/index|157/2025/TT-BTC]] — INF+RAW
- [[04-Vanbanquydinh/TW/Thong_tu/2026/26-2026-TT-BTC/index|26/2026/TT-BTC]] — INF+RAW
- [[04-Vanbanquydinh/TW/Thong_tu/2026/66-2026-TT-BTC/index|66/2026/TT-BTC]] — INF+RAW
- [[04-Vanbanquydinh/TW/Thong_tu/2026/01-2026-TT-KTNN/index|01/2026/TT-KTNN — Thông tư KTNN]] — INF+RAW (Wisdom; ngoài 64 HV/CN)

## Quyết định

- [[04-Vanbanquydinh/TW/Quyet_dinh_TTg/2025/15-2025-QĐ-TTg/index|15/2025/QĐ-TTg]] — INF+RAW
- [[04-Vanbanquydinh/TW/Quyet_dinh_TTg/2026/10-2026-QĐ-TTg/index|10/2026/QĐ-TTg]] — INF+RAW
- [[04-Vanbanquydinh/Da_Nang/Quyet_dinh_CT_UBND/2025/61-2025-QĐ-CTUBND/index|61/2025/QĐ-CTUBND]] — INF+RAW
- [[04-Vanbanquydinh/Da_Nang/Quyet_dinh_UBND/2026/14-2026-QĐ-UBND/index|14/2026/QĐ-UBND]] — INF+RAW
- [[04-Vanbanquydinh/Da_Nang/Quyet_dinh_UBND/2026/71-2026-QĐ-UBND/index|71/2026/QĐ-UBND — lịch DT / quyết toán]] — INF+RAW

## Nghị quyết HĐND (Đà Nẵng / Quảng Nam cũ)

- [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2025/15-2025-NQ-HĐND/index|15/2025/NQ-HĐND — phân cấp thu–chi]] — INF+RAW
- [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2025/52-2025-NQ-HĐND/index|52/2025/NQ-HĐND]] — INF+RAW
- [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2026/79-2026-NQ-HĐND/index|79/2026/NQ-HĐND]] — INF+RAW
- [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2025/14-NQ-HĐND/index|14/NQ-HĐND]] — ngoài INF (toàn văn nguồn công khai)
- [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2022/28-2022-NQ-HĐND/index|28/2022/NQ-HĐND]] — INF+RAW
- [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2022/29-2022-NQ-HĐND/index|29/2022/NQ-HĐND]] — INF+RAW
- [[04-Vanbanquydinh/Quang_Nam_cu/Nghi_quyet_HDND/2018/11-2018-NQ-HĐND/index|11/2018/NQ-HĐND]] — INF+RAW

## Thống kê

Catalog khóa học **chốt 64/64**; toàn bộ kho pháp lý hiện có **71 hồ sơ = 64 catalog + 4 Wisdom + 3 chính quyền 2 cấp**. Trong 64 catalog có **3** ngoài INF (toàn văn nguồn công khai — identity khóa học, không thay bằng số hiệu khác):

- [[04-Vanbanquydinh/TW/Nghi_quyet_TW/2018/27-NQ-TW/index|27-NQ/TW]] — CCTL (21/5/2018). Thực hiện 2026: [[04-Vanbanquydinh/TW/Thong_tu/2025/133-2025-TT-BTC/DieudiemDanchieu/Dieu-04|TT 133 Điều 4]], không thay số hiệu nghị quyết.
- [[04-Vanbanquydinh/TW/Nghi_quyet_TW/2024/57-NQ-TW/index|57-NQ/TW]] — KHCN / ĐMST / CĐS (22/12/2024).
- [[04-Vanbanquydinh/Da_Nang/Nghi_quyet_HDND/2025/14-NQ-HĐND/index|14/NQ-HĐND]] — HĐLĐ GDĐT 12/8/2025. **Không** lấy `14/2025/NQ-HĐND` INF (di dời nhà / lệ phí GPXD).

Không còn mục chờ nạp.

## Ontology (thực thể / quan hệ / quy trình)

TBox: [[02-TAILIEU/ontology|Ontology TBox]]. ABox **trong từng thư mục số hiệu** (cùng chỗ với `toan-van.md`): `Thucthe.md` · `Quanhe.md` · `quytrinh.md`. Wikilink full path — ví dụ [[04-Vanbanquydinh/TW/Luat/2025/89-2025-QH15/Thucthe|Thực thể Luật 89 (ontology)]]. So với 4 buổi cẩm nang: [[03-TIMHIEU/nghien-cuu/ontology-cam-nang|Vanbanquydinh + ontology so với cẩm nang]] (wiki đủ cho người dùng; ABox trục 4 buổi đã điền).

## Liên kết

- Hub: [[hub-goi|Hub gói — lối vào nhu cầu]] — chọn cửa việc trước khi mở catalog.
- Tìm hiểu: [[03-TIMHIEU/index|Tìm hiểu — nắm → nghĩ → làm]] — chuỗi hỏi trước khi trích Điều.
- Khái niệm: [[03-TIMHIEU/khai-niem/index|Khái niệm căn bản]] — gắn số hiệu với việc (thu, chi, TSC…).
- Nghiên cứu: [[03-TIMHIEU/nghien-cuu/index|Nghiên cứu seed (Go)]] — phạm vi 64+4+3 và nguyên tắc không đổ catalog KTNN. Ontology vs cẩm nang: [[03-TIMHIEU/nghien-cuu/ontology-cam-nang|Vanbanquydinh + ontology so với cẩm nang]].
- Giáo trình: [[01-GIAOTRINH/00-index|Giáo trình — hai trục]] — buổi / CĐ đã dẫn số hiệu.
- Tài liệu: [[02-TAILIEU/index|Tài liệu tập huấn]] — file gốc cẩm nang + học viên.
