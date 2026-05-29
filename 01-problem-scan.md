Nhóm hihi - Nguyễn Văn Đoan - 2A202600795

# Lab 02 — Worksheet: AI Product Scoping - Problem Scan (Vin Smart Future)

---

## 🏛️ Bối cảnh cá nhân
Tôi là **Nguyễn Văn Đoan**, AI Engineer tại **Vin Smart Future**. Nhiệm vụ của tôi là khảo sát và phân tích quy trình vận hành tại các công ty thành viên thuộc hệ sinh thái Vingroup, từ đó tìm kiếm và đánh giá tính khả thi của các bài toán có thể giải quyết hoặc tối ưu hóa hiệu quả bằng công nghệ AI. 

Dưới đây là nội dung chi tiết của **Phase 1 (SCAN)** và **Phase 2 (QUICK-ASSESS)** thể hiện tư duy tìm kiếm bài toán cá nhân trước khi bước vào thảo luận nhóm.

---

# 🔍 Phase 1 — SCAN: Tìm kiếm cơ hội (Cá nhân)

Sử dụng **4 Lenses** dưới đây để quét qua hoạt động vận hành của các công ty thành viên Vingroup nhằm phát hiện ra các bottleneck và điểm kém hiệu quả thực tế:
1. **Lặp lại (Repetitive):** Tác vụ lặp đi lặp lại nhiều lần hàng ngày.
2. **Tốn thời gian (Time-consuming):** Tác vụ ngốn thời gian xử lý thủ công của nhân viên.
3. **AI có thể tốt hơn (AI-upgrade):** Dịch vụ hiện tại còn chậm hoặc phản hồi rập khuôn.
4. **Pain từ người khác (Stakeholder Pain):** Bottleneck khiến khách hàng hoặc nhân viên thực địa phàn nàn.

### 📝 Bảng quét cơ hội (SCAN Opportunity Table):

| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | **Xanh SM (GSM)** | Tốn thời gian / Pain từ người khác | Tài xế báo cáo sự cố sạc pin / hết pin giữa đường, điều phối viên phải tra cứu thủ công vị trí xe, tìm trạm sạc trống tương thích và viết tin nhắn hướng dẫn chỉ đường. |
| 2 | **Vinmec** | Tốn thời gian / Pain từ người khác | Bác sĩ mất quá nhiều thời gian (20-30 phút/bệnh nhân) để đọc dữ liệu bệnh án điện tử EHR và tự soạn thảo thủ công bản tóm tắt hồ sơ xuất viện (Discharge Summary). |
| 3 | **Vinhomes** | Lặp lại / Tốn thời gian | Phân loại và định tuyến tự động khiếu nại của cư dân gửi qua App Vinhomes Resident (mất nước, hỏng đèn, ồn ào...) tới đúng Ban quản lý (BQL) của từng tòa nhà cụ thể. |
| 4 | **Vinpearl** | Tốn thời gian | Nhân viên đặt phòng phải đọc và phân tích email đặt phòng theo đoàn (Group Booking) phức tạp từ đại lý lữ hành để kiểm tra quỹ phòng trống và lên lệnh đặt phòng thủ công trên PMS. |
| 5 | **VinFast** | Lặp lại | So khớp dữ liệu sạc điện hằng tuần từ hàng nghìn trụ sạc liên kết ngoài (đối tác thứ ba) với hóa đơn thực tế gửi về hệ thống tài chính để đối chiếu công nợ. |
| 6 | **Xanh SM (GSM)** | AI-upgrade / Pain từ người khác | Tự động phân tích ghi âm cuộc gọi hủy chuyến và ghi chú viết tay của tài xế để phân loại chính xác lý do hủy chuyến, phục vụ việc cải thiện chất lượng dịch vụ. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards (Cá nhân)

Chọn **top 3 bài toán tiềm năng nhất** từ danh sách trên để tiến hành đánh giá nhanh và chi tiết hóa thông tin vận hành.

---

