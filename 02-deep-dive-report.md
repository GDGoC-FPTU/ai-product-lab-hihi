# 02 - Deep Dive Report

## Thong tin nhom

- Ten nhom: hihi
- Thanh vien:
  - Le Duy Hung - LDH1401
- Vai tro gia dinh trong bai lab: AI Product Engineer, phu trach scoping, prompt prototype va danh gia ranh gioi van hanh.

## Quyet dinh lua chon bai toan

Nhom chon bai toan: **Xanh SM Dispatcher Co-pilot cho su co pin thap thuc dia**.

Muc tieu la ho tro dieu phoi vien Xanh SM xu ly nhanh tinh huong tai xe xe dien bao pin thap, can tim tram sac gan nhat hoac dieu xe sac pin di dong. AI khong duoc tu dong gui lenh/tin nhan; AI chi duoc tao ban nhap co nhan `[DRAFT_ONLY]` de dieu phoi vien duyet.

## Phase 3.1 - Current-State Workflow Mapping

```text
Tai xe bao su co pin thap
        |
        v
[1] Dieu phoi vien nhan cuoc goi/chat
    Thoi gian: 2 phut
    Handoff: Tai xe -> Tong dai dieu van
        |
        v
[2] Tra cuu bien so, dong xe, toa do GPS
    Thoi gian: 2 phut
    Handoff: Tong dai -> Dashboard doi xe
        |
        v
[3] Tra cuu tram sac VinFast gan nhat, con tru trong
    Thoi gian: 5 phut
    Bottleneck: can so khop khoang cach, loai cong sac, trang thai tru
        |
        v
[4] Soan tin nhan huong dan tai xe
    Thoi gian: 5 phut
    Bottleneck: de sai thong tin, thieu canh bao an toan pin
        |
        v
[5] Goi doi cuu ho sac pin di dong neu pin qua thap
    Thoi gian: 1 phut
    Handoff: Dieu van -> Doi cuu ho

Tong thoi gian thu cong: khoang 15 phut/luot.
```

### Diem ngheo va rui ro hien tai

| Hang muc | Mo ta |
|---|---|
| Bottleneck chinh | Buoc 3 va 4 mat tong cong khoang 10 phut, chiem phan lon thoi gian xu ly. |
| Rui ro van hanh | Dieu phoi vien co the de xuat tram sac qua xa khi xe con pin rat thap. |
| Rui ro khach hang | Tai xe cham den diem don, khach huy chuyen, trai nghiem dich vu giam. |
| Rui ro an toan | Xe co the can pin giua duong neu dieu huong sai. |

## Phase 3.2 - Problem Statement 6-field

| Field | Noi dung chi tiet |
|---|---|
| 1. Actor / Operator | Dieu phoi vien Xanh SM tai trung tam dieu van, xu ly su co cua tai xe xe dien. |
| 2. Current Workflow | Hien tai dieu phoi vien nhan cuoc goi/chat, tra GPS xe, mo dashboard tram sac, kiem tra tram con tru trong, soan tin nhan huong dan va goi cuu ho neu can. Quy trinh chu yeu thu cong, mat khoang 15 phut/luot. |
| 3. Bottleneck | Tra cuu tram sac phu hop va soan huong dan cho tai xe. Hai buoc nay yeu cau tong hop nhieu nguon du lieu va viet lai bang ngon ngu ro rang. |
| 4. Business Impact | Gia dinh co 80 su co pin/ngay tai Ha Noi. Moi su co mat 15 phut, tuong duong 20 gio dieu phoi/ngay. Neu rut xuong 3 phut, tiet kiem khoang 16 gio/ngay va giam thoi gian xe khong san sang don khach. |
| 5. Success Metric | Giam thoi gian xu ly tu 15 phut xuong duoi 3 phut/luot; 98% draft dung ranh gioi pin; 100% draft co nhan `[DRAFT_ONLY]`; khong co truong hop pin duoi 5% ma AI de xuat tram sac xa hon 5km. |
| 6. Operational Boundary | AI duoc phep tong hop thong tin va draft de xuat. AI khong duoc tu dong gui tin nhan, khong duoc bo nhan `[DRAFT_ONLY]`, khong duoc khuyen tai xe di den tram sac xa hon 5km neu pin duoi 5%, va phai chuyen sang `dispatch_mobile_charger` trong truong hop pin nguy kich. |

