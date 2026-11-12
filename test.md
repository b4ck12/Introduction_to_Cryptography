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
    - [2.3 MÃ HÓA VÀ GIẢI MÃ THÔNG ĐIỆP VỚI MÃ SV 056 (3/20 ĐIỂM)](#23-ma-hoa-va-giai-ma-thong-iep-voi-ma-sv-056-320-iem)
  - [BÀI 3: QUÁ TRÌNH ĐỆM (PADDING PREPROCESS) CỦA HÀM BĂM SHA-1 (4/20 ĐIỂM)](#bai-3-qua-trinh-em-padding-preprocess-cua-ham-bam-sha-1-420-iem)
  - [BÀI 4: GIAO THỨC TRAO ĐỔI KHÓA DIFFIE-HELLMAN - DHKE (4/20 ĐIỂM)](#bai-4-giao-thuc-trao-oi-khoa-diffie-hellman-dhke-420-iem)
    - [2.1 Lời giải theo Biến thể A: $p = 27361, \alpha = 6$ (Đề thi in trên giấy)](#21-loi-giai-theo-bien-the-a-p-27361-alpha-6-e-thi-in-tren-giay)
    - [2.2 Lời giải theo Biến thể B: $p = 51907, \alpha = 6$ (Đề chiếu lớp học)](#22-loi-giai-theo-bien-the-b-p-51907-alpha-6-e-chieu-lop-hoc)
- [PHẦN III: ĐỀ THI SỐ 2 – HỌC KỲ 2, NĂM HỌC 2024–2025 (60 PHÚT)](#phan-iii-e-thi-so-2-hoc-ky-2-nam-hoc-20242025-60-phut)
  - [BÀI 1.1: TẠO KHÓA RSA ($p = 223, q = 193$) (4/20 ĐIỂM)](#bai-11-tao-khoa-rsa-p-223-q-193-420-iem)
  - [BÀI 1.2: CHỨNG CHỈ SỐ RSA CỦA CA CHO MÃ SV 056 (4/20 ĐIỂM)](#bai-12-chung-chi-so-rsa-cua-ca-cho-ma-sv-056-420-iem)
  - [BÀI 1.3: QUY TRÌNH TRAO ĐỔI EMAIL BẢO MẬT PKI (4/20 ĐIỂM)](#bai-13-quy-trinh-trao-oi-email-bao-mat-pki-420-iem)
- [PHẦN IV: CẨM NANG PHƯƠNG PHÁP TÍNH NHANH TRONG PHÒNG THI](#phan-iv-cam-nang-phuong-phap-tinh-nhanh-trong-phong-thi)
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
### 2.3 MÃ HÓA VÀ GIẢI MÃ THÔNG ĐIỆP VỚI MÃ SV 056 (3/20 ĐIỂM)

> [!TIP]
> **File code giải bài toán:** [`code/rsa_encryption_decryption.py`](code/rsa_encryption_decryption.py)  
> *Lệnh chạy terminal:* `python code/rsa_encryption_decryption.py`

<a id="1-e-bai-3"></a>
#### 1. Đề bài
Sử dụng cặp khóa RSA đã tạo ở Bài 2.1 ($N = 31553, e = 125, d = 30689$), thực hiện mã hóa thông điệp biểu diễn bởi mã sinh viên ($M = 56$) và giải mã để kiểm chứng.

<a id="2-loi-giai-chi-tiet-1"></a>
#### 2. Lời giải chi tiết
1. **Quá trình mã hóa (Encryption):**
   $$C \equiv M^e \pmod N = 56^{125} \pmod{31553}$$
   Áp dụng thuật toán Square-and-Multiply:
   $$C = \mathbf{2365}$$
2. **Quá trình giải mã (Decryption):**
   $$M \equiv C^d \pmod N = 2365^{30689} \pmod{31553} = \mathbf{56}$$
   Bản rõ khôi phục thành công trùng khớp hoàn toàn với thông điệp ban đầu $M = 56$.

> *(Mở rộng: Nếu đề yêu cầu mã hóa thông điệp $M = 20260$ theo năm học:  
> $C = 20260^{125} \pmod{31553} = \mathbf{11571}$, và $11571^{30689} \pmod{31553} = \mathbf{20260}$)*.

---

<a id="bai-3-qua-trinh-em-padding-preprocess-cua-ham-bam-sha-1-420-iem"></a>
## BÀI 3: QUÁ TRÌNH ĐỆM (PADDING PREPROCESS) CỦA HÀM BĂM SHA-1 (4/20 ĐIỂM)

> [!TIP]
> **File code giải bài toán:** [`code/sha1_padding_preprocess.py`](code/sha1_padding_preprocess.py)  
> *Lệnh chạy terminal:* `python code/sha1_padding_preprocess.py`

<a id="1-e-bai-4"></a>
### 1. Đề bài
Trình bày quy tắc đệm thông điệp của chuẩn hàm băm an toàn SHA-1. Áp dụng tính toán cụ thể trường đệm cho thông điệp $x$.

<a id="2-loi-giai-chi-tiet-2"></a>
### 2. Lời giải chi tiết
1. **Quy tắc đệm chuẩn của SHA-1 (`Session7.pdf`, Slide 20):**
   - Giả sử thông điệp ban đầu có độ dài $l$ bits.
   - Thêm bit `1` vào ngay sau thông điệp.
   - Thêm $k$ bit `0` ($0 \le k < 512$) sao cho:
     $$(l + 1 + k) \equiv 448 \pmod{512}$$
     $$k = (448 - 1 - l) \pmod{512} = (447 - l) \pmod{512}$$
   - Nối thêm 64 bit biểu diễn độ dài gốc $l$ ở dạng số nguyên nhị phân không dấu (Big-endian).
   - Tổng độ dài sau khi đệm là bội số nguyên của 512 bit: $L \times 512$ bits.
2. **Áp dụng tính toán cho thông điệp có độ dài $l = 20260$ bits:**
   - $20260 \pmod{512} = 292$ bits.
   - Số bit 0 cần chèn thêm:
     $$k = (447 - 292) = \mathbf{155 \text{ bit 0}}$$
   - Biểu diễn 64 bit của số $20260_{10}$:
     $$20260_{10} = \mathbf{\text{0x0000000000004F24}}$$
   - Tổng chiều dài sau đệm: $20260 + 1 + 155 + 64 = 20480$ bits = $40$ khối $\times 512$ bits.

---

<a id="bai-4-giao-thuc-trao-oi-khoa-diffie-hellman-dhke-420-iem"></a>
## BÀI 4: GIAO THỨC TRAO ĐỔI KHÓA DIFFIE-HELLMAN - DHKE (4/20 ĐIỂM)

> [!TIP]
> **File code giải bài toán:** [`code/diffie_hellman_key_exchange.py`](code/diffie_hellman_key_exchange.py)  
> *Lệnh chạy terminal:* `python code/diffie_hellman_key_exchange.py`  
> *(Xem thêm mã nguồn mô phỏng tấn công MitM tại [`code/dhke_mitm_attack.py`](code/dhke_mitm_attack.py))*

<a id="1-e-bai-5"></a>
### 1. Đề bài
Alice và Bob thực hiện giao thức trao đổi khóa Diffie-Hellman.  
Số bí mật chọn tại mỗi bên:
- Alice chọn: $a = \text{Mã\_SV} = 56$
- Bob chọn: $b = C = 2365$ (với $C$ là bản mã tính được từ Bài 2.3).  
Trình bày các bước tạo khóa công khai và suy dẫn khóa phiên chung $k_{AB}$ cho hai biến thể tham số trong đề thi:
- **Biến thể A (In trên đề thi chính thức `crop_bot.png`):** $p = 27361, \alpha = 6$.
- **Biến thể B (In trên đề chiếu lớp học `869026595...png`):** $p = 51907, \alpha = 6$.

<a id="2-loi-giai-chi-tiet-cho-ma-sv-23ba14056"></a>
### 2. Lời giải chi tiết cho Mã SV 23BA14056

<a id="21-loi-giai-theo-bien-the-a-p-27361-alpha-6-e-thi-in-tren-giay"></a>
#### 2.1 Lời giải theo Biến thể A: $p = 27361, \alpha = 6$ (Đề thi in trên giấy)
1. **Phía Alice:**
   - Alice tính khóa công khai:
     $$k_A = \alpha^a \pmod p = 6^{56} \pmod{27361} = \mathbf{2474}$$
   - Alice gửi $k_A = 2474$ cho Bob.
2. **Phía Bob:**
   - Bob tính khóa công khai:
     $$k_B = \alpha^b \pmod p = 6^{2365} \pmod{27361} = \mathbf{5253}$$
   - Bob gửi $k_B = 5253$ cho Alice.
3. **Tính khóa phiên bí mật chung $k_{AB}$:**
   - **Alice tính:** $k_{AB} = (k_B)^a \pmod p = 5253^{56} \pmod{27361} = \mathbf{15552}$.
   - **Bob tính:** $k_{AB} = (k_A)^b \pmod p = 2474^{2365} \pmod{27361} = \mathbf{15552}$.
   - Khóa phiên chung thống nhất: $\mathbf{k_{AB} = 15552}$.

<a id="22-loi-giai-theo-bien-the-b-p-51907-alpha-6-e-chieu-lop-hoc"></a>
#### 2.2 Lời giải theo Biến thể B: $p = 51907, \alpha = 6$ (Đề chiếu lớp học)
1. **Phía Alice:**
   - Khóa công khai: $k_A = 6^{56} \pmod{51907} = \mathbf{3235}$.
2. **Phía Bob:**
   - Khóa công khai: $k_B = 6^{2365} \pmod{51907} = \mathbf{20853}$.
3. **Tính khóa phiên bí mật chung $k_{AB}$:**
   - Alice tính: $k_{AB} = 20853^{56} \pmod{51907} = \mathbf{48191}$.
   - Bob tính: $k_{AB} = 3235^{2365} \pmod{51907} = \mathbf{48191}$.
   - Khóa phiên chung thống nhất: $\mathbf{k_{AB} = 48191}$.
   - *Mã nguồn kiểm chứng độc lập:* [`code/diffie_hellman_key_exchange.py`](code/diffie_hellman_key_exchange.py).

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

<a id="phan-iv-cam-nang-phuong-phap-tinh-nhanh-trong-phong-thi"></a>
# PHẦN IV: CẨM NANG PHƯƠNG PHÁP TÍNH NHANH TRONG PHÒNG THI

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
### 2. Bảng Tóm Tắt Đáp Số Cho Mã Sinh Viên 23BA14056
- **Đầu vào:** $x = a = M = \mathbf{56}$.
- **Đầu ra Hộp S-box $S_1$:** Hàng 2, Cột 12 $\implies \mathbf{3}$ (nhị phân: $\mathbf{0011_2}$).
- **Khóa RSA:** Modulus $N = \mathbf{31553}$, Public key $e = \mathbf{125}$, Private key $d = \mathbf{30689}$.
- **Bản mã RSA:** $C = \mathbf{2365}$.
- **Khóa Diffie-Hellman:** $k_A = \mathbf{3235}$, $k_B = \mathbf{20853}$, Khóa chung $k_{AB} = \mathbf{48191}$.
- **Chữ ký CA (2024–2025):** $S_{\text{CA}} = \mathbf{11273}$.
- **Chứng chỉ CA ElGamal (2025–2026, $k_E = 185$):** $(r, s) = \mathbf{(591, 158)}$, $v_1 \equiv v_2 \equiv \mathbf{72} \pmod{997}$.
- **Ghi chú bẫy $k_E = 105$:** $\gcd(105, 996) = 3 \ne 1 \implies$ vô nghiệm $s$ (do nhìn nhầm số 185).

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
