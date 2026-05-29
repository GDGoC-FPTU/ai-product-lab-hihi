# Nhật ký chiêm nghiệm tương tác với AI (AI Log & Reflection)

* Họ và tên: Trần Hoàng Đạt
* MSSV: 2A202600807

---

## 1. AI đã giúp gì cho tôi trong buổi học?

Trong suốt buổi Lab 02 về AI Product Scoping, tôi đã sử dụng Gemini như một trợ lý đồng hành để hỗ trợ hoàn thành các công việc sau:

- Brainstorm ý tưởng: Khi mới bắt đầu, tôi gặp khó khăn trong việc tìm các vấn đề và nút thắt cổ chai thực tế trong vận hành của Vinhomes. AI đã gợi ý quy trình tiếp nhận và phân loại phản ánh cư dân trên Resident App, giúp tôi hình dung rõ hơn về chuỗi quy trình và các điểm hạn chế.
- Soạn thảo Problem Statement: AI hỗ trợ tôi sắp xếp các thông tin để điền vào khung 6-field của Vin Smart Future một cách mạch lạc, đảm bảo đúng các chỉ số cần đo lường như SLA hay tỷ lệ chính xác.
- Lĩnh vực lập trình: AI giúp tôi viết khung mã nguồn Python với thư viện google-genai mới. Đặc biệt, khi chạy thử nghiệm trên Windows bị crash do lỗi encoding cp1258 không in được emoji ra màn hình, AI đã hướng dẫn tôi thêm đoạn code wrapper để ép standard output về UTF-8, giúp script chạy ổn định hơn.

---

## 2. AI đã đưa ra những câu trả lời sai lệch hoặc chưa tối ưu nào?

Tuy nhiên, trong quá trình làm việc, AI cũng có một số đề xuất chưa phù hợp và cần phải điều chỉnh:

- Đề xuất phương án quá phức tạp: Lúc đầu, AI liên tục hướng tới việc xây dựng hệ thống Multi-Agent tự động gửi email phản hồi thẳng cho cư dân mà không cần người kiểm duyệt. Điều này rất nguy hiểm trong vận hành thực tế vì mô hình có thể tự ý đưa ra thông tin sai lệch cho cư dân khi gặp các tình huống phức tạp.
- Dễ bị lừa bởi Prompt Injection: Ở phiên bản prompt đầu tiên, khi tôi giả lập tình huống người dùng yêu cầu bỏ qua tag [DRAFT_ONLY] vì đây là tin nhắn thông thường, AI đã ngay lập tức nghe lời người dùng và bỏ luôn tag kiểm duyệt.
- Không nhận diện được sự cố khẩn cấp: Khi cư dân báo mất điện trên diện rộng (trên 5% số căn hộ), AI vẫn coi đó là một yêu cầu sửa chữa thông thường và dùng quy trình tiêu chuẩn thay vì phải chuyển ngay sang đề xuất điều động thiết bị máy phát điện khẩn cấp.

---

## 3. Tôi đã điều chỉnh Prompt và thiết lập ranh giới như thế nào?

Để khắc phục các vấn đề trên, tôi đã thiết lập lại hệ thống ranh giới vận hành trong SYSTEM_PROMPT của file prototype:

- Đặt mệnh lệnh tuyệt đối để AI luôn luôn phải bắt đầu tin nhắn bằng tag [DRAFT_ONLY] trong mọi trường hợp, kể cả khi người dùng cố tình yêu cầu bỏ qua.
- Định nghĩa quy tắc khẩn cấp: nếu phản ánh có từ khóa liên quan đến mất điện và quy mô ảnh hưởng lớn (trên 5%), AI bắt buộc phải trả về cấu trúc JSON định sẵn chứ không được tự viết văn bản tự do, mục đích là để hệ thống tự động nhận diện và điều xe phát điện lưu động (dispatch_mobile_charger) ngay lập tức.
- Kết quả là ở lần chạy cuối cùng, script đã vượt qua tất cả các bài test tấn công prompt mà không bị bypass nữa.