## 📱 QUICK PROBLEM CARD #1: Xanh SM - Xử lý sự cố sạc pin thực địa

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu): Tài xế Xanh SM báo cáo sự cố hết pin hoặc │
│ sự cố sạc pin thực địa cần hỗ trợ khẩn cấp trạm sạc gần     │
│ nhất hoặc điều động xe cứu hộ pin lưu động.                  │
│                                                             │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)?                                        │
│ - Tài xế Xanh SM: Lo lắng khi xe sắp cạn pin, bị động ngoài │
│   đường, ảnh hưởng trực tiếp đến thu nhập và an toàn.        │
│ - Điều phối viên (Dispatcher): Bị quá tải vào giờ cao điểm, │
│   phải xử lý gấp nhiều sự cố cùng lúc.                      │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Tài xế gọi tổng đài điều vận báo sự cố pin/sắp hết pin │
│   ──> 2. Điều phối viên tra cứu thủ công vị trí GPS của xe  │
│   ──> 3. Mở dashboard trạm sạc VinFast, tìm trụ trống phù   │
│          hợp với cổng sạc của dòng xe (VF5/e34/VF8)         │
│   ──> 4. Viết thủ công tin nhắn SMS/In-app chỉ đường gửi xe │
│   ──> 5. Gọi xe sạc pin cứu hộ di động nếu pin dưới 5%      │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 & 4                 │
│ (⏱ 10 - 12 phút/lượt xử lý)                                  │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 & 4            │
│ (Tự động hóa lấy dữ liệu GPS -> Tra cứu trụ sạc tương thích │
│ trống -> Draft tin nhắn chỉ dẫn/Đề xuất cứu hộ)              │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian điều phối và soạn tin nhắn chỉ dẫn cho tài xế │
│ từ trung bình 15 phút ──> dưới 3 phút/lượt.                  │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

> [!NOTE]
> **Lý do lựa chọn & Đề xuất kiến trúc:**
> Quy trình có các bước phản ứng nhanh theo dữ liệu thời gian thực. Việc sử dụng **LLM** đóng vai trò là một trợ lý (Co-pilot) giúp trích xuất thông tin định vị, đối chiếu loại xe với loại cổng sạc (CCS2/GBT) và soạn thảo tin nhắn hướng dẫn tiếng Việt cực kỳ tự nhiên, chính xác. Bắt buộc có Human-in-the-loop (HITL) phê duyệt trước khi gửi tin đi để tránh rủi ro an toàn.

---

## 🏥 QUICK PROBLEM CARD #2: Vinmec - Soạn thảo tóm tắt hồ sơ xuất viện (Discharge Summary)

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Tự động trích xuất thông tin lâm sàng từ  │
│ bệnh án điện tử (EHR) để soạn thảo bản tóm tắt hồ sơ xuất   │
│ viện y khoa và bản dặn dò bình dân dễ hiểu cho bệnh nhân.   │
│                                                             │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [x] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)?                                        │
│ - Bác sĩ điều trị: Quá tải vì thủ tục giấy tờ hành chính    │
│   sau mỗi ca điều trị, làm giảm thời gian chuyên môn khám.  │
│ - Bệnh nhân xuất viện: Phải chờ lâu để nhận hồ sơ xuất viện.│
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Bác sĩ xem lại toàn bộ bệnh án điện tử (EHR) của bệnh  │
│      nhân (xét nghiệm, chẩn đoán hình ảnh, lịch sử điều trị)│
│   ──> 2. Tổng hợp thủ công các chỉ số lâm sàng quan trọng   │
│   ──> 3. Gõ tay bản tóm tắt hồ sơ xuất viện (chuẩn y khoa)   │
│   ──> 4. Viết tay phần dặn dò, dịch từ ngữ y khoa chuyên    │
│          ngành thành lời khuyên dễ hiểu tại nhà cho bệnh nhân│
│   ──> 5. In ấn, ký duyệt và chuyển bộ phận hành chính đóng dấu│
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2, 3 & 4              │
│ (⏱ 20 - 30 phút/bệnh nhân)                                  │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2, 3 & 4         │
│ (LLM phân tích dữ liệu EHR có cấu trúc và phi cấu trúc để   │
│ draft tự động bản tóm tắt y khoa và bản diễn giải bình dân) │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian bác sĩ soạn tóm tắt hồ sơ xuất viện từ       │
│ trung bình 25 phút/bệnh nhân ──> dưới 5 phút/bệnh nhân.     │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

