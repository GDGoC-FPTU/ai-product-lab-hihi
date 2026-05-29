# Deep-Dive & Evaluation Report

> **THÔNG TIN NHÓM:**
>
> * Tên Nhóm: hihi
> * Thành viên:
>   1. Nguyễn Văn Đoan - 2A202600795 (Trưởng nhóm)
>   2. Lê Duy Hùng - 2A202600718
>   3. Trần Hoàng Đạt - 2A202600807
> * Mảng kinh doanh lựa chọn: Vinhomes - Quản lý đô thị thông minh.

---

# Phase 3 - DEEP-DIVE: Phân Tích Chi Tiết Bài Toán

Nhóm quyết định chọn bài toán "Tự động phân loại và điều hướng phản ánh của cư dân trên App Vinhomes Resident" để tiến hành phân tích sâu và đề xuất giải pháp AI.

## 3.1. Sơ lược quy trình hiện tại (Current-State Workflow)

*(Sơ đồ chi tiết được lưu trong file 04-workflow-diagram.pdf)*

- Tổng thời gian xử lý thủ công trung bình: ~13 phút/lượt phản ánh.
- Các nút thắt cổ chai chính (Bottleneck):
  - Bước đọc, hiểu và phân loại thủ công các phản ánh của cư dân (ví dụ: phân biệt sự cố về kỹ thuật điện nước vs. an ninh trật tự vs. vệ sinh cảnh quan).
  - Bước chuyển tiếp thủ công phiếu yêu cầu đến đúng ban quản lý hoặc tổ chuyên môn của từng tòa nhà tương ứng.

---

## 3.2. Problem Statement (6-field) - Vin Smart Future Standard

| Trường thông tin               | Nội dung chi tiết                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Actor / Operator**     | Điều phối viên CSKH thuộc Ban quản lý (BQL) Vinhomes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **2. Current Workflow**     | Khi cư dân gửi phản ánh lên ứng dụng Vinhomes Resident dưới dạng tin nhắn văn bản kèm hình ảnh, điều phối viên CSKH phải đọc thủ công từng yêu cầu, xác định loại sự cố (kỹ thuật, vệ sinh, an ninh...), tạo ticket trên hệ thống ERP nội bộ và chuyển tiếp thủ công sang tổ chuyên trách của tòa nhà đó.                                                                                                                                                              |
| **3. Bottleneck**           | Bước 3 và 4 (mất trung bình 7 phút/phản ánh): Việc đọc hiểu các đoạn text viết tự do của cư dân (đôi khi viết tắt hoặc mô tả không rõ ràng) và tra cứu danh sách tổ chuyên trách trực ca để điều phối thủ công.                                                                                                                                                                                                                                                                     |
| **4. Business Impact**      | Mỗi ngày BQL nhận hàng trăm phản ánh từ hàng vạn căn hộ. Việc xử lý thủ công gây trễ SLA phản hồi (trung bình cư dân phải đợi 12 giờ mới có phản hồi ban đầu). Điều này gây bất mãn cho cư dân, tăng tải cuộc gọi phàn nàn lên tổng đài và ảnh hưởng đến uy tín dịch vụ của Vinhomes.                                                                                                                                                                             |
| **5. Success Metric**       | 1. Giảm thời gian xử lý và điều phối phản ánh của CSKH từ 12 giờ xuống dưới 5 phút.`<br>`2. Tỷ lệ tự động phân loại và chuyển tiếp chính xác đến đúng bộ phận chuyên trách đạt trên 97%.                                                                                                                                                                                                                                                                                              |
| **6. Operational Boundary** | AI được phép trích xuất thông tin, tự động phân loại chủ đề và soạn thảo phiếu yêu cầu nháp (draft ticket). Nghiêm cấm tuyệt đối AI tự động phản hồi lại cư dân hoặc đóng ticket khi chưa có nhân viên CSKH phê duyệt; không tự ý thay đổi trạng thái ưu tiên của ticket đối với các trường hợp khẩn cấp liên quan đến cháy nổ, an toàn tính mạng (các trường hợp này phải lập tức kích hoạt chuông cảnh báo đỏ cho con người xử lý). |

