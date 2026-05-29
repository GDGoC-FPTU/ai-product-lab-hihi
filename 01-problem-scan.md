# 01 - Problem Scan

## Thong tin ca nhan

- Ho ten: Le Duy Hung
- Ma so sinh vien: 2A202600718
- Vai tro trong lab: AI Product Engineer tai Vin Smart Future
- Chu de uu tien: Van hanh xe dien thong minh cho Xanh SM va VinFast

## Phase 1 - Scan: Bang quet co hoi AI

| # | Subsidiary | Lens | Mo ta ngan bai toan |
|---|---|---|---|
| 1 | Xanh SM | Ton thoi gian | Dieu phoi vien xu ly thu cong su co pin thap cua tai xe: nghe dien thoai, tra GPS, tim tram sac phu hop, soan tin nhan chi duong. |
| 2 | VinFast | Lap lai | Doi chieu hoa don sac dien tu cac tram doi tac voi log sac noi bo de tim sai lech ve thoi gian, cong suat va ma giao dich. |
| 3 | Vinhomes | AI-upgrade | Phan loai phan anh cu dan tren app Vinhomes Resident con cham, nhieu ticket bi route sai bo phan xu ly. |
| 4 | Vinmec | Ton thoi gian | Bac si va dieu duong mat nhieu thoi gian soan tom tat ho so xuat vien bang ngon ngu de hieu cho benh nhan. |
| 5 | Vinpearl | Stakeholder Pain | Quan ly khach san phai doc thu cong review tren Google/Agoda/Booking de phat hien phan nan khan cap ve phong, thai do nhan vien, do an. |
| 6 | Xanh SM | Stakeholder Pain | Tai xe phan nan diem don khach tren ban do khong khop mo ta thuc te, lam tang thoi gian tim khach va ti le huy chuyen. |

## Phase 2 - Quick Assess: Top 3 Problem Cards

### Quick Problem Card #1 - Xanh SM xu ly su co pin thap thuc dia

```text
QUICK PROBLEM CARD #1

Bai toan:
Dieu phoi vien Xanh SM can xu ly nhanh tinh huong tai xe bao pin thap/gan het pin khi dang tren duong don khach.

Cong ty thanh vien:
[x] Xanh SM

Ai dang dau?
- Tai xe: dang o ngoai duong, can huong dan ngay de khong bi can pin.
- Dieu phoi vien: phai tra nhieu dashboard va soan tin nhan thu cong.
- Khach hang: co nguy co bi tre/huy chuyen.

Workflow thu cong hien tai:
1. Tai xe goi/tro chuyen voi tong dai bao pin thap.
2. Dieu phoi vien tra bien so va toa do GPS xe.
3. Dieu phoi vien mo dashboard tram sac VinFast de tim tram gan va con tru.
4. Dieu phoi vien soan tin nhan chi duong cho tai xe.
5. Neu pin qua thap, dieu phoi vien goi doi cuu ho sac pin di dong.

Buoc ton thoi gian/loi nhat:
Buoc 3-4, khoang 10-12 phut/luot, de sai vi phai so khop vi tri, khoang cach, loai xe va trang thai tru sac.

AI co the ho tro o buoc nao?
Buoc 3-4: tong hop thong tin xe, pin, toa do, tram sac va draft tin nhan huong dan cho dieu phoi vien duyet.

Metric thanh cong:
Giam thoi gian xu ly su co tu 15 phut xuong duoi 3 phut/luot; 98% draft dung quy tac an toan pin.

Quick Architecture:
[ ] No AI  [ ] Rule  [x] LLM  [ ] Agent
```

### Quick Problem Card #2 - Vinhomes phan loai phan anh cu dan

```text
QUICK PROBLEM CARD #2

Bai toan:
Phan anh cu dan tren app Vinhomes Resident can duoc phan loai va route den dung bo phan trong thoi gian ngan.

Cong ty thanh vien:
[x] Vinhomes

Ai dang dau?
- Cu dan: doi phan hoi lau.
- Ban quan ly toa nha: nhan ticket khong dung chuyen mon.
- Tong dai CSKH: phai doc va route thu cong.

Workflow thu cong hien tai:
1. Cu dan gui phan anh bang text/anh tren app.
2. CSKH doc noi dung va xac dinh loai van de.
3. CSKH chuyen ticket sang ky thuat, ve sinh, an ninh hoac ke toan.
4. Bo phan tiep nhan kiem tra lai thong tin.
5. CSKH cap nhat trang thai cho cu dan.

Buoc ton thoi gian/loi nhat:
Buoc 2-3, khoang 8-10 phut/ticket, de route sai khi noi dung mo ho.

AI co the ho tro o buoc nao?
Buoc 2: LLM phan loai noi dung, trich xuat toa nha/can ho/muc do khan cap, de xuat bo phan nhan.

Metric thanh cong:
85% ticket duoc phan loai trong duoi 10 giay; ti le route sai giam xuong duoi 5%.

Quick Architecture:
[ ] No AI  [x] Rule + LLM  [ ] Agent
```

### Quick Problem Card #3 - Vinmec tom tat ho so xuat vien

```text
QUICK PROBLEM CARD #3

Bai toan:
Bac si Vinmec mat nhieu thoi gian viet ban tom tat xuat vien de benh nhan hieu duoc tinh trang, don thuoc va lich tai kham.

Cong ty thanh vien:
[x] Vinmec

Ai dang dau?
- Bac si: qua tai viec hanh chinh sau kham.
- Benh nhan: can huong dan ro rang bang ngon ngu de hieu.
- Dieu duong: phai giai thich lai neu ban tom tat qua ky thuat.

Workflow thu cong hien tai:
1. Bac si xem benh an dien tu, xet nghiem va chan doan.
2. Bac si tong hop ket qua dieu tri.
3. Bac si viet huong dan dung thuoc, dau hieu can quay lai, lich tai kham.
4. Dieu duong in va giai thich cho benh nhan.

Buoc ton thoi gian/loi nhat:
Buoc 2-3, khoang 20-30 phut/benh nhan, de thieu thong tin neu bac si qua tai.

AI co the ho tro o buoc nao?
Buoc 2-3: LLM draft ban tom tat de bac si review va chinh sua.

Metric thanh cong:
Giam thoi gian soan tom tat tu 25 phut xuong duoi 8 phut; 100% ban nhap phai duoc bac si duyet truoc khi in.

Quick Architecture:
[ ] No AI  [ ] Rule  [x] LLM with HITL  [ ] Agent
```

## Lua chon de deep-dive

Toi chon **Quick Problem Card #1 - Xanh SM xu ly su co pin thap thuc dia** de phan tich sau vi:

- Tac vu co workflow ro, lap lai nhieu lan moi ngay.
- Co metric do thanh cong cu the ve thoi gian xu ly va do an toan.
- LLM phu hop de tong hop thong tin va draft tin nhan, nhung van co Human-in-the-loop de giam rui ro.
- Ranh gioi van hanh ro: pin duoi 5% thi khong duoc de xuat tram sac xa hon 5km, phai dieu xe sac pin di dong.