## Phase 3.3 - Future-State Flow va AI Fit

### AI Fit Matrix

| Lua chon | Danh gia |
|---|---|
| Rule / State Machine | Phu hop cho rule cung nhu nguong pin duoi 5%, nhung khong linh hoat khi can soan huong dan bang ngon ngu tu nhieu nguon du lieu. |
| LLM Feature | Phu hop nhat. LLM co the tong hop GPS, pin, loai xe, tram sac va tao draft ro rang cho dieu phoi vien duyet. |
| Agentic Loop | Chua can thiet. Rui ro van hanh cao neu agent tu dong goi API dieu xe hoac gui tin nhan khi chua co nguoi duyet. |

Quyet dinh: **LLM Feature + Rule Guardrails + Human-in-the-loop**.

### Future-State Flow

```text
[1] Tai xe bao su co pin thap
        |
        v
[2] He thong tu lay GPS, dong xe, % pin, trang thai tram sac
        |
        v
[3] Rule guardrail kiem tra:
    - Neu pin < 5%: khong de xuat tram > 5km, tao action dispatch_mobile_charger
    - Neu pin >= 5%: cho phep LLM draft huong dan tram gan nhat phu hop
        |
        v
[4] LLM tao output co nhan [DRAFT_ONLY]
        |
        v
[5] Dieu phoi vien review, sua neu can, roi moi gui cho tai xe
        |
        v
[6] Fallback:
    - Neu AI thieu du lieu/khong tu tin: quay ve quy trinh thu cong
    - Neu dashboard tram sac loi: goi truc tiep hotline tram sac hoac dieu xe cuu ho
```

## Phase 4 - Prompt Prototype va Boundary Test

File code: `extras/prompt_prototype.py`.

Ranh gioi duoc test:

1. Moi output gui cho nguoi van hanh phai bat dau bang `[DRAFT_ONLY]`.
2. Neu pin duoi 5%, AI khong duoc de xuat tram sac xa hon 5km; phai tra ve action `dispatch_mobile_charger`.
3. Neu user co tinh yeu cau bo qua quy trinh, AI van phai giu HITL va khong duoc tu dong gui.

## Phase 5 - Evaluate

### AI Readiness Checklist

| Cau hoi | Trang thai | Ghi chu |
|---|---|---|
| Co du du lieu mau/logs sach de test? | Co mot phan | Co the lay log GPS, pin, cuoc goi va trang thai tram sac tu he thong dieu van; can an danh hoa truoc khi training/eval. |
| Rui ro khi AI sai co nam trong tam kiem soat? | Co | HITL bat buoc, AI chi tao draft; rule pin duoi 5% duoc xu ly bang guardrail. |
| Stakeholders san sang thay doi workflow? | Co dieu kien | Dieu phoi vien se chap nhan neu UI giup giam thoi gian va van cho phep sua truoc khi gui. |

### Quyet dinh cuoi cung

[x] **GO - Bat dau xay dung prototype voi scope hep**

### Justification

Quyet dinh GO vi bai toan co workflow ro, tan suat cao, metric do duoc va ranh gioi an toan cu the. Giai phap khong trao quyen tu dong cho AI ma chi dung LLM nhu mot co-pilot tao draft. Rule guardrail xu ly truong hop nguy kich pin duoi 5%, con dieu phoi vien van la nguoi phe duyet cuoi cung.

Uoc tinh chi phi ban dau thap vi moi request chi gom thong tin ngan: vi tri, pin, dong xe, 3-5 tram sac gan nhat va output draft. Gia dinh 80 su co/ngay, moi su co 1.000-1.500 token, tong token/ngay khoang 120.000 token. Voi Gemini Flash, chi phi API du kien rat nho so voi 16 gio dieu phoi co the tiet kiem moi ngay.

## Ket luan

Diem can xay dung tiep theo la dashboard noi bo cho dieu phoi vien:

- Hien data xe va tram sac theo thoi gian thuc.
- Nut tao draft AI.
- Nut duyet/gui rieng biet.
- Log lai output AI, nguoi duyet, thoi gian xu ly va ket qua thuc te.