---

## 3.3. Future-State Flow & AI Fit

### Xác định mức độ AI Fit:

- Lựa chọn: LLM Feature (Phân loại ý định, trích xuất thực thể và soạn thảo ticket tự động).
- Lý do: Bài toán phân loại văn bản và chuyển tiếp có cấu trúc rõ ràng. Sử dụng LLM Feature giúp đảm bảo tính tin cậy, kiểm soát chặt chẽ thông qua prompt và dễ dàng tích hợp vào hệ thống ERP sẵn có của Vinhomes mà không cần xây dựng hệ thống Agent tự trị phức tạp.

### Quy trình tương lai (Future-State Flow):

```text
[Bước 1: Tiếp nhận phản ánh từ cư dân qua App]
                │
                ▼
[Bước 2: AI tự động trích xuất và phân loại chủ đề]
                │
                ▼
[Bước 3: AI soạn thảo ticket nháp (gắn nhãn DRAFT_ONLY)]
                │
                ├──────────────────────────────────────────────┐
                ▼ (Siêu khẩn cấp: Cháy nổ...)                 ▼ (Bình thường)
[Kích hoạt cảnh báo đỏ trực tiếp đến BQL]        [Bước 4: CSKH kiểm duyệt tin nháp]
                                                               │
                                                               ▼
                                                 [Chuyển tiếp sang đội kỹ thuật]
                                                               │
                                                               ▼
                                                 [Fallback: Nếu AI sai, CSKH tự sửa]
```

- Human-in-the-loop (HITL): Nhân viên CSKH kiểm tra lại loại sự cố và nơi tiếp nhận do AI đề xuất trên Dashboard trước khi nhấn nút duyệt để chuyển tiếp phiếu.
- Phương án dự phòng (Fallback): Khi mô hình trả về độ tự tin (confidence score) phân loại dưới 80%, hoặc nội dung văn bản quá mơ hồ, hệ thống sẽ tự động gắn nhãn "Cần phân loại thủ công" để chuyển trực tiếp cho nhân viên CSKH xử lý từ đầu.

---

# Phase 5 - EVALUATE: Đánh Giá Độ Sẵn Sàng & Quyết Định

## 5.1. AI Readiness Checklist

- [X] Dữ liệu mẫu (Data): Đã có sẵn kho dữ liệu gồm hàng vạn log phản ánh lịch sử và ticket đã xử lý thành công được gắn nhãn chính xác để huấn luyện và kiểm thử mô hình.
- [X] Kiểm soát rủi ro (Risk Control): Đã thiết lập ranh giới an toàn (Operational Boundary) nghiêm ngặt để con người kiểm duyệt (HITL) và xử lý riêng biệt các trường hợp khẩn cấp.
- [X] Sự sẵn sàng của các bên (Stakeholders): Ban quản lý vận hành Vinhomes sẵn sàng ứng dụng công nghệ để giải quyết nút thắt cổ chai về SLA và nâng cao điểm số hài lòng của cư dân.

---

## 5.2. Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future

- Quyết định: GO (Bắt đầu xây dựng Prototype).
- Lý giải quyết định (Justification):

  1. Hiệu quả rõ rệt về SLA: Giảm thời gian chờ đợi phản hồi của cư dân từ hàng giờ xuống còn dưới vài phút, nâng cao hình ảnh dịch vụ của Vinhomes.
  2. Giải phóng năng lượng CSKH: Tự động hóa đến 90% tác vụ đọc hiểu và phân loại lặp đi lặp lại hằng ngày, giúp nhân viên CSKH có nhiều thời gian hơn để giải quyết trực tiếp các vấn đề phức tạp.
  3. Khả năng triển khai nhanh chóng: Giải pháp LLM Feature sử dụng mô hình Gemini 2.5 Flash có thể triển khai thử nghiệm (pilot) nhanh chóng với chi phí vận hành tối ưu.
