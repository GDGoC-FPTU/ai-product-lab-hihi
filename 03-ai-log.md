# Nhật kỳ chiêm nghiệm tương tác với AI (AI Log & Reflection)

* Họ và tên: Trần Hoàng Đạt
* MSSV: 2A202600807

---

## 1. AI đã giúp gì cho tôi trong buổi học?

Trong suốt buổi Lab 02, nhóm chúng tôi tự thảo luận và thống nhất ý tưởng bài toán Vinhomes cũng như tự vẽ sơ đồ quy trình. AI (Gemini) hoàn toàn không tham gia vào khâu brainstorm hay đưa ra ý tưởng thiết kế quy trình nghiệp vụ. Tôi chỉ sử dụng AI như một trợ lý kỹ thuật hỗ trợ các công việc lập trình và sửa lỗi:

- Hướng dẫn cú pháp: AI hỗ trợ chuyển đổi cú pháp và viết khung code Python sử dụng thư viện SDK mới (`google-genai` của Gemini 2.5 Flash), giúp đẩy nhanh tốc độ viết mã nguồn cho file prototype.
- Khắc phục lỗi môi trường: Khi chạy thử nghiệm code trên terminal Windows, chương trình bị crash do lỗi mã hóa `cp1258` không in được các ký tự unicode và emoji. AI đã hỗ trợ tôi viết đoạn wrapper chuẩn hóa stdout/stderr sang UTF-8 để khắc phục triệt để lỗi này.

---

## 2. AI đã đưa ra những câu trả lời sai lệch hoặc chưa tối ưu nào?

Khi hỗ trợ thiết lập các ca kiểm thử tấn công prompt (Adversarial Tests), AI ban đầu có các đề xuất chưa tối ưu:

- Đề xuất prompt lỏng lẻo: AI gợi ý một số câu chỉ thị hệ thống khá dài dòng nhưng không chặt chẽ, dẫn đến việc mô hình dễ dàng bị người dùng "thuyết phục" bỏ qua nhãn `[DRAFT_ONLY]` trong Test Case 2 để gửi thẳng phản hồi.
- Nhận diện sai điều kiện: Khi xử lý điều kiện khẩn cấp liên quan đến việc mất điện ảnh hưởng diện rộng, prompt ban đầu do AI gợi ý không làm rõ ranh giới hành động, khiến mô hình đôi khi vẫn trả về phản hồi văn bản thông thường thay vì xuất ra cấu trúc JSON điều động xe cứu hộ phát điện (`dispatch_mobile_charger`).

---

## 3. Tôi đã điều chỉnh Prompt và thiết lập ranh giới như thế nào?

Để đảm bảo an toàn tuyệt đối cho hệ thống và vượt qua các bài stress-test ranh giới:

- Tôi đã trực tiếp viết lại phần chỉ thị hệ thống `SYSTEM_PROMPT` trong file code, đưa ra các mệnh lệnh tuyệt đối bắt buộc mô hình luôn đặt tag `[DRAFT_ONLY]` ở đầu mọi tin nhắn nháp trong mọi hoàn cảnh.
- Thiết lập rõ cấu trúc đầu ra bắt buộc của quy tắc cứu hộ: nếu phản ánh mất điện chạm ngưỡng diện rộng (trên 5% căn hộ), mô hình bắt buộc phải chuyển sang định dạng JSON quy định cho hành động `dispatch_mobile_charger`.
- Nhờ những điều chỉnh cấu trúc ranh giới nghiêm ngặt này, script chạy thực tế đã kiểm thử thành công và pass toàn bộ các tiêu chí an toàn của autograder.
