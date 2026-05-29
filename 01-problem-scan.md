# Name: Trần Hoàng Đạt - 2A202600807

# PHRASE 1. SCAN

Dưới đây là bảng quét cơ hội (SCAN) áp dụng 4 lenses để tìm kiếm các bài toán/bottleneck thực tế trong hoạt động vận hành của các công ty thành viên thuộc tập đoàn Vingroup:

| # | Subsidiary         | Lens                   | Mô tả ngắn bài toán / Bottleneck                                                                                                                                                                                             |
| - | ------------------ | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | **Xanh SM**  | Tốn thời gian        | Điều phối viên phải xử lý thủ công các báo cáo khẩn cấp từ tài xế về sự cố sạc pin hoặc hết pin giữa đường (mất 15-20 phút/lượt).                                                                  |
| 2 | **Vinhomes** | Lặp lại              | Ban quản lý tòa nhà phải phân loại và điều hướng thủ công hàng trăm phản ánh/khiếu nại của cư dân (hỏng nước, mất điện, ồn ào...) gửi qua App Vinhomes Resident đến các bộ phận chức năng. |
| 3 | **Vinmec**   | Tốn thời gian        | Bác sĩ điều trị mất nhiều thời gian tổng hợp thông tin lâm sàng, kết quả xét nghiệm để viết tóm tắt hồ sơ xuất viện (Discharge Summary) cho bệnh nhân (20-30 phút/bệnh nhân).                      |
| 4 | **VinFast**  | AI-upgrade             | Hệ thống gợi ý trạm sạc trên màn hình trung tâm của xe điện chưa tối ưu theo dung lượng pin thực tế, loại cổng sạc (CCS2/GBT) và hành trình di chuyển thực tế của tài xế.                         |
| 5 | **Vinpearl** | Pain từ người khác | Đội ngũ quản lý khách sạn phải tự đọc và phân tích hàng nghìn đánh giá (review) của khách hàng trên Booking.com, Agoda, Google Maps để lọc ra các phàn nàn khẩn cấp về dịch vụ.                 |
| 6 | **Xanh SM**  | Lặp lại              | Bộ phận đối soát tài chính phải tra cứu thủ công lịch sử định vị GPS và log chuyến đi để xác minh khiếu nại của khách hàng về việc tài xế đi sai lộ trình/tính sai tiền.                      |

---

# PHRASE 2. QUICK-ASSESS

Dưới đây là phân tích chi tiết cho 3 bài toán tiềm năng nhất được lựa chọn từ danh sách quét ở trên:

## Vinhomes — Tự động phân loại và điều hướng phản ánh cư dân

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Cư dân gửi khiếu nại/phản ánh lên App Vinhomes    │
│ Resident cần được phân loại và chuyển tiếp nhanh đến đúng   │
│ bộ phận kỹ thuật, vệ sinh hoặc an ninh của tòa nhà.         │
│ Công ty thành viên: [x] Vinhomes                            │
│                                                             │
│ Ai đang đau? Điều phối viên CSKH (quá tải), Cư dân (chờ lâu)│
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Cư dân gửi text/ảnh phản ánh lên App Vinhomes Resident │
│   → 2. Nhân viên CSKH đọc nội dung phản ánh để hiểu vấn đề  │
│   → 3. CSKH xác định bộ phận xử lý và tạo ticket thủ công   │
│   → 4. Hệ thống gửi thông báo đến nhân viên kỹ thuật thực địa│
│                                                             │
│ Bước nào tốn nhất? Bước 2 và 3 (8 phút/phản ánh)            │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 và 3           │
│ (Trích xuất ý định -> Phân loại loại sự cố -> Tự động route)│
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Giảm thời gian điều phối từ 12 giờ (SLA cũ) ──> dưới 5 phút │
│                                                             │
│ Quick Architecture: [x] LLM Feature (Phân loại & Trích xuất)│
└─────────────────────────────────────────────────────────────┘
```

---

## Xanh SM — Xử lý sự cố sạc pin thực địa của tài xế

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Tài xế Xanh SM báo sự cố hết pin/pin yếu dưới 5%  │
│ giữa đường cần được điều phối cứu hộ hoặc trạm sạc gần nhất.│
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau? Tài xế (chờ lâu/lo lắng), Điều phối viên (quá  │
│ tải vào giờ cao điểm).                                      │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Tài xế gọi điện/báo tin nhắn khẩn cấp lên tổng đài     │
│   → 2. Điều phối viên định vị vị trí xe trên bản đồ quản lý │
│   → 3. Tra cứu danh sách các trạm sạc VinFast còn trụ trống │
│   → 4. Soạn tin nhắn chỉ dẫn/khoảng cách gửi cho tài xế     │
│   → 5. Liên hệ xe cứu hộ pin di động nếu pin dưới ngưỡng an toàn│
│                                                             │
│ Bước nào tốn nhất? Bước 3 và 4 (10 phút/lượt)               │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 và 4           │
│ (Lấy tọa độ -> Truy vấn trạm trống -> Soạn tin nhắn nháp)   │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Giảm thời gian xử lý sự cố từ 15 phút ──> dưới 3 phút.      │
│ Tỉ lệ gợi ý đúng trạm sạc đạt 98%.                          │
│                                                             │
│ Quick Architecture: [x] LLM Feature (Sinh tin nhắn & Logic) │
└─────────────────────────────────────────────────────────────┘
```

---

## Vinmec — Tự động soạn thảo tóm tắt hồ sơ xuất viện

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Tự động trích xuất thông tin bệnh án điện tử để   │
│ soạn bản tóm tắt hồ sơ xuất viện ngắn gọn cho bệnh nhân.    │
│ Công ty thành viên: [x] Vinmec                              │
│                                                             │
│ Ai đang đau? Bác sĩ điều trị (quá tải công việc giấy tờ),   │
│ Bệnh nhân (phải chờ đợi lâu để được xuất viện).             │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Bác sĩ mở hồ sơ bệnh án điện tử (EMR) của bệnh nhân    │
│   → 2. Đọc và tổng hợp kết quả xét nghiệm, chẩn đoán hình ảnh│
│   → 3. Gõ tay tóm tắt diễn tiến lâm sàng & dặn dò xuất viện │
│   → 4. In ấn, ký tên xác nhận và bàn giao cho bệnh nhân     │
│                                                             │
│ Bước nào tốn nhất? Bước 2 và 3 (20 phút/bệnh nhân)          │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 và 3           │
│ (Tổng hợp thông tin lâm sàng -> Draft văn bản tóm tắt xuất viện)│
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Giảm thời gian bác sĩ viết tóm tắt từ 20 phút ──> dưới 3 phút│
│                                                             │
│ Quick Architecture: [x] LLM Feature (RAG & Sinh văn bản)    │
└─────────────────────────────────────────────────────────────┘
```