> [!WARNING]
> **Ranh giới an toàn nghiêm ngặt (Operational Boundary):**
> Do liên quan trực tiếp đến sức khỏe con người, AI chỉ đóng vai trò **Drafting Assistant**. Tuyệt đối không được in hoặc lưu hồ sơ trực tiếp lên hệ thống EHR của Vinmec nếu không có chữ ký điện tử xác nhận của Bác sĩ điều trị sau khi đã rà soát lại thông tin (100% HITL).

---

## 🏢 QUICK PROBLEM CARD #3: Vinhomes - Tự động phân loại & điều hướng khiếu nại cư dân

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Tự động đọc hiểu, phân loại và định tuyến │
│ phản ánh của cư dân từ ứng dụng Vinhomes Resident đến đúng  │
│ Ban quản lý (BQL) tòa nhà và bộ phận kỹ thuật thực địa.     │
│                                                             │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)?                                        │
│ - Nhân viên CSKH Trung tâm: Quá tải vì hàng nghìn phản ánh  │
│   mỗi ngày từ hàng chục khu đô thị Vinhomes toàn quốc.      │
│ - Cư dân Vinhomes: Chờ đợi phản hồi lâu khi gặp sự cố tại   │
│   căn hộ (ví dụ: rò rỉ nước, hỏng thang máy...).            │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Cư dân gửi phản ánh bằng chữ/ảnh lên App Resident      │
│   ──> 2. Điều phối viên trung tâm đọc phản ánh, phân tích   │
│          nội dung xem thuộc loại vấn đề gì (Kỹ thuật/An ninh)│
│   ──> 3. Tra cứu thông tin căn hộ thuộc tòa nhà/phân khu nào│
│   ──> 4. Gán tag phân loại và chuyển tiếp yêu cầu đến tài    │
│          khoản của BQL tòa nhà đó trên CRM nội bộ           │
│   ──> 5. BQL tiếp nhận và cử nhân sự kỹ thuật xuống xử lý    │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 4                 │
│ (⏱ 3 - 6 tiếng từ khi gửi đến khi BQL nhận đúng do quá tải) │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2, 3 & 4         │
│ (AI tự động xử lý ngôn ngữ tự động (NLP/LLM) để gán tag phân │
│  loại, định vị tòa nhà và route trực tiếp trên CRM)         │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian xử lý và phân phối phản ánh cư dân từ        │
│ trung bình 4 giờ ──> dưới 10 giây (gần như tức thời).        │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [ ] LLM  [x] Agent │
└─────────────────────────────────────────────────────────────┘
```

> [!TIP]
> **Cơ chế Fallback & Tự động hóa thông minh:**
> Với các khiếu nại phức tạp hoặc có độ tự tin phân loại thấp (< 80%), hệ thống sẽ kích hoạt **Fallback**, tự động chuyển về cho điều phối viên CSKH con người xử lý thủ công. Điều này đảm bảo tính ổn định cao cho dịch vụ Vinhomes.

---

## 🏁 Tổng kết
Cả 3 bài toán trên đều có tiềm năng ứng dụng AI cực lớn và bám sát vào 4 thấu kính cốt lõi nhằm giải phóng thời gian và công sức cho nhân sự của **Vin Smart Future**. Trong các bước thảo luận tiếp theo, tôi sẽ đề xuất bài toán **"Card #1 — Xanh SM - Xử lý sự cố sạc pin thực địa"** để nhóm cùng làm Deep-Dive và xây dựng bản prompt prototype, do đây là bài toán có tác động trực tiếp nhất tới trải nghiệm thực tế của tài xế và khách hàng Xanh SM theo thời gian thực.
