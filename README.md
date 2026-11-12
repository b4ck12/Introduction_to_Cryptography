# Introduction to Cryptography (USTH - ICT3.08E / ICT3.001)

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Test Suite](https://img.shields.io/badge/Tests-29%2F29%20Passed-brightgreen.svg)](code/run_all_crypto_algorithms.py)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![USTH ICT](https://img.shields.io/badge/USTH-ICT%20Department-red.svg)](https://usth.edu.vn/)

Comprehensive educational repository and algorithmic implementation suite for **Introduction to Cryptography**, offered by the Department of Information and Communication Technology (ICT) at the **University of Science and Technology of Hanoi (USTH)**.

---

## 📌 Repository Overview

This repository provides an end-to-end companion for theoretical lectures, laboratory assignments, and examination preparation:

1. **[`code/`](code/)**: **29 Standalone Python 3 Scripts** covering every single algorithm and mathematical calculation taught in the course. Requires **zero external dependencies** (standard Python library only).
2. **[`test.md`](test.md)**: Exhaustive examination archive with full step-by-step mathematical solutions for **Final Exam 2025–2026** and **Final Exam 2024–2025**, tailored for Student ID `23BA14056` ($x = a = M = 56$).
3. **[`DOC.md`](DOC.md)**: In-depth English textbook companion with mathematical derivations, security proofs, trace tables, and cross-references (164 headings, 100% verified anchors).
4. **[`DOC_VN.md`](DOC_VN.md)**: Tài liệu hướng dẫn ôn tập toàn diện tiếng Việt (98 đề mục, liên kết chuẩn xác).
5. **Course Materials**: Official lecture slides (`session1.pdf` to `Session8.pdf`), labwork assignments (`Lab1.pdf`, `Lab2.pdf`, `Lab3.pdf`), and scanned exam papers.

---

## 🚀 Quick Start & Hướng dẫn Sử dụng Nhanh

### 0. Cách Chạy Ngay Lập Tức (Không cần cài đặt, Clone về là chạy)
Ngay tại thư mục gốc của repository đã có sẵn file thực thi độc lập:
* **Cách 1**: Double-click trực tiếp vào file **`USTH_Cryptography_Tool.exe`** (hoặc chạy **`Run_App.bat`**).
* **Cách 2**: Chạy từ Command Prompt / PowerShell:
```powershell
.\USTH_Cryptography_Tool.exe
```
> [!TIP]
> Ứng dụng là phiên bản **Release tối ưu hóa (chỉ 4.5 MB)**, khởi động tức thì, hoạt động 100% offline, không yêu cầu Node.js hay Rust để chạy. Chỉ cần máy có Python tiêu chuẩn (sẵn có trên Windows/Linux/macOS).

---

### 1. Hướng Dẫn Sử Dụng Giao Diện Desktop GUI
1. **Tìm kiếm & Chọn Thuật Toán:**
   * Dùng thanh tìm kiếm ở góc trên bên trái (hoặc bấm danh mục ở cột bên trái: *Modular Arithmetic, Classical Ciphers, Stream Ciphers, Block Ciphers, Asymmetric Cryptography, Signatures & Hash*).
   * Hỗ trợ tìm kiếm nhanh theo tên tiếng Anh lẫn tiếng Việt (ví dụ: `rsa`, `dhke`, `elgamal`, `sbox`, `euclid`, `modulo`).
2. **Nạp Tham Số Đầu Vào:**
   * Bấm nút **"Load Defaults"** để tự động điền sẵn tham số đề thi USTH chuẩn cho Mã sinh viên `23BA14056` ($x = 56$).
   * Hoặc bấm vào các nút **Quick Presets / Solvers** ở dưới cùng để nạp tức thì các bộ số của Đề thi 2025–2026, Đề thi 2023–2024, Slide bài giảng.
   * Có thể tự do sửa bất kỳ số nào theo đề bài thi thực tế.
3. **Xem Lời Giải Chi Tiết Từng Bước (Visual Steps) & Đáp Án Nhanh:**
   * Bấm **"Calculate & Solve"** (hoặc Enter).
   * **Hero Answer Card (Banner trên cùng):** Hiển thị ngay đáp số cốt lõi (ví dụ: Bản mã $C$, Khóa phiên $k_{AB}$, Cặp chữ ký $(r, s)$) cùng nút **"Copy Answer"** để tra soát nhanh cuối giờ thi.
   * **Visual Steps (Từng bước chi tiết):** Hiển thị công thức toán học (`.math-formula-box`), các bước tính nhẩm trung gian (`.calc-substep`), bảng vết thuật toán (`.calc-table` cho Euclid mở rộng, Square-and-Multiply) và huy hiệu xác minh (`.verify-badge`).
   * **Tab "Raw Essay Text":** Xem toàn bộ văn bản thuần để chép vào bài thi tự luận.
   * **Nút "Copy for Exam":** Copy 1-click toàn bộ bài giải chi tiết vào clipboard.

---

### 2. Chạy Bằng Dòng Lệnh Python (CLI) Cho Từng Bài Thi
Toàn bộ 31 thuật toán trong thư mục `code/` đều chạy độc lập không cần thư viện ngoài:
```powershell
# Chạy tương tác (tự hỏi nhập tham số nếu không truyền đối số):
python code/rsa_encryption_decryption.py

# Truyền trực tiếp tham số đề bài (Ví dụ: M=20260, e=125, N=31553, d=30689):
python code/rsa_encryption_decryption.py 20260 125 31553 30689

# Tính Diffie-Hellman (p=27361, alpha=6, a=20260, b=24372):
python code/diffie_hellman_key_exchange.py 27361 6 20260 24372

# Tính Chữ ký ElGamal (p=997, alpha=6, d=25, k_E=185, x=181):
python code/elgamal_digital_signature.py 997 6 25 185 181

# Chạy kiểm thử toàn bộ 31 thuật toán (Verify All Tests):
python code/run_all_crypto_algorithms.py
```
*Expected Output:*
```text
================================================================================
USTH CRYPTOGRAPHY - MASTER ALGORITHM & CALCULATION RUNNER
Student ID: 23BA14056 (x = 56)
Total Standalone Algorithm Scripts: 29
================================================================================
Idx  | Filename                       | Status   | Elapsed 
------------------------------------------------------------
1    | modular_arithmetic.py          | [OK]     | 0.025s
2    | euclidean_gcd.py               | [OK]     | 0.024s
3    | extended_euclidean.py          | [OK]     | 0.040s
4    | euler_totient_coprime.py       | [OK]     | 0.039s
5    | square_and_multiply.py         | [OK]     | 0.040s
6    | string_integer_conversion.py   | [OK]     | 0.025s
7    | caesar_cipher.py               | [OK]     | 0.043s
8    | affine_cipher.py               | [OK]     | 0.048s
9    | vigenere_cipher.py             | [OK]     | 0.025s
10   | binary_xor_stream.py           | [OK]     | 0.041s
11   | a51_stream_cipher.py           | [OK]     | 0.025s
12   | rc4_stream_cipher.py           | [OK]     | 0.039s
13   | des_sbox_lookup.py             | [OK]     | 0.025s
14   | des_feistel_cipher.py          | [OK]     | 0.040s
15   | aes_galois_field.py            | [OK]     | 0.040s
16   | block_cipher_modes.py          | [OK]     | 0.040s
17   | rsa_key_generation.py          | [OK]     | 0.024s
18   | rsa_encryption_decryption.py   | [OK]     | 0.025s
19   | pki_rsa_certificate.py         | [OK]     | 0.024s
20   | diffie_hellman_key_exchange.py | [OK]     | 0.024s
21   | dhke_mitm_attack.py            | [OK]     | 0.026s
22   | elgamal_digital_signature.py   | [OK]     | 0.025s
23   | dsa_digital_signature.py       | [OK]     | 0.041s
24   | sha1_padding_preprocess.py     | [OK]     | 0.024s
25   | sha1_compression_function.py   | [OK]     | 0.041s
26   | block_cipher_hash.py           | [OK]     | 0.042s
27   | birthday_attack_collision.py   | [OK]     | 0.041s
28   | hmac_sha1.py                   | [OK]     | 0.046s
29   | session_slide_exercises.py     | [OK]     | 0.026s
------------------------------------------------------------
Total Scripts: 29 | Passed: 29 | Failed: 0
Total Execution Time: ~0.95 seconds
================================================================================
```

---

## 📂 Algorithm Catalog

> [!TIP]
> **Going to an exam with different numbers?**
> - Run **[`code/exam_calculator.py`](code/exam_calculator.py)** to launch the interactive all-in-one exam solver menu.
> - Or run any individual script below with **`-i`** (e.g., `python code/rsa_key_generation.py -i`) to input your specific exam parameters directly.

Every script is completely self-contained, documented, and parameterized. You can run scripts with default student parameters, input custom numbers interactively, or supply arguments via command line.

### A. Number Theory & Foundations
| Script | Algorithm / Topic | Description & CLI Example |
| :--- | :--- | :--- |
| [`code/modular_arithmetic.py`](code/modular_arithmetic.py) | **Modular Arithmetic & Cayley Tables** | Computes addition, subtraction, multiplication, modular powers, and prints group Cayley tables for $\mathbb{Z}_m$.<br>`python code/modular_arithmetic.py` |
| [`code/euclidean_gcd.py`](code/euclidean_gcd.py) | **Euclidean Algorithm for GCD** | Step-by-step division algorithm finding $\gcd(a, b)$. Solves Lab 2 Ex 1: $\gcd(61430, 52698) = 2$.<br>`python code/euclidean_gcd.py` |
| [`code/extended_euclidean.py`](code/extended_euclidean.py) | **Extended Euclidean Algorithm (EEA)** | Calculates Bézout coefficients $a \cdot s + b \cdot t = \gcd(a, b)$ and modular inverse $a^{-1} \pmod m$. Solves Lab 2 Ex 4 ($65537^{-1} \pmod{35256} = 32393$).<br>`python code/extended_euclidean.py` |
| [`code/euler_totient_coprime.py`](code/euler_totient_coprime.py) | **Euler's Totient $\Phi(m)$ & Coprimes** | Prime factorization, totient calculation, and pairwise coprime filter for Set $A$ (Lab 2 Ex 2, 22 coprime pairs).<br>`python code/euler_totient_coprime.py` |
| [`code/square_and_multiply.py`](code/square_and_multiply.py) | **Fast Exponentiation (Square & Multiply)** | $O(\log e)$ exponentiation trace table for $x^e \pmod n$. Solves Lab 2 Ex 3 ($8^{5625} \pmod 7 = 1$) and Session 6 Slide 11 ($5^{23} \pmod{33} = 26$).<br>`python code/square_and_multiply.py` |
| [`code/string_integer_conversion.py`](code/string_integer_conversion.py) | **ASCII $\leftrightarrow$ Big-Endian Integer** | Base-256 Big-Endian string encoding and decoding. Solves Lab 3 Ex 1 & 2 (`"flow"` $\leftrightarrow 1718382455$).<br>`python code/string_integer_conversion.py` |

### B. Classical & Stream Ciphers
| Script | Algorithm / Topic | Description & CLI Example |
| :--- | :--- | :--- |
| [`code/caesar_cipher.py`](code/caesar_cipher.py) | **Caesar Shift Cipher** | Encryption, decryption, and complete 26-key brute-force cryptanalysis. Auto-detects shift rule for `"ictlab" \to "lfwode"` ($k = 3$).<br>`python code/caesar_cipher.py` |
| [`code/affine_cipher.py`](code/affine_cipher.py) | **Affine Cipher ($ax + b \pmod{26}$)** | Multiplier coprimality validation ($\gcd(a, 26) = 1$, 12 valid keys), inversion $a^{-1} \pmod{26}$, and decryption.<br>`python code/affine_cipher.py` |
| [`code/vigenere_cipher.py`](code/vigenere_cipher.py) | **Vigenère Polyalphabetic Cipher** | Encryption and decryption with repeating keyword schedule and Tabula Recta tracing.<br>`python code/vigenere_cipher.py` |
| [`code/binary_xor_stream.py`](code/binary_xor_stream.py) | **Bitwise XOR Stream & One-Time Pad** | Character-to-binary bit arrays, keystream XOR encryption and decryption, OTP perfect secrecy verification.<br>`python code/binary_xor_stream.py` |
| [`code/a51_stream_cipher.py`](code/a51_stream_cipher.py) | **GSM A5/1 Stream Cipher** | 3 LFSR registers, majority voting clocking rule. Implements both **Option 1 (Official USTH Standard: Output First, Then Step $\implies \mathbf{0100000001}$)** and **Option 2 (Textbook: Shift First $\implies 1000000010$)**.<br>`python code/a51_stream_cipher.py` |
| [`code/rc4_stream_cipher.py`](code/rc4_stream_cipher.py) | **RC4 Stream Cipher** | 256-byte state array Key-Scheduling Algorithm (KSA) and Pseudo-Random Generation Algorithm (PRGA) keystream generator.<br>`python code/rc4_stream_cipher.py` |

### C. Modern Block Ciphers & Operation Modes
| Script | Algorithm / Topic | Description & CLI Example |
| :--- | :--- | :--- |
| [`code/des_sbox_lookup.py`](code/des_sbox_lookup.py) | **DES S-Box $S_1$ Substitution** | Traverses 6-bit input $x = \text{ID} \bmod 64$, determines Row $r$ (outer bits) and Column $c$ (inner 4 bits). For ID 56: Row 2, Col 12 $\to \mathbf{3}$ (`0011`).<br>`python code/des_sbox_lookup.py [student_id]` |
| [`code/des_feistel_cipher.py`](code/des_feistel_cipher.py) | **16-Round DES Feistel Network** | Implements the Feistel structure and mathematically proves decryption invertibility regardless of the round function $F$.<br>`python code/des_feistel_cipher.py` |
| [`code/aes_galois_field.py`](code/aes_galois_field.py) | **AES Galois Field $GF(2^8)$ & S-Box** | Polynomial arithmetic modulo $x^8+x^4+x^3+x+1$ (`0x11B`), `xtime` multiplication, inversion, S-Box affine transformation, and MixColumns MDS matrix.<br>`python code/aes_galois_field.py` |
| [`code/block_cipher_modes.py`](code/block_cipher_modes.py) | **Block Cipher Modes (ECB, CBC, CFB, OFB, CTR)** | Simulates all 5 NIST modes of operation, PKCS#7 padding, and error propagation characteristics.<br>`python code/block_cipher_modes.py` |

### D. Asymmetric Cryptography & Key Exchange
| Script | Algorithm / Topic | Description & CLI Example |
| :--- | :--- | :--- |
| [`code/rsa_key_generation.py`](code/rsa_key_generation.py) | **RSA Key Generation** | Key generation for Exam 2025–2026 ($p=139, q=227, e=125 \implies d=30689$) and Session 6 Textbook ($p=11, q=3, e=3 \implies d=7$).<br>`python code/rsa_key_generation.py` |
| [`code/rsa_encryption_decryption.py`](code/rsa_encryption_decryption.py) | **RSA Cryptosystem (Encrypt / Decrypt)** | Evaluates $C \equiv M^e \pmod N$ and $M \equiv C^d \pmod N$ for personalized ID ($M = 56 \implies C = 2365$) and exam parameter ($M = 20260$).<br>`python code/rsa_encryption_decryption.py [message_int]` |
| [`code/pki_rsa_certificate.py`](code/pki_rsa_certificate.py) | **PKI Digital Certificate (RSA)** | Complete solution for Final Exam 2024–2025: RSA keygen ($e=5525 \implies d=26045$), CA signature on $M=56 \implies S_{\text{CA}} = 11273$, and secure email exchange.<br>`python code/pki_rsa_certificate.py [student_id]` |
| [`code/diffie_hellman_key_exchange.py`](code/diffie_hellman_key_exchange.py) | **Diffie-Hellman Key Exchange (DHKE)** | Computes public keys $k_A, k_B$ and shared secret session key $k_{AB}$ for Exam Variant A ($p=27361, \alpha=7$) and Variant B ($p=51907, \alpha=6$).<br>`python code/diffie_hellman_key_exchange.py [student_id]` |
| [`code/dhke_mitm_attack.py`](code/dhke_mitm_attack.py) | **Man-in-the-Middle (MitM) Attack Simulation** | Demonstrates active attacker interception and independent session key derivation for unauthenticated DHKE (Exam and Session 8 Slide 18 with Oscar).<br>`python code/dhke_mitm_attack.py` |

### E. Digital Signatures, Hashes & MACs
| Script | Algorithm / Topic | Description & CLI Example |
| :--- | :--- | :--- |
| [`code/elgamal_digital_signature.py`](code/elgamal_digital_signature.py) | **ElGamal Digital Signature Scheme** | CA signature for Exam 2025–2026 ($x_A = 181, k_E = 107 \implies r=461, s=136$) and Session 7 Slide 8 ($p=29, \alpha=2, d=12, k_E=5$).<br>`python code/elgamal_digital_signature.py [student_id]` |
| [`code/dsa_digital_signature.py`](code/dsa_digital_signature.py) | **Digital Signature Algorithm (DSA)** | Key generation, signature generation $(r, s)$, and verification $v == r$ for Session 7 Slide 12 test vector ($p=59, q=29, \alpha=3, d=7, k_E=10$).<br>`python code/dsa_digital_signature.py` |
| [`code/sha1_padding_preprocess.py`](code/sha1_padding_preprocess.py) | **SHA-1 Padding Preprocessing** | Calculates zero padding bits $k$ and 512-bit block count $L$ for $l = 20260$ bits ($k=155, L=40$) and $l = 56$ bits ($k=391, L=1$).<br>`python code/sha1_padding_preprocess.py [length_bits]` |
| [`code/sha1_compression_function.py`](code/sha1_compression_function.py) | **SHA-1 Compression & Message Schedule** | Expands 16 words to 80 words $W_t$, performs 80 compression rounds updating $(A, B, C, D, E)$. Solves Session 7 Slide 25 ($x = 0^{512}$ vs $x = 0^{511}1$).<br>`python code/sha1_compression_function.py` |
| [`code/block_cipher_hash.py`](code/block_cipher_hash.py) | **Block-Cipher-Based Hashes** | Implements Davies-Meyer, Matyas-Meyer-Oseas (MMO), and Miyaguchi-Preneel compression constructions.<br>`python code/block_cipher_hash.py` |
| [`code/birthday_attack_collision.py`](code/birthday_attack_collision.py) | **Birthday Attack & Collision Bound** | Mathematical bound $k \approx 1.1774 \cdot 2^{m/2}$, standard hash collision security table, and empirical Monte Carlo collision simulation.<br>`python code/birthday_attack_collision.py` |
| [`code/hmac_sha1.py`](code/hmac_sha1.py) | **HMAC-SHA1 Authentication Code** | RFC 2104 / FIPS 198 keyed hashing $H((K \oplus opad) \parallel H((K \oplus ipad) \parallel M))$. Verified against RFC 2202 Test Vector 2.<br>`python code/hmac_sha1.py` |
| [`code/session_slide_exercises.py`](code/session_slide_exercises.py) | **Master Slide Exercise Suite** | Centrally executes and prints mathematical solutions for every single calculation appearing in lecture slides (Sessions 1 to 8).<br>`python code/session_slide_exercises.py` |

---

## 📖 Documentation & Study Guides

- **[`test.md`](test.md)**: Personalized exam solutions for Student ID `23BA14056`:
  - **Problem 1 (DES S-Box):** $x = 56 \to \text{Row } 2, \text{Col } 12 \implies \mathbf{3}$ (`0011`).
  - **Problem 2.1 (RSA Keygen):** $N = 31553, \Phi(N) = 31188, e = 125 \implies d = \mathbf{30689}$.
  - **Problem 2.2 (ElGamal Signature):** Typo proof for $k_E = 105$, valid signature with $k_E = 107 \implies (r = 461, s = 136)$.
  - **Problem 2.3 (RSA Encryption):** $M = 56 \implies C = \mathbf{2365}$, $M = 20260 \implies C = \mathbf{11571}$.
  - **Problem 3 (SHA-1 Padding):** $l = 20260 \implies k = \mathbf{155}$ zero bits, $L = \mathbf{40}$ blocks; $l = 56 \implies k = \mathbf{391}$ zero bits, $L = \mathbf{1}$ block.
  - **Problem 4 (Diffie-Hellman):** Variant A ($p = 27361 \implies k_{AB} = \mathbf{15552}$); Variant B ($p = 51907 \implies k_{AB} = \mathbf{48191}$).
  - **Exam 2024–2025:** RSA keygen ($e = 5525 \implies d = \mathbf{26045}$), CA signature on $M = 56 \implies S_{\text{CA}} = \mathbf{11273}$.
- **[`DOC.md`](DOC.md)**: English course textbook covering symmetric cryptography, stream ciphers, block ciphers, public-key infrastructure, hash functions, MACs, and complete Labwork 1–3 walkthroughs.
- **[`DOC_VN.md`](DOC_VN.md)**: Bản hướng dẫn học tập toàn diện bằng Tiếng Việt với giải thích chi tiết, công thức toán học và bảng vết thuật toán.

---

## 🛠️ System Requirements

- **Operating System:** Windows, macOS, or Linux.
- **Python Version:** Python 3.8 or higher.
- **Dependencies:** None. All scripts use standard library modules (`math`, `sys`, `struct`, `hashlib`, `hmac`, `random`, `time`, `subprocess`).

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
Created for academic and educational purposes at the University of Science and Technology of Hanoi (USTH).
