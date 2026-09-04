# Đề xuất và Định hướng Phát triển Hệ thống Wiki Đà Nẵng

**Ngày cập nhật:** 04/09/2026

## 1. Tầm nhìn và Mục tiêu

Hệ thống Wiki này (`DANANG_CQ2cap_Kiemtoan`) được xây dựng với mục tiêu tối thượng là phục vụ **Công chức, viên chức bình thường** đang công tác tại thành phố Đà Nẵng. 

Hệ thống phải loại bỏ hoàn toàn các yếu tố hàn lâm, kỹ thuật hoặc các quy trình kiểm toán nội bộ phức tạp gây bối rối cho người dùng không chuyên. Mọi thông tin cần được viết bằng văn phong **khúc chiết, dễ hiểu, đi thẳng vào nghiệp vụ hàng ngày**.

## 2. Kiến trúc 5 Trụ cột (Phân hệ TIMHIEU)

Để đảm bảo tính tinh gọn, toàn bộ các tài liệu tìm hiểu nghiệp vụ được cô đọng lại thành 5 chuyên đề cốt lõi, phản ánh sát nhất thực tiễn công việc tại Đà Nẵng từ năm 2025:

1. **Sự thay đổi thành Chính quyền 2 cấp:** Tổng hợp cấu trúc tổ chức, cơ quan, và sự thay đổi thẩm quyền khi không còn HĐND, UBND cấp quận/huyện.
2. **Dịch vụ Công trực tuyến:** Quy trình tiếp nhận, giải quyết thủ tục hành chính liên thông, số hóa.
3. **Vị trí việc làm của Công chức:** Quyền hạn, trách nhiệm, tiêu chuẩn và chính sách tinh giản biên chế, đãi ngộ.
4. **Ngân sách Nhà nước (NSNN):** Lập, điều chỉnh, phân bổ dự toán theo cơ chế cấp xã nộp thẳng và nhận dự toán từ cấp thành phố.
5. **Tài sản Công (TSC):** Quy trình đầu tư, mua sắm, thanh lý và phân cấp thẩm quyền tài sản công.

## 3. Quy hoạch Kỹ thuật và Quản trị hệ thống

- **Gom nhóm kỹ thuật:** Mọi tệp tin phục vụ bảo trì, kịch bản (scripts), báo cáo (reports), hay cấu trúc dữ liệu (schemas) đều được gom gọn vào thư mục `KY_THUAT/`. Người dùng cuối không cần (và không nên) tương tác với khu vực này.
- **Tính chính xác pháp lý:** Văn bản gốc, toàn văn và các quyết định, nghị quyết (như Nghị quyết sáp nhập, Quyết định giao dự toán) tiếp tục được duy trì tại thư mục `Vanbanquydinh/`. Mọi hướng dẫn ở phân hệ tìm hiểu đều phải có link trỏ về văn bản pháp lý tương ứng.

## 4. Các bước tiếp theo

1. Thường xuyên rà soát và bổ sung nội dung thực tiễn cho 5 trụ cột trên từ đóng góp của chính công chức các Sở, Ban, Ngành và xã/phường.
2. Kiểm duyệt chặt chẽ ngôn từ: Đảm bảo không sử dụng biệt ngữ kỹ thuật phần mềm (như ontology, YAML, markdown, frontmatter) trong các bài viết hướng dẫn nghiệp vụ.
3. Tích hợp các biểu mẫu (DOCX, PDF điền được) trực tiếp vào các trang hướng dẫn (Dịch vụ công, Quản lý tài sản) để tải về sử dụng ngay.
