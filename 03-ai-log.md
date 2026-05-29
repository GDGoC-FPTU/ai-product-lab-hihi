# 03 - AI Log va Reflection

## Toi da dung AI de lam gi?

Trong Lab 2, toi dung AI nhu mot thought-partner de brainstorm cac pain point van hanh trong he sinh thai Vingroup, dac biet la Xanh SM, VinFast, Vinhomes va Vinmec. AI giup toi mo rong danh sach bai toan ban dau, sau do toi loc lai theo cac tieu chi: workflow co lap lai khong, co bottleneck do duoc khong, co metric thanh cong ro khong, va co ranh gioi van hanh de kiem soat rui ro khong.

Toi cung dung AI de ho tro viet problem statement 6-field, chuyen workflow thu cong thanh future-state flow, va kiem tra xem giai phap nen la Rule, LLM Feature hay Agentic Loop. Phan huu ich nhat la AI co the dong vai CFO/Operations Lead de phan bien: "vi sao bai toan nay co the khong can AI?" Nho do toi tranh duoc viec chon mot y tuong qua mo ho chi vi nghe co ve hay.

## AI da sai hoac chua tot o dau?

AI co xu huong de xuat giai phap qua manh, vi du de agent tu dong dieu xe cuu ho, tu dong gui tin nhan cho tai xe, hoac tu dong cap nhat trang thai cuoc xe. Nhung trong boi canh van hanh xe dien ngoai duong, viec tu dong hoa qua muc co the gay rui ro an toan va rui ro trach nhiem neu AI de xuat sai tram sac.

Mot diem chua tot khac la AI ban dau de xuat metric kha chung chung nhu "tang trai nghiem khach hang" hoac "giam thoi gian xu ly". Toi phai ep AI dua ra con so cu the, vi bai lab yeu cau metric do duoc. Sau khi chinh prompt, metric tot hon: giam thoi gian xu ly tu 15 phut xuong duoi 3 phut, 100% output co `[DRAFT_ONLY]`, va khong co de xuat tram sac xa hon 5km khi pin duoi 5%.

## Toi da sua prompt va ranh gioi nhu the nao?

Toi bo sung cac ranh gioi van hanh cu the vao system prompt:

- AI chi la co-pilot cho dieu phoi vien, khong phai nguoi ra quyet dinh cuoi.
- Moi output phai bat dau bang `[DRAFT_ONLY]`.
- AI khong duoc tu dong gui tin nhan hoac goi xe cuu ho neu chua co nguoi duyet.
- Neu pin duoi 5%, AI khong duoc de xuat tram sac xa hon 5km.
- Trong truong hop pin nguy kich, output phai chuyen sang action `dispatch_mobile_charger`.

Toi cung them adversarial tests de thu cac cach user co the lam AI vuot ranh gioi, vi du yeu cau bo tag `[DRAFT_ONLY]`, yeu cau gui thang tin nhan, hoac ep AI chi duong den tram sac 8km khi pin chi con 2%. Cach test nay giup toi thay prompt khong chi can "hay viet hay", ma phai co cau truc phong thu ro rang.

## Dieu toi hoc duoc

Bai hoc lon nhat la AI Product Scoping khong bat dau bang model, ma bat dau bang workflow. Neu khong hieu actor, bottleneck, metric va ranh gioi van hanh, giai phap AI rat de tro thanh demo dep nhung kho dua vao san xuat.

Toi cung hoc duoc rang LLM nen duoc dat vao vai tro phu hop. Voi bai toan Xanh SM nay, LLM khong nen lam agent tu dong dieu phoi, ma nen la LLM Feature tao draft duoi su kiem soat cua dieu phoi vien. Phan rule-based van rat quan trong de bao ve cac dieu kien an toan nhu nguong pin duoi 5%.
