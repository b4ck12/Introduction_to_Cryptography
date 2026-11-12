# BỘ ĐỀ THI VÀ LỜI GIẢI CHI TIẾT MÔN NHẬP MÔN MẬT MÃ HỌC (INTRODUCTION TO CRYPTOGRAPHY)

**Mã học phần:** ICT3.001 / ICT3.08E  
**Đơn vị đào tạo:** Khoa Công nghệ Thông tin và Truyền thông – Trường Đại học Khoa học và Công nghệ Hà Nội (USTH)  
**Giảng viên giảng dạy & ra đề:** ThS. Nguyễn Minh Hướng  
**Sinh viên thực hiện:** Mã SV: `23BA14056`  
- **3 chữ số cuối mã sinh viên:** `056`  
- **Giá trị số nguyên đại diện:** $x = a = M = \mathbf{56}$  

---

## MỤC LỤC ĐIỀU HƯỚNG

- [PHẦN I: TỔNG HỢP MA TRẬN ĐỀ THI CUỐI KỲ](#phan-i-tong-hop-ma-tran-e-thi-cuoi-ky)
- [PHẦN II: ĐỀ THI SỐ 1 – HỌC KỲ 2, NĂM HỌC 2025–2026 (75 PHÚT)](#phan-ii-e-thi-so-1-hoc-ky-2-nam-hoc-20252026-75-phut)
  - [BÀI 1: TRA CỨU HỘP S-BOX $S_1$ TRONG DES (3/20 ĐIỂM)](#bai-1-tra-cuu-hop-s-box-s1-trong-des-320-iem)
  - [BÀI 2: HỆ THỐNG PKI, CHỮ KÝ CA & MÃ HÓA RSA (9/20 ĐIỂM)](#bai-2-he-thong-pki-chu-ky-ca-ma-hoa-rsa-920-iem)
    - [2.1 TẠO KHÓA RSA CHO NGƯỜI DÙNG A (3/20 ĐIỂM)](#21-tao-khoa-rsa-cho-nguoi-dung-a-320-iem)
    - [2.2 CẤP CHỨNG CHỈ SỐ BẰNG CHỮ KÝ ELGAMAL CỦA CA (3/20 ĐIỂM)](#22-cap-chung-chi-so-bang-chu-ky-elgamal-cua-ca-320-iem)
    - [2.3 MÃ HÓA VÀ GIẢI MÃ THÔNG ĐIỆP M = 20260 (3/20 ĐIỂM)](#23-ma-hoa-va-giai-ma-thong-iep-voi-ma-sv-056-320-iem)
  - [BÀI 3: QUÁ TRÌNH ĐỆM (PADDING PREPROCESS) CỦA HÀM BĂM SHA-1 (4/20 ĐIỂM)](#bai-3-qua-trinh-em-padding-preprocess-cua-ham-bam-sha-1-420-iem)
  - [BÀI 4: GIAO THỨC TRAO ĐỔI KHÓA DIFFIE-HELLMAN - DHKE (4/20 ĐIỂM)](#bai-4-giao-thuc-trao-oi-khoa-diffie-hellman-dhke-420-iem)
    - [2.1 Lời giải theo Biến thể A: $p = 27361, \alpha = 6$ (Đề thi in trên giấy)](#21-loi-giai-theo-bien-the-a-p-27361-alpha-6-e-thi-in-tren-giay)
    - [2.2 Lời giải theo Biến thể B: $p = 51907, \alpha = 6$ (Đề chiếu lớp học)](#22-loi-giai-theo-bien-the-b-p-51907-alpha-6-e-chieu-lop-hoc)
- [PHẦN III: ĐỀ THI SỐ 2 – HỌC KỲ 2, NĂM HỌC 2024–2025 (60 PHÚT)](#phan-iii-e-thi-so-2-hoc-ky-2-nam-hoc-20242025-60-phut)
  - [BÀI 1.1: TẠO KHÓA RSA ($p = 223, q = 193$) (4/20 ĐIỂM)](#bai-11-tao-khoa-rsa-p-223-q-193-420-iem)
  - [BÀI 1.2: CHỨNG CHỈ SỐ RSA CỦA CA CHO MÃ SV 056 (4/20 ĐIỂM)](#bai-12-chung-chi-so-rsa-cua-ca-cho-ma-sv-056-420-iem)
  - [BÀI 1.3: QUY TRÌNH TRAO ĐỔI EMAIL BẢO MẬT PKI (4/20 ĐIỂM)](#bai-13-quy-trinh-trao-oi-email-bao-mat-pki-420-iem)
- [PHẦN IV: ĐỀ THI SỐ 3 – HỌC KỲ 2, NĂM HỌC 2023–2024 (THỨ NĂM, 30/11/2023 - 75 PHÚT)](#phan-iv-e-thi-so-3-hoc-ky-2-nam-hoc-20232024-75-phut)
  - [CÂU 0: CÂU HỎI QUAN TRỌNG: TRA CỨU HỘP S-BOX DES VÀ CHỌN ĐỀ THI (3/20 ĐIỂM)](#cau-0-cau-hoi-quan-trong-tra-cuu-hop-s-box-des-va-chon-e-thi-320-iem)
  - [QUESTION SET 01 (LỜI GIẢI ĐỀ CHÍNH THỨC CHO S-BOX LẺ)](#question-set-01-loi-giai-e-chinh-thuc-cho-s-box-le)
    - [BÀI 1: HÀM BĂM SHA-1 PADDING (l = 2096 BITS) & SƠ ĐỒ KHỐI DAVIES-MEYER (4/20 ĐIỂM)](#set-01-bai-1-ham-bam-sha-1-padding-so-do-khoi-420-iem)
    - [BÀI 2: TRAO ĐỔI KHÓA DIFFIE-HELLMAN (p = 863, alpha = 2) (4/20 ĐIỂM)](#set-01-bai-2-trao-doi-khoa-diffie-hellman-420-iem)
    - [BÀI 3: HỆ THỐNG CHỮ KÝ SỐ ELGAMAL & CHỨNG CHỈ CA (9/20 ĐIỂM)](#set-01-bai-3-he-thong-chu-ky-so-elgamal-va-chung-chi-ca-920-iem)
  - [QUESTION SET 02 (LỜI GIẢI ĐỀ MỞ RỘNG CHO S-BOX CHẴN)](#question-set-02-loi-giai-e-mo-rong-cho-s-box-chan)
    - [BÀI 1: HÀM BĂM SHA-1 PADDING (l = 2225 BITS) & SƠ ĐỒ KHỐI (4/20 ĐIỂM)](#set-02-bai-1-ham-bam-sha-1-padding-so-do-khoi-420-iem)
    - [BÀI 2: TRAO ĐỔI KHÓA DIFFIE-HELLMAN (p = 593, alpha = 2) (4/20 ĐIỂM)](#set-02-bai-2-trao-doi-khoa-diffie-hellman-420-iem)
    - [BÀI 3: HỆ THỐNG CHỮ KÝ SỐ ELGAMAL & CHỨNG CHỈ CA (9/20 ĐIỂM)](#set-02-bai-3-he-thong-chu-ky-so-elgamal-va-chung-chi-ca-920-iem)
- [PHẦN V: CẨM NANG PHƯƠNG PHÁP TÍNH NHANH TRONG PHÒNG THI](#phan-v-cam-nang-phuong-phap-tinh-nhanh-trong-phong-thi)
  - [1. Thuật toán Euclid mở rộng tính nghịch đảo modulo $a^{-1} \pmod m$](#1-thuat-toan-euclid-mo-rong-tinh-nghich-ao-modulo-a-1-pmod-m)
  - [2. Bảng Tóm Tắt Đáp Số Cho Mã Sinh Viên 23BA14056](#2-bang-tom-tat-ap-so-cho-ma-sinh-vien-23ba14056)
  - [3. Danh Mục Các Thuật Toán Mật Mã Lập Trình Chuẩn Trong Thư Mục `code/`](#3-danh-muc-cac-thuat-toan-mat-ma-lap-trinh-chuan-trong-thu-muc-code)

---

<a id="phan-i-tong-hop-ma-tran-e-thi-cuoi-ky"></a>
# PHẦN I: TỔNG HỢP MA TRẬN ĐỀ THI CUỐI KỲ

| Dạng Bài Tập | Xuất Hiện Tại | Trọng Số | Kỹ Năng Cần Nhớ |
| :--- | :--- | :---: | :--- |
| **Tra cứu S-Box DES** | Đề 2025–2026 (Bài 1) | 3/20 | $x = \text{Mã\_SV} \pmod{64} \to$ đổi ra 6 bit $\to$ bit ngoài cùng ra Hàng, 4 bit trong ra Cột. |
| **Thiết lập khóa RSA** | Đề 2024–2025 & 2025–2026 | 3–4/20 | Tính $\Phi(n) = (p-1)(q-1)$, phân tích ước nguyên tố, chọn $e$ sao cho $\gcd(e, \Phi(n)) = 1$, tính $d = e^{-1}$. |
| **Cấp chứng chỉ CA (RSA / ElGamal)** | Đề 2024–2025 & 2025–2026 | 3–4/20 | Ký số trên định danh người dùng: $S = M^{d_{\text{CA}}} \pmod{N_{\text{CA}}}$ hoặc chữ ký cặp $(r, s)$. |
| **Mã hóa / Giải mã RSA** | Đề 2025–2026 (Bài 2.3) | 3/20 | $C \equiv M^e \pmod N$, $M \equiv C^d \pmod N$. |
| **Tiền xử lý đệm SHA-1** | Đề 2025–2026 (Bài 3) | 4/20 | Nối bit 1 $\to$ các bit 0 $\to$ 64 bit chiều dài gốc $l$, sao cho tổng chia hết cho 512 bit. |
| **Trao đổi khóa Diffie-Hellman** | Đề 2025–2026 (Bài 4 / Biến thể) | 4/20 | $k_A = \alpha^a \pmod p$, $k_B = \alpha^b \pmod p$, $k_{AB} = \alpha^{ab} \pmod p$. |

---

<a id="phan-ii-e-thi-so-1-hoc-ky-2-nam-hoc-20252026-75-phut"></a>
# PHẦN II: ĐỀ THI SỐ 1 – HỌC KỲ 2, NĂM HỌC 2025–2026 (75 PHÚT)
*(Trích từ đề thi thật: [`888777526...png`](888777526_1694674142364538_6916016118903342853_n.png) & [`869026595...png`](869026595_1912712470101456_972023757049859571_n.png))*

<a id="bai-1-tra-cuu-hop-s-box-s1-trong-des-320-iem"></a>
## BÀI 1: TRA CỨU HỘP S-BOX $S_1$ TRONG DES (3/20 ĐIỂM)

> [!TIP]
> **File code giải bài toán:** [`code/des_sbox_lookup.py`](code/des_sbox_lookup.py)  
> *Lệnh chạy terminal:* `python code/des_sbox_lookup.py`

<a id="1-e-bai"></a>
### 1. Đề bài
1. Xác định số nguyên $x$ từ 3 chữ số cuối trong mã sinh viên:
   $$x = (\text{your\_student\_ID}) \pmod{64}$$
2. Tính đầu ra của hộp $S_1$ trong chuẩn DES với đầu vào là biểu diễn nhị phân của số $x$.

**Bảng tra cứu hộp $S_1$ cho trong đề:**
```
       Cột: 0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
Hàng 0:    14  04  13  01  02  15  11  08  03  10  06  12  05  09  00  07
Hàng 1:    00  15  07  04  14  02  13  01  10  06  12  11  09  05  03  08
Hàng 2:    04  01  14  08  13  06  02  11  15  12  09  07  03  10  05  00
Hàng 3:    15  12  08  02  04  09  01  07  05  11  03  14  10  00  06  13
```

<a id="2-loi-giai-chi-tiet-cho-ma-sinh-vien-23ba14056"></a>
### 2. Lời giải chi tiết cho Mã sinh viên 23BA14056
- **Bước 1: Tính giá trị $x$**  
  Mã SV là `23BA14056`, 3 chữ số cuối là `056` (số nguyên 56):
  $$x = 56 \pmod{64} = \mathbf{56}$$
- **Bước 2: Đổi sang nhị phân 6 bit**  
  $$56_{10} = 32 + 16 + 8 = \mathbf{(111000)_2} = (b_1 b_2 b_3 b_4 b_5 b_6)$$
- **Bước 3: Xác định Hàng và Cột**  
  - **Hàng $r$** (ghép bit ngoài cùng $b_1 b_6$):
    $$r = (b_1 b_6)_2 = (10)_2 = 1 \cdot 2^1 + 0 \cdot 2^0 = \mathbf{2} \quad \text{(Hàng 2)}$$
  - **Cột $c$** (ghép 4 bit ở giữa $b_2 b_3 b_4 b_5$):
    $$c = (b_2 b_3 b_4 b_5)_2 = (1100)_2 = 1 \cdot 8 + 1 \cdot 4 + 0 \cdot 2 + 0 \cdot 1 = \mathbf{12} \quad \text{(Cột 12)}$$
- **Bước 4: Tra bảng $S_1$ tại (Hàng 2, Cột 12)**  
  Dòng Hàng 2:
  `04  01  14  08  13  06  02  11  15  12  09  07  [03]  10  05  00`  
  Giá trị thập phân tại Cột 12 là $\mathbf{3}$ (hoặc `03`).
- **Bước 5: Đầu ra nhị phân 4 bit**  
  $$3_{10} = \mathbf{(0011)_2}$$

> **Đáp số Bài 1:** Đầu ra hộp $S_1$ là $\mathbf{3}$ (nhị phân: $\mathbf{0011_2}$).

---

<a id="bai-2-he-thong-pki-chu-ky-ca-ma-hoa-rsa-920-iem"></a>
## BÀI 2: HỆ THỐNG PKI, CHỮ KÝ CA & MÃ HÓA RSA (9/20 ĐIỂM)

<a id="21-tao-khoa-rsa-cho-nguoi-dung-a-320-iem"></a>
### 2.1 TẠO KHÓA RSA CHO NGƯỜI DÙNG A (3/20 ĐIỂM)

> [!TIP]
> **File code giải bài toán:** [`code/rsa_key_generation.py`](code/rsa_key_generation.py)  
> *Lệnh chạy terminal:* `python code/rsa_key_generation.py`

<a id="1-e-bai-1"></a>
#### 1. Đề bài
Người dùng A thiết lập hệ mật RSA với các tham số: $p = 139, q = 227$.  
a. Giải thích và chọn số mũ công khai $e$ thích hợp từ tập $\{122; 123; 124; 125\}$.  
b. Tính khóa riêng $d_A$ của người dùng A.

<a id="2-loi-giai-chi-tiet"></a>
#### 2. Lời giải chi tiết
1. **Tính Modulus $N_A$:**
   $$N_A = p \times q = 139 \times 227 = \mathbf{31553}$$
2. **Tính Hàm Phi Euler $\Phi(N_A)$:**
   $$\Phi(N_A) = (p - 1)(q - 1) = 138 \times 226 = \mathbf{31188}$$
3. **Phân tích thừa số nguyên tố của $\Phi(N_A)$:**
   $$\Phi(N_A) = 31188 = 2^2 \times 3 \times 23 \times 113$$
   Tập các ước nguyên tố: $\mathcal{P} = \{2, 3, 23, 113\}$.
4. **Kiểm tra điều kiện nguyên tố cùng nhau $\gcd(e, \Phi(N_A)) = 1$:**
   - $e = 122$: Số chẵn $\implies \gcd(122, 31188) \ge 2 \ne 1$ (Loại).
   - $e = 123$: Tổng các chữ số $1+2+3 = 6$ chia hết cho 3 $\implies \gcd(123, 31188) \ge 3 \ne 1$ (Loại).
   - $e = 124$: Số chẵn $\implies \gcd(124, 31188) \ge 4 \ne 1$ (Loại).
   - $e = 125 = 5^3$: Số nguyên tố 5 không chia hết 31188 $\implies \gcd(125, 31188) = \mathbf{1}$ (**Chấp nhận**).
   - Chọn số mũ công khai: $\mathbf{e_A = 125}$.
5. **Tính khóa riêng $d_A$ bằng thuật toán Euclid mở rộng:**
   Giải $125 \cdot d_A \equiv 1 \pmod{31188}$:
   $$d_A \equiv 125^{-1} \pmod{31188} = \mathbf{30689}$$
   *Kiểm tra lại:* $125 \times 30689 = 3836125 = 123 \times 31188 + 1 \equiv 1 \pmod{31188}$.

> **Đáp số Bài 2.1:**  
> - Cặp khóa công khai: $k_{\text{pub}, A} = (N_A, e_A) = \mathbf{(31553, 125)}$.  
> - Khóa bí mật: $k_{\text{pri}, A} = (d_A) = \mathbf{30689}$.

---

<a id="22-cap-chung-chi-so-bang-chu-ky-elgamal-cua-ca-320-iem"></a>
### 2.2 CẤP CHỨNG CHỈ SỐ BẰNG CHỮ KÝ ELGAMAL CỦA CA (3/20 ĐIỂM)

> [!TIP]
> **File code giải bài toán:** [`code/elgamal_digital_signature.py`](code/elgamal_digital_signature.py)  
> *Lệnh chạy terminal:* `python code/elgamal_digital_signature.py`

<a id="1-e-bai-2"></a>
#### 1. Đề bài
Cơ quan chứng thực CA có các tham số: $p_{\text{CA}} = 997, \alpha = 6, d_{\text{CA}} = 25$.  
CA tính thông điệp liên kết: $x_A = x + e_A$ (với $x$ từ Bài 1 và $e_A$ từ Bài 2.1). Khóa tạm thời $k_E = 185$ *(Lưu ý: trên bản in photo mờ, số 185 có nét cong số 8 dễ bị nhìn nhầm thành số 0 tức 105; xem phân tích bẫy toán học ở mục ghi chú bên dưới)*.  
a. Giải thích và tính chứng chỉ số $\text{Cert}_A = (x_A, (r, s))$.  
b. Trình bày cách người dùng B xác minh chứng chỉ.

<a id="2-loi-giai-chi-tiet-cho-ma-sinh-vien-23ba14056-1"></a>
#### 2. Lời giải chi tiết cho Mã sinh viên 23BA14056
1. **Tính khóa công khai $\beta$ của CA:**
   $$\beta = \alpha^{d_{\text{CA}}} \pmod{p_{\text{CA}}} = 6^{25} \pmod{997} = \mathbf{333}$$
   $k_{\text{pub}, \text{CA}} = (997, 6, 333)$.
2. **Xác định thông điệp liên kết $x_A$:**
   $$x_A = x + e_A = 56 + 125 = \mathbf{181}$$
3. **Kiểm tra điều kiện khóa tạm thời $k_E = 185$:**
   $$\gcd(k_E, p_{\text{CA}} - 1) = \gcd(185, 996) = \mathbf{1}$$
   Vì $\gcd(185, 996) = 1$, $k_E = 185$ nguyên tố cùng nhau với $p_{\text{CA}} - 1$, thỏa mãn tuyệt đối điều kiện sinh chữ ký số ElGamal.
4. **Tính thành phần chữ ký $r$:**
   $$r \equiv \alpha^{k_E} \pmod{p_{\text{CA}}} = 6^{185} \pmod{997} = \mathbf{591}$$
5. **Tìm nghịch đảo $k_E^{-1} \pmod{996}$ bằng thuật toán Euclid mở rộng:**
   Bảng thực thi từng bước giải $185 \cdot k_E^{-1} \equiv 1 \pmod{996}$:
   - $996 = 5 \times 185 + 71$
   - $185 = 2 \times 71 + 43$
   - $71 = 1 \times 43 + 28$
   - $43 = 1 \times 28 + 15$
   - $28 = 1 \times 15 + 13$
   - $15 = 1 \times 13 + 2$
   - $13 = 6 \times 2 + 1$
   - $2 = 2 \times 1 + 0$
   
   Truy ngược hệ số Bézout thu được:
   $$k_E^{-1} = 185^{-1} \pmod{996} = \mathbf{533}$$
   *(Kiểm tra: $185 \times 533 = 98605 = 99 \times 996 + 1 \equiv 1 \pmod{996}$)*.
6. **Tính thành phần chữ ký $s$:**
   Công thức đồng dư:
   $$s \equiv (x_A - d_{\text{CA}} \cdot r) \cdot k_E^{-1} \pmod{p_{\text{CA}} - 1}$$
   - $d_{\text{CA}} \cdot r = 25 \times 591 = \mathbf{14775}$
   - $x_A - d_{\text{CA}} \cdot r = 181 - 14775 = -14594$
   - $(-14594) \pmod{996} = \mathbf{346}$
   - $s \equiv (346 \times 533) \pmod{996} = 184418 \pmod{996} = \mathbf{158}$

   > **Cặp chữ ký số của CA:** $(r, s) = \mathbf{(591, 158)}$  
   > **Chứng chỉ số do CA cấp:** $\text{Cert}_A = (x_A = 181, (r = 591, s = 158))$

7. **Xác minh chữ ký của Người dùng B:**
   Người dùng B nhận được $\text{Cert}_A = (181, (591, 158))$ và khóa công khai CA $k_{\text{pub}, \text{CA}} = (997, 6, 333)$:
   - Tính vế trái $v_1$:
     $$v_1 \equiv \beta^r \cdot r^s \pmod{p_{\text{CA}}} = 333^{591} \times 591^{158} \pmod{997}$$
     $$333^{591} \pmod{997} = 991, \quad 591^{158} \pmod{997} = 985$$
     $$v_1 = (991 \times 985) \pmod{997} = 976135 \pmod{997} = \mathbf{72}$$
   - Tính vế phải $v_2$:
     $$v_2 \equiv \alpha^{x_A} \pmod{p_{\text{CA}}} = 6^{181} \pmod{997} = \mathbf{72}$$
   - So sánh: $v_1 \equiv v_2 \equiv \mathbf{72} \pmod{997}$.
   - **Kết luận:** Chứng chỉ số $\text{Cert}_A$ được xác minh **hoàn toàn hợp lệ và nguyên vẹn**.

8. **Ghi chú phân tích bẫy / trường hợp nhìn nhầm $k_E = 105$:**
   - Nếu đọc đề là $k_E = 105$: $\gcd(105, 996) = 3 \ne 1$.
   - Phương trình đồng dư $105 \cdot s \equiv (181 - 25 \times 539) \equiv 650 \pmod{996}$.
   - Vì $\gcd(105, 996) = 3$ không chia hết cho $650$ ($650 = 3 \times 216 + 2$), phương trình này **vô nghiệm $s$**.
   - Nếu trong phòng thi gặp đề ghi 105, thí sinh chỉ ra $\gcd(105, 996) = 3 \ne 1$ nên phương trình vô nghiệm, và đề chuẩn là $k_E = 185$ để đạt điểm tuyệt đối 3/3 điểm.

---

<a id="23-ma-hoa-va-giai-ma-thong-iep-voi-ma-sv-056-320-iem"></a>
### 2.3 MÃ HÓA VÀ GIẢI MÃ THÔNG ĐIỆP M = 20260 (3/20 ĐIỂM)

> [!TIP]
> **File code giải bài toán:** [`code/rsa_encryption_decryption.py`](code/rsa_encryption_decryption.py)  
> *Lệnh chạy terminal:* `python code/rsa_encryption_decryption.py 20260`

<a id="1-e-bai-3"></a>
#### 1. Đề bài (Trích nguyên văn đề thi in chính thức)
> *"User A starts exchanging message, $M = 20260$, with user B using the certificated keypair. Explain the encryption and decryption done by user A and user B."*

Sử dụng cặp khóa RSA của người dùng A đã được cấp chứng chỉ ở Bài 2.1 và 2.2:
- Modulus: $N_A = 31553$
- Khóa công khai: $e_A = 125$
- Khóa bí mật: $d_A = 30689$
- Thông điệp trao đổi: $M = \mathbf{20260}$ (theo đề in chính thức; không phải mã sinh viên).

<a id="2-loi-giai-chi-tiet-1"></a>
#### 2. Lời giải chi tiết tự luận

##### Bước 1: Người dùng B mã hóa thông điệp gửi cho A (Encryption)
Để gửi thông điệp bảo mật $M = 20260$ cho người dùng A, B sử dụng khóa công khai của A ($N_A = 31553, e_A = 125$) đã được CA chứng thực:
$$C \equiv M^{e_A} \pmod{N_A} = 20260^{125} \pmod{31553}$$

Áp dụng thuật toán **Bình phương và Nhân (Square-and-Multiply)**:
- Số mũ $e_A = 125 = (1111101)_2$ (gồm 7 bit: $b_6 b_5 b_4 b_3 b_2 b_1 b_0$).
- Bảng vết lũy thừa nhanh từng bước:

| Vòng lặp $i$ | Bit $b_i$ | Phép toán thực hiện | Phép tính modulo $31553$ | Giá trị hiện tại $A$ |
| :---: | :---: | :--- | :--- | :---: |
| Khởi tạo | - | - | - | $1$ |
| $i = 6$ | **1** | Square & Multiply | $1^2 \times 20260 \pmod{31553}$ | **$20260$** |
| $i = 5$ | **1** | Square & Multiply | $(20260^2 \pmod{31553}) \times 20260 \pmod{31553}$ | **$14489$** |
| $i = 4$ | **1** | Square & Multiply | $(14489^2 \pmod{31553}) \times 20260 \pmod{31553}$ | **$17462$** |
| $i = 3$ | **1** | Square & Multiply | $(17462^2 \pmod{31553}) \times 20260 \pmod{31553}$ | **$4669$** |
| $i = 2$ | **1** | Square & Multiply | $(4669^2 \pmod{31553}) \times 20260 \pmod{31553}$ | **$27144$** |
| $i = 1$ | **0** | Square | $27144^2 \pmod{31553} = 736800136 \pmod{31553}$ | **$2633$** |
| $i = 0$ | **1** | Square & Multiply | $(2633^2 \pmod{31553}) \times 20260 \pmod{31553} = 22582 \times 20260 \pmod{31553}$ | **$24373$** |

$$C = \mathbf{24373}$$
Người dùng B truyền bản mã $C = 24373$ qua kênh truyền công khai cho A.

##### Bước 2: Người dùng A giải mã bản mã (Decryption)
Người dùng A nhận được bản mã $C = 24373$ và sử dụng khóa bí mật duy nhất của mình ($d_A = 30689$) để khôi phục bản rõ:
$$M \equiv C^{d_A} \pmod{N_A} = 24373^{30689} \pmod{31553}$$
Thực hiện lũy thừa nhanh:
$$M = \mathbf{20260}$$

Kiểm tra: Bản rõ khôi phục hoàn toàn trùng khớp với thông điệp ban đầu $M = 20260$. Quá trình mã hóa và giải mã RSA hoàn toàn chính xác.

> [!NOTE]
> **Phương án dự phòng (Nếu giám khảo yêu cầu thay $M$ bằng số nguyên từ Mã sinh viên $M = 56$):**  
> - Mã hóa: $C = 56^{125} \pmod{31553} = \mathbf{2365}$.  
> - Giải mã: $M = 2365^{30689} \pmod{31553} = \mathbf{56}$.  
> *(Cả hai kết quả $M=20260 \implies C=24373$ và $M=56 \implies C=2365$ đều được tích hợp sẵn trong script [`code/rsa_encryption_decryption.py`](code/rsa_encryption_decryption.py))*.

---

<a id="bai-3-qua-trinh-em-padding-preprocess-cua-ham-bam-sha-1-420-iem"></a>
## BÀI 3: QUÁ TRÌNH ĐỆM (PADDING PREPROCESS) CỦA HÀM BĂM SHA-1 (4/20 ĐIỂM)

> [!TIP]
> **File code giải bài toán:** [`code/sha1_padding_preprocess.py`](code/sha1_padding_preprocess.py)  
> *Lệnh chạy terminal:* `python code/sha1_padding_preprocess.py 20260`

<a id="1-e-bai-4"></a>
### 1. Đề bài (Trích nguyên văn đề thi)
> *"Suppose that SHA-1, a hash function, is used to hash a message of $M$ bits (from Exercise 1.3 - tức mục 2.3). Explain the prepocess (padding process) of the message and describe the format of the padded message before applying the compression function."*

Vì thông điệp ở mục 2.3 có giá trị $M = 20260$, chiều dài bit của thông điệp cần băm là $l = M = \mathbf{20260}$ bits.

<a id="2-loi-giai-chi-tiet-2"></a>
### 2. Lời giải chi tiết
1. **Quy tắc đệm chuẩn của SHA-1 (FIPS PUB 180-1):**
   - Giả sử thông điệp ban đầu có độ dài $l$ bits.
   - Thêm bit `1` vào ngay sau thông điệp gốc $\implies$ Chiều dài lúc này là $l + 1$ bits.
   - Thêm $k$ bit `0` ($0 \le k < 512$) sao cho:
     $$(l + 1 + k) \equiv 448 \pmod{512} \implies k = (447 - l) \pmod{512}$$
   - Nối thêm trường 64 bit biểu diễn độ dài gốc $l$ ở dạng số nguyên nhị phân không dấu (Big-endian).
   - Tổng độ dài sau khi đệm là bội số nguyên của 512 bit: $L \times 512$ bits.

2. **Áp dụng tính toán cụ thể cho thông điệp có độ dài $l = 20260$ bits:**
   - Phân tích số dư: $20260 = 39 \times 512 + 292 \implies 20260 \equiv 292 \pmod{512}$.
   - Chiều dài sau khi nối bit `1`: $20260 + 1 = 20261 \equiv 293 \pmod{512}$.
   - Số bit `0` cần chèn thêm:
     $$k = (448 - 293) = \mathbf{155 \text{ bit 0}}$$
   - Biểu diễn 64-bit của số $l = 20260_{10}$:
     - Giá trị Hexadecimal: $20260_{10} = \mathbf{\text{0x0000000000004F24}}$ (vì $4F24_{16} = 4 \times 4096 + 15 \times 256 + 2 \times 16 + 4 = 20260$).
     - Giá trị nhị phân 64-bit:
       $$\mathbf{00000000\ 00000000\ 00000000\ 00000000\ 00000000\ 00000000\ 01001111\ 00100100_2}$$
   - Tổng chiều dài thông điệp sau đệm:
     $$L = l + 1 + k + 64 = 20260 + 1 + 155 + 64 = \mathbf{20480} \quad \text{bits}$$
   - Số khối 512-bit đưa vào hàm nén:
     $$N = \frac{20480}{512} = \mathbf{40} \quad \text{khối } (M_1, M_2, \dots, M_{40})$$

3. **Mô tả định dạng các khối trước khi áp dụng hàm nén:**
   - **Khối $M_1$ đến $M_{39}$:** Mỗi khối chứa trọn vẹn 512 bit thông điệp gốc (tổng cộng $39 \times 512 = 19968$ bits).
   - **Khối $M_{40}$ (Khối cuối cùng, 512 bits):**
     - $292$ bit cuối cùng của thông điệp gốc ($20260 - 19968 = 292$ bits).
     - **1 bit `1`**.
     - **$155$ bit `0`**.
     - **64 bit trường độ dài gốc** ($l = 20260$).
     - Kiểm tra kích thước khối cuối: $292 + 1 + 155 + 64 = \mathbf{512}$ bits.

---

<a id="bai-4-giao-thuc-trao-oi-khoa-diffie-hellman-dhke-420-iem"></a>
## BÀI 4: GIAO THỨC TRAO ĐỔI KHÓA DIFFIE-HELLMAN - DHKE (4/20 ĐIỂM)

> [!TIP]
> **File code giải bài toán:** [`code/diffie_hellman_key_exchange.py`](code/diffie_hellman_key_exchange.py)  
> *Lệnh chạy terminal chuẩn:* `python code/diffie_hellman_key_exchange.py 27361 6 20260 24373`  
> *(Xem thêm mã nguồn mô phỏng tấn công MitM tại [`code/dhke_mitm_attack.py`](code/dhke_mitm_attack.py))*

<a id="1-e-bai-5"></a>
### 1. Đề bài (Trích nguyên văn đề thi)
> *"Diffie-Hellman Key Exchange (DHKE) is processed by Alice and Bob:  
> Explain how two users exchange and compute the two public keys, denoted as $k_A, k_B$ and the common key, denoted as $k_{AB}$, for the DHKE scheme with the parameters prime $p = 27361$, generator $\alpha = 6$, and the numbers that are chosen at each user to generate their public keys are:  
> $$a = M; \quad b = C$$  
> where $C$ denotes the ciphertext of message $M$ in Exercise 2.3."*

Căn cứ vào kết quả chính thức ở Bài 2.3 ($M = 20260 \implies C = 24373$):
- Alice chọn số bí mật: $a = M = \mathbf{20260}$.
- Bob chọn số bí mật: $b = C = \mathbf{24373}$.

---

<a id="2-loi-giai-chi-tiet-cho-ma-sv-23ba14056"></a>
### 2. Lời giải chi tiết tự luận (Trường hợp chính thức: $a = 20260, b = 24373$)

<a id="21-loi-giai-theo-bien-the-a-p-27361-alpha-6-e-thi-in-tren-giay"></a>
#### 2.1 Lời giải theo Biến thể A: $p = 27361, \alpha = 6$ (Đề thi in trên giấy)

##### Bước 1: Alice tạo và tính khóa công khai $k_A$
Alice tính khóa công khai của mình theo công thức:
$$k_A = \alpha^a \pmod p = 6^{20260} \pmod{27361}$$

*Rút gọn số mũ theo định lý Fermat nhỏ ($p - 1 = 27360$):*  
Vì $20260 < 27360$, ta thực hiện tính lũy thừa nhanh Square-and-Multiply:
$$k_A = \mathbf{12}$$
Alice truyền công khai $k_A = 12$ cho Bob qua mạng.

##### Bước 2: Bob tạo và tính khóa công khai $k_B$
Bob tính khóa công khai của mình:
$$k_B = \alpha^b \pmod p = 6^{24373} \pmod{27361}$$
Thực hiện tính lũy thừa nhanh:
$$k_B = \mathbf{3268}$$
Bob truyền công khai $k_B = 3268$ cho Alice.

##### Bước 3: Tính khóa phiên bí mật chung $k_{AB}$
- **Alice nhận $k_B = 3268$ và dùng số bí mật $a = 20260$ để tính:**
  $$k_{AB} = (k_B)^a \pmod p = 3268^{20260} \pmod{27361} = \mathbf{20184}$$
- **Bob nhận $k_A = 12$ và dùng số bí mật $b = 24373$ để tính:**
  $$k_{AB} = (k_A)^b \pmod p = 12^{24373} \pmod{27361} = \mathbf{20184}$$

**Kết luận:** $k_{AB}(\text{Alice}) == k_{AB}(\text{Bob}) == \mathbf{20184}$. Cả hai bên thiết lập thành công khóa phiên bí mật chung.

---

<a id="22-loi-giai-theo-bien-the-b-p-51907-alpha-6-e-chieu-lop-hoc"></a>
#### 2.2 Lời giải theo Biến thể B: $p = 51907, \alpha = 6$ (Đề chiếu lớp học)
- Khóa công khai của Alice:
  $$k_A = 6^{20260} \pmod{51907} = \mathbf{13196}$$
- Khóa công khai của Bob:
  $$k_B = 6^{24373} \pmod{51907} = \mathbf{25141}$$
- Khóa phiên bí mật chung:
  $$k_{AB} = 25141^{20260} \pmod{51907} = 13196^{24373} \pmod{51907} = \mathbf{22981}$$

---

### 3. Phương án dự phòng (Nếu tính theo $M = \text{Mã SV} = 56$ và $C = 2365$)
Nếu người chấm hiểu $M$ là mã sinh viên ($a = 56, b = C = 2365$):
- **Biến thể A ($p = 27361, \alpha = 6$):**
  - $k_A = 6^{56} \pmod{27361} = \mathbf{2474}$
  - $k_B = 6^{2365} \pmod{27361} = \mathbf{5253}$
  - $k_{AB} = 5253^{56} \equiv 2474^{2365} \pmod{27361} = \mathbf{15552}$
- **Biến thể B ($p = 51907, \alpha = 6$):**
  - $k_A = 6^{56} \pmod{51907} = \mathbf{3235}$
  - $k_B = 6^{2365} \pmod{51907} = \mathbf{20853}$
  - $k_{AB} = \mathbf{48191}$

---

<a id="phan-iii-e-thi-so-2-hoc-ky-2-nam-hoc-20242025-60-phut"></a>
# PHẦN III: ĐỀ THI SỐ 2 – HỌC KỲ 2, NĂM HỌC 2024–2025 (60 PHÚT)
*(Trích từ đề thi thật: [`889012961...png`](889012961_1149336604139458_2097881916641920719_n.png))*

<a id="bai-11-tao-khoa-rsa-p-223-q-193-420-iem"></a>
## BÀI 1.1: TẠO KHÓA RSA ($p = 223, q = 193$) (4/20 ĐIỂM)

> [!TIP]
> **File code giải toàn bộ Đề 2024–2025:** [`code/pki_rsa_certificate.py`](code/pki_rsa_certificate.py)  
> *Lệnh chạy terminal:* `python code/pki_rsa_certificate.py`

1. $N_A = 223 \times 193 = \mathbf{43039}$.
2. $\Phi(N_A) = 222 \times 192 = \mathbf{42624} = 2^7 \times 3^2 \times 37$.
3. Chọn $e$ từ tập $\{3525; 5525; 6525\}$:
   - $3525$ chia hết cho 3 ($\gcd = 3 \ne 1$).
   - $6525$ chia hết cho 9 ($\gcd = 9 \ne 1$).
   - $5525 = 5^2 \times 13 \times 17 \implies \gcd(5525, 42624) = \mathbf{1}$.
   - Chọn $\mathbf{e_A = 5525}$.
4. Tính khóa riêng $d_A$:
   $$d_A \equiv 5525^{-1} \pmod{42624} = \mathbf{26045}$$
5. Cặp khóa: $k_{\text{pub}, A} = (43039, 5525), k_{\text{pri}, A} = (26045)$.

---

<a id="bai-12-chung-chi-so-rsa-cua-ca-cho-ma-sv-056-420-iem"></a>
## BÀI 1.2: CHỨNG CHỈ SỐ RSA CỦA CA CHO MÃ SV 056 (4/20 ĐIỂM)

> [!TIP]
> **File code giải bài toán:** [`code/pki_rsa_certificate.py`](code/pki_rsa_certificate.py)  
> *Lệnh chạy terminal:* `python code/pki_rsa_certificate.py`

1. Tham số CA: $p_{\text{CA}} = 227, q_{\text{CA}} = 149 \implies N_{\text{CA}} = 33823, e_{\text{CA}} = 25537$.
2. $\Phi(N_{\text{CA}}) = 226 \times 148 = \mathbf{33448}$.
3. Khóa riêng CA:
   $$d_{\text{CA}} \equiv 25537^{-1} \pmod{33448} = \mathbf{15593}$$
4. Ký chứng chỉ số cho Mã SV `23BA14056` ($M = 56$):
   $$S_{\text{CA}} \equiv M^{d_{\text{CA}}} \pmod{N_{\text{CA}}} = 56^{15593} \pmod{33823} = \mathbf{11273}$$
5. Xác minh chữ ký số (Người dùng B):
   $$V \equiv S_{\text{CA}}^{e_{\text{CA}}} \pmod{N_{\text{CA}}} = 11273^{25537} \pmod{33823} = \mathbf{56} = M \quad (\text{Hợp lệ})$$

---

<a id="bai-13-quy-trinh-trao-oi-email-bao-mat-pki-420-iem"></a>
## BÀI 1.3: QUY TRÌNH TRAO ĐỔI EMAIL BẢO MẬT PKI (4/20 ĐIỂM)

> [!TIP]
> **File code giải thích & minh họa quy trình:** [`code/pki_rsa_certificate.py`](code/pki_rsa_certificate.py)  
> *Lệnh chạy terminal:* `python code/pki_rsa_certificate.py`

Quy trình gồm 3 bước:
1. **Bước 1 (Đăng ký chứng chỉ):** Người dùng A gửi khóa công khai $k_{\text{pub}, A}$ và định danh cho CA để nhận chứng chỉ số $\text{Cert}_A = (A, k_{\text{pub}, A}, S_{\text{CA}})$.
2. **Bước 2 (Trao đổi chứng chỉ & Khóa phiên):** Người dùng A gửi $\text{Cert}_A$ cho B. Người dùng B dùng khóa công khai của CA để xác thực $k_{\text{pub}, A}$. B tạo khóa phiên đối xứng $K_{\text{session}}$ (AES), mã hóa $K_{\text{session}}$ bằng khóa công khai của A ($C_K = e_{k_{\text{pub}, A}}(K_{\text{session}})$) và gửi cho A.
3. **Bước 3 (Truyền email bảo mật):** Người dùng A giải mã lấy $K_{\text{session}}$. Hai bên sử dụng $K_{\text{session}}$ cùng chế độ AES-GCM hoặc AES-CBC để mã hóa và giải mã nội dung email với tốc độ cao.

---

<a id="phan-iv-e-thi-so-3-hoc-ky-2-nam-hoc-20232024-75-phut"></a>
# PHẦN IV: ĐỀ THI SỐ 3 – HỌC KỲ 2, NĂM HỌC 2023–2024 (THỨ NĂM, 30/11/2023 - 75 PHÚT)
*(Trích từ đề thi gốc 3 trang: [`01.webp`](01.webp), [`02.webp`](02.webp), [`03.webp`](03.webp))*  
- **Mã học phần:** ICT3.001 (Introduction to Cryptography) – Thời gian: 75 phút – Mã đề: 00  
- **Giảng viên ra đề:** ThS. Nguyễn Minh Hướng  
- **Quy định phòng thi:** Được dùng 1 tờ A4 viết tay, máy tính bỏ túi. 30 phút cuối được mở laptop không kết nối Internet.  
- **File code Python tự động giải và xác thực 100%:** [`code/exam_2023_2024_solver.py`](code/exam_2023_2024_solver.py)

---

<a id="cau-0-cau-hoi-quan-trong-tra-cuu-hop-s-box-des-va-chon-e-thi-320-iem"></a>
## CÂU 0: CÂU HỎI QUAN TRỌNG: TRA CỨU HỘP S-BOX DES VÀ CHỌN ĐỀ THI (3/20 ĐIỂM)

### 1. Đề bài
- Xác định số nguyên $x$ từ **3 chữ số cuối** trong mã sinh viên theo công thức:
  $$x = (\text{YourStudentID}) \pmod{64}$$
- Tính toán đầu ra của hộp S-Box $S_1$ dùng trong chuẩn mã hóa DES với đầu vào là dạng biểu diễn nhị phân của số $x$.
- **Quy tắc phân nhánh đề thi:**
  - Nếu đầu ra của hộp S-Box là **SỐ CHẴN (EVEN)**: Thí sinh làm **Question set 02**.
  - Nếu đầu ra của hộp S-Box là **SỐ LẺ (ODD)**: Thí sinh làm **Question set 01**.

Bảng tra cứu hộp phi tuyến $S_1$ của DES (trích trong đề thi):
$$\begin{array}{|c|c c c c c c c c c c c c c c c c|}
\hline
S_1 & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 & 12 & 13 & 14 & 15 \\
\hline
0 & 14 & 04 & 13 & 01 & 02 & 15 & 11 & 08 & 03 & 10 & 06 & 12 & 05 & 09 & 00 & 07 \\
1 & 00 & 15 & 07 & 04 & 14 & 02 & 13 & 01 & 10 & 06 & 12 & 11 & 09 & 05 & 03 & 08 \\
2 & 04 & 01 & 14 & 08 & 13 & 06 & 02 & 11 & 15 & 12 & 09 & 07 & 03 & 10 & 05 & 00 \\
3 & 15 & 12 & 08 & 02 & 04 & 09 & 01 & 07 & 05 & 11 & 03 & 14 & 10 & 00 & 06 & 13 \\
\hline
\end{array}$$

---

### 2. Bài giải chi tiết tự luận (Mã SV: 23BA14056)

#### Bước 1: Xác định số nguyên $x$ từ mã sinh viên
- Mã sinh viên: `23BA14056`.
- 3 chữ số cuối cùng là: `056` $\implies$ Giá trị số nguyên tương ứng: $56$.
- Tính số $x$ qua phép đồng dư modulo 64:
  $$x = 56 \pmod{64} = \mathbf{56}$$

#### Bước 2: Chuyển đổi $x = 56$ sang chuỗi nhị phân 6 bit
Ta thực hiện phân tích số $56$ thành tổng các lũy thừa của 2:
$$56 = 32 + 16 + 8 = 1 \cdot 2^5 + 1 \cdot 2^4 + 1 \cdot 2^3 + 0 \cdot 2^2 + 0 \cdot 2^1 + 0 \cdot 2^0$$
Do đó, dạng biểu diễn nhị phân 6-bit của $x$ là:
$$(x)_2 = (b_1 b_2 b_3 b_4 b_5 b_6)_2 = \mathbf{111000_2}$$

#### Bước 3: Xác định tọa độ Hàng và Cột trong hộp $S_1$
Theo quy chuẩn thiết kế của hộp thay thế DES:
- **Chỉ số Hàng ($r$ - Row):** Được cấu tạo bởi 2 bit ngoài cùng (bit đầu tiên $b_1$ và bit cuối cùng $b_6$):
  $$r = (b_1 b_6)_2 = (10)_2 = 1 \cdot 2^1 + 0 \cdot 2^0 = \mathbf{2} \quad (\text{Hàng số } 2)$$
- **Chỉ số Cột ($c$ - Column):** Được cấu tạo bởi 4 bit ở giữa ($b_2, b_3, b_4, b_5$):
  $$c = (b_2 b_3 b_4 b_5)_2 = (1100)_2 = 1 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 0 \cdot 2^0 = 8 + 4 = \mathbf{12} \quad (\text{Cột số } 12)$$

#### Bước 4: Tra cứu bảng $S_1$ và kết luận chọn đề
Dóng theo Hàng 2 và Cột 12 trong bảng $S_1$:
- Hàng 2: `[04, 01, 14, 08, 13, 06, 02, 11, 15, 12, 09, 07, 03, 10, 05, 00]`
- Giá trị tại vị trí Cột 12 (đếm từ 0 đến 15) là: **`03`** (dạng thập phân: $3$, dạng nhị phân 4-bit: $0011_2$).

$$S_1(111000_2) = \mathbf{3}$$

> [!IMPORTANT]
> **KẾT LUẬN PHÂN NHÁNH ĐỀ THI:**
> - Vì giá trị đầu ra của hộp S-Box là $3$, đây là một **SỐ LẺ (ODD NUMBER)**.
> - Căn cứ theo quy định của đề thi: **Thí sinh mã sinh viên 23BA14056 thực hiện QUESTION SET 01**.
> - *(Dưới đây, tài liệu cung cấp lời giải toàn diện 100% cho cả **Question set 01** và **Question set 02**).*

---

<a id="question-set-01-loi-giai-e-chinh-thuc-cho-s-box-le"></a>
# QUESTION SET 01 (LỜI GIẢI ĐỀ CHÍNH THỨC CHO S-BOX LẺ)

<a id="set-01-bai-1-ham-bam-sha-1-padding-so-do-khoi-420-iem"></a>
## BÀI 1: HÀM BĂM SHA-1 PADDING (l = 2096 BITS) & SƠ ĐỒ KHỐI DAVIES-MEYER (4/20 ĐIỂM)

### 1. Ý 1: Tiền xử lý đệm (Padding Preprocess) cho thông điệp $l = 2096$ bits

#### Bước 1: Nguyên lý đệm theo tiêu chuẩn FIPS PUB 180-1 (SHA-1)
Hàm băm SHA-1 xử lý dữ liệu theo từng khối cố định **512 bits**. Trước khi đưa vào thuật toán nén lặp Merkle-Damgård, một thông điệp có chiều dài $l$ bit bất kỳ phải được đệm để tổng chiều dài sau đệm là bội số nguyên của 512 bit ($N \times 512$ bits). Quy trình thực hiện qua 3 bước bắt buộc:
1. Nối thêm **đúng 1 bit `1`** vào ngay sau bit cuối cùng của thông điệp gốc. Chiều dài lúc này trở thành $l + 1$ bits.
2. Nối thêm **$k$ bit `0`** (với $k \ge 0$ là số nguyên không âm nhỏ nhất) sao cho tổng chiều dài thỏa mãn:
   $$(l + 1 + k) \equiv 448 \pmod{512}$$
   *(Nghĩa là cách bội số của 512 đúng 64 bits để dành chỗ cho trường lưu trữ độ dài).*
3. Nối thêm **khối 64-bit biểu diễn số nguyên $l$** (chiều dài ban đầu của thông điệp) theo định dạng số nguyên không dấu nhị phân chuẩn Big-Endian.

#### Bước 2: Tính toán số bit đệm $k$ cho $l = 2096$ bits
Ta phân tích chiều dài thông điệp:
$$l = 2096 = 4 \times 512 + 48 \implies 2096 \equiv 48 \pmod{512}$$
Sau khi nối 1 bit `1`:
$$l + 1 = 2096 + 1 = 2097 \equiv 49 \pmod{512}$$
Điều kiện đệm $k$ bit `0`:
$$(49 + k) \equiv 448 \pmod{512} \implies k = 448 - 49 = \mathbf{399} \quad (\text{bit } 0)$$

#### Bước 3: Xác định tổng chiều dài và số khối 512-bit sau đệm
Tổng chiều dài thông điệp sau khi đệm hoàn tất:
$$L = l + 1 + k + 64 = 2096 + 1 + 399 + 64 = \mathbf{2560} \quad \text{bits}$$
Số lượng khối 512-bit được đưa vào xử lý:
$$N = \frac{2560}{512} = \mathbf{5} \quad \text{khối } (M_1, M_2, M_3, M_4, M_5)$$

#### Bước 4: Biểu diễn 64-bit độ dài thông điệp gốc $l = 2096$
- Giá trị thập phân: $l = 2096$.
- Dưới dạng thập lục phân (Hexadecimal 16 ký tự):
  $$2096 = 8 \times 256 + 48 = 0x0830 \implies \mathbf{0x0000000000000830}$$
- Dưới dạng nhị phân 64 bit (Big-Endian):
  $$\mathbf{00000000\ 00000000\ 00000000\ 00000000\ 00000000\ 00000000\ 00001000\ 00110000_2}$$

#### Bước 5: Mô tả định dạng chi tiết của 5 khối $M_1 \dots M_5$ trước khi nén
| Tên khối | Dải chỉ số bit | Cấu trúc nội dung chi tiết |
| :---: | :---: | :--- |
| **Khối $M_1$** | $0 \dots 511$ | Chứa 512 bit đầu tiên của thông điệp gốc (bit $0$ đến bit $511$). |
| **Khối $M_2$** | $512 \dots 1023$ | Chứa 512 bit tiếp theo của thông điệp gốc (bit $512$ đến bit $1023$). |
| **Khối $M_3$** | $1024 \dots 1535$ | Chứa 512 bit tiếp theo của thông điệp gốc (bit $1024$ đến bit $1535$). |
| **Khối $M_4$** | $1536 \dots 2047$ | Chứa 512 bit tiếp theo của thông điệp gốc (bit $1536$ đến bit $2047$). |
| **Khối $M_5$** | $2048 \dots 2559$ | Chứa $48$ bit thông điệp gốc còn lại (bit $2048 \dots 2095$) + **1 bit `1`** + **$399$ bit `0`** + **64 bit độ dài gốc** ($l=2096$). |

---

### 2. Ý 2: Vẽ và giải thích sơ đồ khối hàm băm $H_i = e(x_i, H_{i-1}) \oplus H_{i-1}$

#### Bước 1: Nhận diện cấu trúc nén
Hàm băm được xây dựng từ hàm mã hóa khối $e(K, P)$ với:
$$H_i = e(x_i, H_{i-1}) \oplus H_{i-1}$$
- Cổng **Khóa (Key)** của thuật toán mã hóa nhận khối thông điệp hiện tại: $K = x_i$.
- Cổng **Bản rõ (Plaintext)** nhận giá trị băm của vòng trước: $P = H_{i-1}$.
- Đầu ra của khối mã hóa $e(x_i, H_{i-1})$ được cộng XOR $(\oplus)$ với chính đường truyền tiến (feedforward) của giá trị băm vòng trước $H_{i-1}$.
- **Tên gọi kiến trúc:** Đây chính là cấu trúc nén **Davies-Meyer** kinh điển (nền tảng của các hàm băm chuẩn như MD5, SHA-1, SHA-2).

#### Bước 2: Sơ đồ khối (Block Diagram)

```
             Khối thông điệp x_i
                     │
                     ▼ (Key input)
             ┌───────────────┐
             │               │
H_{i-1} ────┬┤  Mã hóa khối  ├─────┐
 (Bản rõ)   ││    e(K, P)    │     │
            ││               │     ▼
            │└───────────────┘   ┌───┐
            │                    │ ⊕ │──────► H_i (Giá trị băm mới)
            └───────────────────►│   │
                (Feedforward)    └───┘
```

#### Bước 3: Giải thích nguyên lý hoạt động & tính một chiều (One-Wayness)
1. **Khử tính khả nghịch của mã khối:** Thuật toán mã hóa khối $e$ vốn có tính khả nghịch (tồn tại giải mã $e^{-1}$). Nhờ có phép cộng XOR vòng lặp truyền tiến (feedforward $\oplus H_{i-1}$), kẻ tấn công không thể đảo ngược từ $H_i$ để suy ra $H_{i-1}$ ngay cả khi biết khối $x_i$, vì phương trình $H_i = e(x_i, H_{i-1}) \oplus H_{i-1}$ là phương trình phi tuyến không thể giải ngược theo chiều thuận thông thường.
2. **Khởi tạo:** Với khối đầu tiên $i=1$, giá trị đầu vào là vectơ khởi tạo cố định $H_0 = \text{IV}$ (Initialization Vector).

---

<a id="set-01-bai-2-trao-doi-khoa-diffie-hellman-420-iem"></a>
## BÀI 2: TRAO ĐỔI KHÓA DIFFIE-HELLMAN (p = 863, alpha = 2) (4/20 ĐIỂM)

### 1. Đề bài
Thực hiện giao thức trao đổi khóa Diffie-Hellman (DHKE) giữa Alice và Bob với các tham số:
- Số nguyên tố: $p = 863$
- Phần tử sinh (Generator): $\alpha = 2$
- Khóa bí mật do người dùng chọn: Alice chọn $a = 2023$, Bob chọn $b = 2024$.
- **Yêu cầu:** Tính khóa công khai $k_A, k_B$ của hai bên và tính khóa bí mật chung $k_{AB}$.

---

### 2. Bài giải chi tiết tự luận

#### Bước 1: Alice tính khóa công khai $k_A$
Công thức:
$$k_A = \alpha^a \pmod p = 2^{2023} \pmod{863}$$

*Kỹ thuật rút gọn số mũ bằng định lý Fermat nhỏ:*
Vì $p = 863$ là số nguyên tố và $\gcd(2, 863) = 1$, theo định lý Fermat nhỏ ta có:
$$2^{p-1} = 2^{862} \equiv 1 \pmod{863}$$
Phân tích số mũ $a = 2023$:
$$2023 = 2 \times 862 + 299 \implies 2023 \equiv 299 \pmod{862}$$
Do đó:
$$k_A \equiv 2^{299} \pmod{863}$$

Áp dụng thuật toán Square-and-Multiply tính $2^{299} \pmod{863}$:
$$299 = (100101011)_2$$
Ta thu được:
$$k_A = \mathbf{629}$$

#### Bước 2: Bob tính khóa công khai $k_B$
Công thức:
$$k_B = \alpha^b \pmod p = 2^{2024} \pmod{863}$$
Vì $b = 2024 = 2023 + 1$, ta tính nhanh thông qua $k_A$:
$$k_B = 2^{2024} \pmod{863} = (2^{2023} \cdot 2) \pmod{863} = (629 \times 2) \pmod{863} = 1258 \pmod{863}$$
$$k_B = 1258 - 863 = \mathbf{395}$$

#### Bước 3: Tính khóa phiên bí mật chung $k_{AB}$
- **Alice nhận $k_B = 395$ và tính:**
  $$k_{AB} = (k_B)^a \pmod p = 395^{2023} \pmod{863}$$
  Rút gọn số mũ: $2023 \equiv 299 \pmod{862}$.
  $$k_{AB} = 395^{299} \pmod{863} = \mathbf{113}$$

- **Bob nhận $k_A = 629$ và tính:**
  $$k_{AB} = (k_A)^b \pmod p = 629^{2024} \pmod{863}$$
  Rút gọn số mũ: $2024 \equiv 300 \pmod{862}$.
  $$k_{AB} = 629^{300} \pmod{863} = \mathbf{113}$$

> [!TIP]
> **ĐÁP SỐ BÀI 2 (QUESTION SET 01):**
> - Khóa công khai của Alice: $k_A = \mathbf{629}$
> - Khóa công khai của Bob  : $k_B = \mathbf{395}$
> - Khóa phiên bí mật chung : $k_{AB} = \mathbf{113}$ (Trùng khớp 100% giữa hai bên).

---

<a id="set-01-bai-3-he-thong-chu-ky-so-elgamal-va-chung-chi-ca-920-iem"></a>
## BÀI 3: HỆ THỐNG CHỮ KÝ SỐ ELGAMAL & CHỨNG CHỈ CA (9/20 ĐIỂM)

### 1. Đề bài
Tham số hệ thống chữ ký số ElGamal của Bob:
- Khóa riêng của Bob: $K_{pr} = d = 127$.
- Khóa công khai của Bob: $K_{pub} = (p, \alpha, \beta)$ với $p = 863, \alpha = 2$.
- **Yêu cầu 1:** Tính khóa công khai $\beta$. Ký thông điệp $x = 30$ gửi từ Bob cho Alice với khóa tạm thời $k_E = 215$, thu cặp chữ ký $(r, s)$ và xác thực.
- **Yêu cầu 2:** Nhận được 2 thông điệp kèm chữ ký từ Bob: $(x_1, r_1, s_1) = (40, 306, 64)$ và $(x_2, r_2, s_2) = (55, 306, 465)$. Xác minh xem cả hai có thực sự do Bob ký hay không?
- **Yêu cầu 3:** Nhà cấp chứng thực số CA dùng hệ chữ ký ElGamal để cấp chứng chỉ cho Alice ($\text{ID}(A) = 1$) và Bob ($\text{ID}(B) = 2$) với khóa tạm thời tương ứng $k_{E-A} = 213$ và $k_{E-B} = 211$. Khóa công khai DHKE của Alice và Bob lấy từ Bài 2 ($k_A = 629, k_B = 395$).
  CA tính giá trị đại diện chứng chỉ:
  $$x_i = 4 \cdot k_i + \text{ID}(i)$$
  Tính và xác thực hai chứng chỉ số $\text{Cert}_A$ và $\text{Cert}_B$.

---

### 2. Bài giải chi tiết tự luận

#### Phần 3.1: Tạo và xác thực chữ ký của Bob cho thông điệp $x = 30, k_E = 215$

##### Bước 1: Tính khóa công khai $\beta$ của Bob
$$\beta = \alpha^d \pmod p = 2^{127} \pmod{863}$$
Thực hiện tính lũy thừa bằng Square-and-Multiply:
$$\beta = \mathbf{365}$$
Vậy khóa công khai của Bob là: $K_{pub} = (p = 863, \alpha = 2, \beta = 365)$.

##### Bước 2: Kiểm tra điều kiện khả nghịch của $k_E = 215$
Ta tính ước chung lớn nhất giữa $k_E$ và $p - 1 = 862$:
$$\gcd(k_E, p-1) = \gcd(215, 862) = \gcd(215, 862 - 4 \times 215) = \gcd(215, 2) = 1$$
Vì $\gcd(215, 862) = 1$, khóa tạm thời $k_E$ hoàn toàn hợp lệ và tồn tại nghịch đảo modulo $862$.

Tìm nghịch đảo $k_E^{-1} \pmod{862}$ qua thuật toán Euclid mở rộng:
$$862 = 4 \times 215 + 2 \implies 2 = 862 - 4 \times 215$$
$$215 = 107 \times 2 + 1 \implies 1 = 215 - 107 \times 2 = 215 - 107 \times (862 - 4 \times 215) = 429 \times 215 - 107 \times 862$$
Do đó:
$$k_E^{-1} \equiv \mathbf{429} \pmod{862}$$
*(Kiểm tra: $(215 \times 429) \pmod{862} = 92235 \pmod{862} = 1$).*

##### Bước 3: Tính thành phần chữ ký thứ nhất $r$
$$r = \alpha^{k_E} \pmod p = 2^{215} \pmod{863}$$
$$r = \mathbf{306}$$

##### Bước 4: Tính thành phần chữ ký thứ hai $s$
Công thức chữ ký ElGamal:
$$s \equiv (x - d \cdot r) \cdot k_E^{-1} \pmod{p-1}$$
Thay các giá trị: $x = 30, d = 127, r = 306, k_E^{-1} = 429$:
$$d \cdot r = 127 \times 306 = 38862$$
$$x - d \cdot r = 30 - 38862 = -38832$$
Đưa về phần dư dương modulo 862:
$$-38832 = -46 \times 862 + 820 \implies -38832 \equiv 820 \pmod{862}$$
Tính $s$:
$$s \equiv (820 \times 429) \pmod{862} = 351780 \pmod{862} = \mathbf{84}$$

**Cặp chữ ký ElGamal:**
$$(r, s) = \mathbf{(306, 84)}$$

##### Bước 5: Xác thực chữ ký
Người nhận Alice kiểm tra điều kiện đẳng thức:
$$v_1 \equiv \beta^r \cdot r^s \pmod p \quad \text{và} \quad v_2 \equiv \alpha^x \pmod p$$
- Tính $v_1$:
  $$v_1 = (365^{306} \cdot 306^{84}) \pmod{863}$$
  - $365^{306} \pmod{863} = 730$
  - $306^{84} \pmod{863} = 153$
  - $v_1 = (730 \times 153) \pmod{863} = 111690 \pmod{863} = \mathbf{676}$
- Tính $v_2$:
  $$v_2 = 2^{30} \pmod{863} = 1073741824 \pmod{863} = \mathbf{676}$$

Vì $v_1 = v_2 = \mathbf{676}$, chữ ký **HOÀN TOÀN HỢP LỆ**.

---

#### Phần 3.2: Xác minh hai thông điệp nhận được có phải từ Bob không

##### 1. Xác minh thông điệp $(x_1, r_1, s_1) = (40, 306, 64)$:
- Tính $v_1$:
  $$v_1 = (\beta^{r_1} \cdot r_1^{s_1}) \pmod p = (365^{306} \cdot 306^{64}) \pmod{863}$$
  - $365^{306} \pmod{863} = 730$
  - $306^{64} \pmod{863} = 227$
  - $v_1 = (730 \times 227) \pmod{863} = 165710 \pmod{863} = \mathbf{98}$
- Tính $v_2$:
  $$v_2 = \alpha^{x_1} \pmod p = 2^{40} \pmod{863} = \mathbf{98}$$
- **Kết luận 1:** $v_1 = v_2 = 98 \implies$ **Thông điệp 1 thực sự do Bob ký và toàn vẹn!**

##### 2. Xác minh thông điệp $(x_2, r_2, s_2) = (55, 306, 465)$:
- Tính $v_1$:
  $$v_1 = (\beta^{r_2} \cdot r_2^{s_2}) \pmod p = (365^{306} \cdot 306^{465}) \pmod{863}$$
  - $365^{306} \pmod{863} = 730$
  - $306^{465} \pmod{863} = 512$
  - $v_1 = (730 \times 512) \pmod{863} = 373760 \pmod{863} = \mathbf{41}$
- Tính $v_2$:
  $$v_2 = \alpha^{x_2} \pmod p = 2^{55} \pmod{863} = \mathbf{41}$$
- **Kết luận 2:** $v_1 = v_2 = 41 \implies$ **Thông điệp 2 cũng thực sự do Bob ký và toàn vẹn!**

> [!WARNING]
> **NHẬN XÉT BẢO MẬT CHUYÊN SÂU (ĐIỂM CỘNG THI TỰ LUẬN):**
> Cả 2 thông điệp đều có thành phần chữ ký thứ nhất $r_1 = r_2 = \mathbf{306}$. Điều này chứng tỏ **Bob đã tái sử dụng cùng một khóa tạm thời $k_E = 215$ cho hai thông điệp khác nhau ($x_1 \ne x_2$)**.
> Đây là một lỗ hổng chí mạng trong ElGamal: Kẻ tấn công có thể dễ dàng giải hệ phương trình:
> $$s_1 - s_2 \equiv k_E^{-1} (x_1 - x_2) \pmod{p-1}$$
> để tìm ra $k_E$, từ đó khôi phục hoàn toàn khóa bí mật $d$ của Bob!

---

#### Phần 3.3: Tính và xác thực chứng chỉ CA cho Alice và Bob

Theo đề bài, CA sử dụng hệ chữ ký ElGamal với tham số $(p = 863, \alpha = 2, d = 127, \beta = 365)$.
Khóa trao đổi DHKE tính từ Bài 2: Alice có $k_A = 629$, Bob có $k_B = 395$.

##### 1. Cấp và xác thực chứng chỉ $\text{Cert}_A$ cho Alice ($\text{ID}(A) = 1, k_{E-A} = 213$):
- **Thông điệp cần ký:**
  $$x_A = 4 \cdot k_A + \text{ID}(A) = 4 \times 629 + 1 = \mathbf{2517}$$
- **Kiểm tra khả nghịch của $k_{E-A} = 213$:**
  $$\gcd(213, 862) = 1 \implies k_{E-A}^{-1} \equiv \mathbf{211} \pmod{862}$$
- **Tính chữ ký $(r_A, s_A)$:**
  $$r_A = \alpha^{k_{E-A}} \pmod p = 2^{213} \pmod{863} = \mathbf{508}$$
  $$s_A \equiv (x_A - d \cdot r_A) \cdot k_{E-A}^{-1} \pmod{862}$$
  $$x_A - d \cdot r_A = 2517 - 127 \times 508 = 2517 - 64516 = -61999 \equiv 65 \pmod{862}$$
  $$s_A \equiv (65 \times 211) \pmod{862} = 13715 \pmod{862} = \mathbf{405}$$
  $$\mathbf{\text{Cert}_A = (r_A = 508, s_A = 405)}$$
- **Xác thực chứng chỉ $\text{Cert}_A$:**
  $$v_1 = (365^{508} \cdot 508^{405}) \pmod{863} = (527 \times 441) \pmod{863} = \mathbf{34}$$
  $$v_2 = 2^{2517} \pmod{863} \equiv 2^{793} \pmod{863} = \mathbf{34}$$
  Vì $v_1 = v_2 = 34 \implies$ **Chứng chỉ $\text{Cert}_A$ của Alice HỢP LỆ!**

##### 2. Cấp và xác thực chứng chỉ $\text{Cert}_B$ cho Bob ($\text{ID}(B) = 2, k_{E-B} = 211$):
- **Thông điệp cần ký:**
  $$x_B = 4 \cdot k_B + \text{ID}(B) = 4 \times 395 + 2 = \mathbf{1582}$$
- **Kiểm tra khả nghịch của $k_{E-B} = 211$:**
  $$\gcd(211, 862) = 1 \implies k_{E-B}^{-1} \equiv \mathbf{213} \pmod{862}$$
- **Tính chữ ký $(r_B, s_B)$:**
  $$r_B = \alpha^{k_{E-B}} \pmod p = 2^{211} \pmod{863} = \mathbf{127}$$
  $$s_B \equiv (x_B - d \cdot r_B) \cdot k_{E-B}^{-1} \pmod{862}$$
  $$x_B - d \cdot r_B = 1582 - 127 \times 127 = 1582 - 16129 = -14547 \equiv 107 \pmod{862}$$
  $$s_B \equiv (107 \times 213) \pmod{862} = 22791 \pmod{862} = \mathbf{503}$$
  $$\mathbf{\text{Cert}_B = (r_B = 127, s_B = 503)}$$
- **Xác thực chứng chỉ $\text{Cert}_B$:**
  $$v_1 = (365^{127} \cdot 127^{503}) \pmod{863} = (205 \times 199) \pmod{863} = \mathbf{288}$$
  $$v_2 = 2^{1582} \pmod{863} \equiv 2^{720} \pmod{863} = \mathbf{288}$$
  Vì $v_1 = v_2 = 288 \implies$ **Chứng chỉ $\text{Cert}_B$ của Bob HỢP LỆ!**

---

<a id="question-set-02-loi-giai-e-mo-rong-cho-s-box-chan"></a>
# QUESTION SET 02 (LỜI GIẢI ĐỀ MỞ RỘNG CHO S-BOX CHẴN)

<a id="set-02-bai-1-ham-bam-sha-1-padding-so-do-khoi-420-iem"></a>
## BÀI 1: HÀM BĂM SHA-1 PADDING (l = 2225 BITS) & SƠ ĐỒ KHỐI (4/20 ĐIỂM)

### 1. Ý 1: Tiền xử lý đệm SHA-1 cho thông điệp $l = 2225$ bits
- Chiều dài thông điệp gốc: $l = 2225$ bits.
- Phân tích: $2225 = 4 \times 512 + 177 \implies 2225 \equiv 177 \pmod{512}$.
- Nối thêm 1 bit `1`: $l + 1 = 2226 \equiv 178 \pmod{512}$.
- Tìm số bit `0` đệm $k$:
  $$(178 + k) \equiv 448 \pmod{512} \implies k = 448 - 178 = \mathbf{270} \quad (\text{bit } 0)$$
- Tổng chiều dài sau đệm:
  $$L = 2225 + 1 + 270 + 64 = \mathbf{2560} \quad \text{bits} = \mathbf{5} \text{ khối } 512\text{-bit } (M_1 \dots M_5)$$
- Trường độ dài 64-bit ($l = 2225$):
  $$2225 = 8 \times 256 + 177 = 0x08b1 \implies \mathbf{0x00000000000008b1}$$
- **Định dạng 5 khối:** Khối $M_1 \dots M_4$ chứa 2048 bit gốc đầu tiên; khối $M_5$ chứa 177 bit thông điệp còn lại + 1 bit `1` + 270 bit `0` + 64 bit độ dài gốc.

---

### 2. Ý 2: Sơ đồ khối hàm băm $H_i = e(x_i, H_{i-1}) \oplus x_i$
- Trong cấu trúc này, đầu vào bản rõ của mã khối là $H_{i-1}$, đầu vào khóa là $x_i$, và đường feedforward XOR lấy từ **khối thông điệp $x_i$**:

```
             ┌─────────────────────────┐
             │  Khối thông điệp x_i    │
             └────┬───────────────┬────┘
                  │ (Key)         │ (Feedforward)
                  ▼               │
           ┌──────────────┐       │
H_{i-1} ──►│ Mã hóa khối  ├─┐     │
(Bản rõ)   │   e(K, P)    │ │     ▼
           └──────────────┘ │   ┌───┐
                            └──►│ ⊕ │──────► H_i
                                └───┘
```

---

<a id="set-02-bai-2-trao-doi-khoa-diffie-hellman-420-iem"></a>
## BÀI 2: TRAO ĐỔI KHÓA DIFFIE-HELLMAN (p = 593, alpha = 2) (4/20 ĐIỂM)

- Tham số: $p = 593$, $\alpha = 2$, Alice chọn $a = 2023$, Bob chọn $b = 2024$.
- Rút gọn số mũ theo Fermat nhỏ ($p - 1 = 592$):
  $$2023 = 3 \times 592 + 247 \implies 2023 \equiv 247 \pmod{592}$$
  $$2024 \equiv 248 \pmod{592}$$
- **Khóa công khai của Alice $k_A$:**
  $$k_A = 2^{2023} \pmod{593} = 2^{247} \pmod{593} = \mathbf{473}$$
- **Khóa công khai của Bob $k_B$:**
  $$k_B = 2^{2024} \pmod{593} = (473 \times 2) \pmod{593} = 946 \pmod{593} = \mathbf{353}$$
- **Khóa chung $k_{AB}$:**
  $$k_{AB} = 353^{2023} \pmod{593} = 473^{2024} \pmod{593} = \mathbf{281}$$

---

<a id="set-02-bai-3-he-thong-chu-ky-so-elgamal-va-chung-chi-ca-920-iem"></a>
## BÀI 3: HỆ THỐNG CHỮ KÝ SỐ ELGAMAL & CHỨNG CHỈ CA (9/20 ĐIỂM)

Tham số: $p = 593, \alpha = 2, d = 127$.
- Khóa công khai Bob:
  $$\beta = 2^{127} \pmod{593} = \mathbf{435}$$

### 3.1 Ký thông điệp $x = 30, k_e = 215$:
- $\gcd(215, 592) = 1 \implies k_e^{-1} \equiv \mathbf{391} \pmod{592}$.
- $r = 2^{215} \pmod{593} = \mathbf{227}$.
- $s = (30 - 127 \times 227) \times 391 \pmod{592} = (-28799 \times 391) \pmod{592} = \mathbf{23}$.
- Cặp chữ ký: $(r, s) = \mathbf{(227, 23)}$.
- Xác thực: $v_1 = (435^{227} \cdot 227^{23}) \pmod{593} = 282$; $v_2 = 2^{30} \pmod{593} = 282 \implies$ Hợp lệ.

### 3.2 Kiểm tra hai thông điệp nhận được:
1. **Thông điệp $(x_1, r_1, s_1) = (42, 306, 64)$:**
   $$v_1 = (435^{306} \cdot 306^{64}) \pmod{593} = \mathbf{592}$$
   $$v_2 = 2^{42} \pmod{593} = \mathbf{501}$$
   Vì $v_1 \ne v_2 \implies$ **CHỮ KÝ KHÔNG HỢP LỆ (Không phải từ Bob)!**
2. **Thông điệp $(x_2, r_2, s_2) = (50, 306, 465)$:**
   $$v_1 = (435^{306} \cdot 306^{465}) \pmod{593} = \mathbf{514}$$
   $$v_2 = 2^{50} \pmod{593} = \mathbf{168}$$
   Vì $v_1 \ne v_2 \implies$ **CHỮ KÝ KHÔNG HỢP LỆ (Không phải từ Bob)!**

> [!CAUTION]
> **PHÂN TÍCH ĐỀ THI:**
> Cả hai thông điệp trên đều **KHÔNG HỢP LỆ** vì cặp tham số $(r=306, s_1=64, s_2=465)$ là giá trị sinh ra từ đề thi $p=863$ của Question set 01. Khi đưa vào hệ thống $p=593$, chữ ký bị sai lệch hoàn toàn. Thí sinh khẳng định cả hai thông điệp đều bị giả mạo hoặc lỗi hệ thống.

### 3.3 Cấp và xác thực chứng chỉ CA:
- Alice ($\text{ID}(A) = 1, k_A = 473, k_{E-A} = 213$):
  - $x_A = 4 \times 473 + 1 = 1893$.
  - $\text{Cert}_A = (r_A = \mathbf{205}, s_A = \mathbf{298})$.
  - Xác thực: $v_1 = v_2 = 184 \implies$ Hợp lệ.
- Bob ($\text{ID}(B) = 2, k_B = 353, k_{E-B} = 211$):
  - $x_B = 4 \times 353 + 2 = 1414$.
  - $\text{Cert}_B = (r_B = \mathbf{496}, s_B = \mathbf{418})$.
  - Xác thực: $v_1 = v_2 = 337 \implies$ Hợp lệ.

---

<a id="phan-v-cam-nang-phuong-phap-tinh-nhanh-trong-phong-thi"></a>
# PHẦN V: CẨM NANG PHƯƠNG PHÁP TÍNH NHANH TRONG PHÒNG THI

<a id="1-thuat-toan-euclid-mo-rong-tinh-nghich-ao-modulo-a-1-pmod-m"></a>
### 1. Thuật toán Euclid mở rộng tính nghịch đảo modulo $a^{-1} \pmod m$

> [!TIP]
> **File code tính GCD & nghịch đảo modulo:** [`code/extended_euclidean.py`](code/extended_euclidean.py) và [`code/euclidean_gcd.py`](code/euclidean_gcd.py)  
> *Lệnh chạy terminal:* `python code/extended_euclidean.py`

| Bước | $m$ | $a$ | Thương $q = \lfloor m/a \rfloor$ | Dư $r = m \pmod a$ | $x$ | $y$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 31188 | 125 | 249 | 63 | $x_1$ | $y_1$ |
| 2 | 125 | 63 | 1 | 62 | $x_2$ | $y_2$ |
| 3 | 63 | 62 | 1 | 1 | 1 | -1 |

Thế ngược: $1 = 63 - 1 \times 62 = 63 - 1 \times (125 - 1 \times 63) = 2 \times 63 - 1 \times 125 = 2 \times (31188 - 249 \times 125) - 125 = 2 \times 31188 - 499 \times 125$.  
Do đó $125 \times (-499) \equiv 1 \pmod{31188}$.  
Nghịch đảo dương: $-499 + 31188 = \mathbf{30689}$.

<a id="2-bang-tom-tat-ap-so-cho-ma-sinh-vien-23ba14056"></a>
### 2. Bảng Tóm Tắt Đáp Số Chuẩn Cho Đề Thi 2025–2026 (Mã SV: 23BA14056)
- **Đầu vào Bài 1 (S-Box):** $x = \text{Mã\_SV} \pmod{64} = 056 \pmod{64} = \mathbf{56}$.
- **Đầu ra Hộp S-box $S_1$:** Hàng 2, Cột 12 $\implies \mathbf{3}$ (nhị phân: $\mathbf{0011_2}$).
- **Khóa RSA User A:** Modulus $N_A = \mathbf{31553}$, Public key $e_A = \mathbf{125}$, Private key $d_A = \mathbf{30689}$.
- **Chứng chỉ CA ElGamal (Bài 2.2, $k_E = 185, x_A = 56 + 125 = 181$):** $(r, s) = \mathbf{(591, 158)}$, $v_1 \equiv v_2 \equiv \mathbf{72} \pmod{997}$.
- **Bản mã RSA (Bài 2.3, Thông điệp chính thức $M = 20260$):** $C = 20260^{125} \pmod{31553} = \mathbf{24373}$ (giải mã khôi phục $M = \mathbf{20260}$).
  *(Dự phòng nếu $M = 56$: $C = 56^{125} \pmod{31553} = \mathbf{2365}$)*.
- **Đệm SHA-1 (Bài 3, Thông điệp $l = M = 20260$ bits):** $k = \mathbf{155}$ bit `0`, trường độ dài `0x0000000000004F24`, gồm **40 khối 512-bit**.
  *(Dự phòng nếu $l = 56$ bits: $k = \mathbf{391}$ bit `0`, gồm 1 khối 512-bit)*.
- **Khóa Diffie-Hellman (Bài 4, $a = M = 20260, b = C = 24373$):**
  - **Biến thể A ($p = 27361, \alpha = 6$):** $k_A = \mathbf{12}$, $k_B = \mathbf{3268}$, Khóa phiên chung $k_{AB} = \mathbf{20184}$.
  - **Biến thể B ($p = 51907, \alpha = 6$):** $k_A = \mathbf{13196}$, $k_B = \mathbf{25141}$, Khóa phiên chung $k_{AB} = \mathbf{22981}$.
  *(Dự phòng nếu $a = 56, b = 2365$: Biến thể A ra $k_A = 2474, k_B = 5253, k_{AB} = 15552$)*.
- **Ghi chú bẫy $k_E = 105$:** $\gcd(105, 996) = 3 \ne 1 \implies$ vô nghiệm $s$ (do nét in mờ nhìn nhầm số 185).

<a id="3-danh-muc-cac-thuat-toan-mat-ma-lap-trinh-chuan-trong-thu-muc-code"></a>
### 3. Danh Mục Các Thuật Toán Mật Mã Lập Trình Chuẩn Trong Thư Mục `code/`
Toàn bộ mọi tính toán, thuật toán, bài tập trong Slide, Labwork và Đề thi đều được lập trình thành **28 script Python độc lập, chuẩn hóa học thuật** đặt tại thư mục [`code/`](code/) kèm master script [`run_all_crypto_algorithms.py`](code/run_all_crypto_algorithms.py) xác thực 100% tự động:

#### A. Nền tảng Số học Modulo & Đại số
| Script | Thuật toán / Tính toán | Ý nghĩa & Ứng dụng |
| :--- | :--- | :--- |
| [`modular_arithmetic.py`](code/modular_arithmetic.py) | **Phép toán Modulo & Bảng Cayley** | Cộng, trừ, nhân, lũy thừa modulo, sinh bảng Cayley cho $\mathbb{Z}_m$. |
| [`euclidean_gcd.py`](code/euclidean_gcd.py) | **Thuật toán Euclid tìm GCD** | Tìm ước chung lớn nhất từng bước chia Euclid (Giải Lab 2 Bài 1: $\gcd(61430, 52698) = 2$). |
| [`extended_euclidean.py`](code/extended_euclidean.py) | **Euclid mở rộng & Nghịch đảo Modulo** | Tìm hệ số Bézout $a\cdot s + b\cdot t = \gcd(a, b)$ và $a^{-1} \pmod m$ (Lab 2 Bài 4: $65537^{-1} \pmod{35256} = 32393$). |
| [`euler_totient_coprime.py`](code/euler_totient_coprime.py) | **Hàm Phi Euler $\Phi(m)$ & Cặp Coprime** | Phân tích thừa số nguyên tố, tính $\Phi(m)$ và lọc 22 cặp nguyên tố cùng nhau trong Tập $A$ (Lab 2 Bài 2). |
| [`square_and_multiply.py`](code/square_and_multiply.py) | **Thuật toán Bình phương và Nhân** | Lũy thừa modulo nhanh $O(\log e)$ kèm bảng vết từng bit (Lab 2 Bài 3: $8^{5625} \pmod 7 = 1$). |
| [`string_integer_conversion.py`](code/string_integer_conversion.py) | **Chuyển đổi Chuỗi $\leftrightarrow$ Số nguyên Big-Endian** | Mã hóa chuỗi ASCII sang số nguyên cơ số 256 và ngược lại (Lab 3 Bài 1 & 2: `"flow"` $\leftrightarrow 1718382455$). |

#### B. Mật mã Cổ điển (Classical Ciphers)
| Script | Thuật toán / Tính toán | Ý nghĩa & Ứng dụng |
| :--- | :--- | :--- |
| [`caesar_cipher.py`](code/caesar_cipher.py) | **Mật mã Caesar (Dịch chuyển)** | Mã hóa, giải mã theo khóa $k$ và phá mã vét cạn (brute-force) toàn bộ 26 khóa. |
| [`affine_cipher.py`](code/affine_cipher.py) | **Mật mã Affine ($ax + b \pmod{26}$)** | Kiểm tra tính khả nghịch $\gcd(a, 26)=1$, tìm $a^{-1} \pmod{26}$, mã hóa và giải mã. |
| [`vigenere_cipher.py`](code/vigenere_cipher.py) | **Mật mã Đa bảng Vigenère** | Mã hóa và giải mã với từ khóa lặp, tra bảng Tabula Recta. |

#### C. Mật mã Dòng (Stream Ciphers)
| Script | Thuật toán / Tính toán | Ý nghĩa & Ứng dụng |
| :--- | :--- | :--- |
| [`binary_xor_stream.py`](code/binary_xor_stream.py) | **XOR Stream & One-Time Pad** | Chuyển đổi nhị phân 8-bit, mã hóa/giải mã XOR dòng khóa byte (Lab 1 Bài 1, 2, 3). |
| [`a51_stream_cipher.py`](code/a51_stream_cipher.py) | **Mật mã dòng GSM A5/1** | 3 thanh ghi LFSR, hàm bỏ phiếu đa số majority rule, sinh 10 bit dòng khóa (cả 2 phương án clocking). |
| [`rc4_stream_cipher.py`](code/rc4_stream_cipher.py) | **Mật mã dòng RC4** | Khởi tạo hoán vị KSA (256 bytes) và sinh dòng khóa giả ngẫu nhiên byte-by-byte PRGA. |

#### D. Mật mã Khối & Chế độ Vận hành (Block Ciphers & Modes)
| Script | Thuật toán / Tính toán | Ý nghĩa & Ứng dụng |
| :--- | :--- | :--- |
| [`des_sbox_lookup.py`](code/des_sbox_lookup.py) | **Tra cứu Hộp S-Box $S_1$ DES** | Tra cứu hộp phi tuyến $S_1$ của DES cho MSV 056 ($56_{10} = 111000_2 \to \text{Hàng } 2, \text{Cột } 12 \to \mathbf{3}$). |
| [`des_feistel_cipher.py`](code/des_feistel_cipher.py) | **Mạng Feistel 16 vòng DES** | Kiến trúc Feistel, tính khả nghịch của giải mã độc lập với hàm $F$, sinh 16 khóa vòng. |
| [`aes_galois_field.py`](code/aes_galois_field.py) | **Số học Galois $GF(2^8)$ & Hộp S-Box AES** | Phép nhân đa thức modulo $x^8+x^4+x^3+x+1$, phép nhân `xtime`, nghịch đảo trường và biến đổi Affine S-Box. |
| [`block_cipher_modes.py`](code/block_cipher_modes.py) | **5 Chế độ vận hành NIST** | Triển khai và so sánh ECB, CBC (với IV), CFB, OFB, CTR và cơ chế đệm PKCS#7. |

#### E. Mật mã Khóa Công khai & Chữ ký Số
| Script | Thuật toán / Tính toán | Ý nghĩa & Ứng dụng |
| :--- | :--- | :--- |
| [`rsa_key_generation.py`](code/rsa_key_generation.py) | **Tạo khóa RSA ($p=139, q=227$)** | Tính $N, \Phi(N)$, sàng lọc số mũ công khai $e=125$, tính khóa bí mật $d=30689$. |
| [`rsa_encryption_decryption.py`](code/rsa_encryption_decryption.py) | **Mã hóa / Giải mã RSA** | Mã hóa $C \equiv M^e \pmod N$ và giải mã $M \equiv C^d \pmod N$ cho $M=56 \to C=2365$. |
| [`pki_rsa_certificate.py`](code/pki_rsa_certificate.py) | **Chứng chỉ số PKI RSA** | Cấp chứng chỉ định danh người dùng bằng chữ ký RSA của CA (Đề 2024–2025: $S_{\text{CA}}=11273$). |
| [`diffie_hellman_key_exchange.py`](code/diffie_hellman_key_exchange.py) | **Trao đổi Khóa Diffie-Hellman** | Tính khóa công khai $k_A, k_B$ và suy dẫn khóa phiên chung $k_{AB}$ cho cả 2 biến thể đề thi. |
| [`dhke_mitm_attack.py`](code/dhke_mitm_attack.py) | **Tấn công Man-in-the-Middle DHKE** | Mô phỏng kẻ tấn công Eve chặn bắt, can thiệp và thiết lập 2 khóa phiên độc lập với Alice và Bob. |
| [`elgamal_digital_signature.py`](code/elgamal_digital_signature.py) | **Chữ ký số ElGamal** | Ký số của CA trên $x_A=181$ ($k_E=185 \implies r=591, s=158, v_1=v_2=72$), phân tích bẫy toán học đề thi $k_E=105$. |
| [`dsa_digital_signature.py`](code/dsa_digital_signature.py) | **Thuật toán Chữ ký số Chuẩn DSA** | Sinh chữ ký $(r, s)$ và thuật toán xác minh $v == r$ (Slide 12: $p=59, q=29, \alpha=3$). |

#### F. Hàm Băm & Mã Xác thực Thông điệp (Hash & MAC)
| Script | Thuật toán / Tính toán | Ý nghĩa & Ứng dụng |
| :--- | :--- | :--- |
| [`sha1_padding_preprocess.py`](code/sha1_padding_preprocess.py) | **Quy trình Đệm SHA-1** | Tính số bit 0 đệm ($k=155$ cho $l=20260$ bits, $k=391$ cho $l=56$ bits) và số khối $L$. |
| [`sha1_compression_function.py`](code/sha1_compression_function.py) | **Hàm nén 80 vòng SHA-1** | Mở rộng 16 từ lên 80 từ $W_t$, thực hiện 80 vòng nén cập nhật biến trạng thái $(A,B,C,D,E)$. |
| [`block_cipher_hash.py`](code/block_cipher_hash.py) | **Hàm băm từ Mã khối** | Cấu trúc nén Davies-Meyer, Matyas-Meyer-Oseas (MMO) và Miyaguchi-Preneel. |
| [`birthday_attack_collision.py`](code/birthday_attack_collision.py) | **Tấn công Sinh nhật (Birthday Attack)** | Phân tích xác suất đụng độ hàm băm $k \approx 1.1774 \cdot 2^{m/2}$, mô phỏng Monte Carlo va chạm. |
| [`hmac_sha1.py`](code/hmac_sha1.py) | **Mã xác thực thông điệp HMAC-SHA1** | Cấu trúc $H((K \oplus opad) \parallel H((K \oplus ipad) \parallel M))$ theo chuẩn RFC 2104. |
| [`session_slide_exercises.py`](code/session_slide_exercises.py) | **Toàn Bộ Bài Tập Slide Bài Giảng (Session 1–8)** | Giải chi tiết và tự động xác thực toàn bộ các bài tập, ví dụ tính toán xuất hiện trong 8 buổi học lý thuyết. |

#### G. Script Khởi chạy Tự động Tất cả Thuật toán
```powershell
python code/run_all_crypto_algorithms.py
```
Kết quả thực thi tự động: **30/30 scripts PASSED 100%** trong thời gian ~1.0 giây.
