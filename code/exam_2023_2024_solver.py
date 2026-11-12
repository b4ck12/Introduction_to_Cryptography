# -*- coding: utf-8 -*-
"""
=============================================================================
Course: Introduction to Cryptography (USTH) - ICT3.001
Official Final Exam 2023-2024 (Thursday, 30 November 2023)
Exam Code: 00 | Lecturer: Nguyen Minh Huong
Student ID: 23BA14056 (x = 56)
=============================================================================
Complete automated solver for BOTH Question Set 01 and Question Set 02.
=============================================================================
"""

import math
import sys

def solve_question_0(student_id_str="23BA14056"):
    print("=" * 80)
    print("0. IMPORTANT QUESTION: (3/20 ĐIỂM) - TRA CỨU S-BOX DES & CHỌN ĐỀ THI")
    print("=" * 80)
    digits = "".join(filter(str.isdigit, student_id_str))
    last3 = int(digits[-3:]) if len(digits) >= 3 else int(digits)
    x = last3 % 64
    bin_6bit = f"{x:06b}"
    b1, b2, b3, b4, b5, b6 = [int(c) for c in bin_6bit]
    row = (b1 << 1) | b6
    col = (b2 << 3) | (b3 << 2) | (b4 << 1) | b5

    s1_table = [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ]

    out_val = s1_table[row][col]
    out_bin = f"{out_val:04b}"
    is_even = (out_val % 2 == 0)
    chosen_set = "Question set 02" if is_even else "Question set 01"

    print(f"[*] Mã sinh viên : {student_id_str}")
    print(f"[*] 3 chữ số cuối: {last3:03d}")
    print(f"[*] Tính số x   : x = {last3} mod 64 = {x}")
    print(f"[*] Dạng nhị phân 6-bit: {bin_6bit}_2 (b1={b1}, b2={b2}, b3={b3}, b4={b4}, b5={b5}, b6={b6})")
    print(f"[*] Chỉ số Hàng  : r = (b1 b6)_2 = ({b1}{b6})_2 = {row}")
    print(f"[*] Chỉ số Cột   : c = (b2 b3 b4 b5)_2 = ({b2}{b3}{b4}{b5})_2 = {col}")
    print(f"[*] Tra bảng S1  : S_1[row={row}][col={col}] = {out_val} (Nhị phân 4-bit: {out_bin}_2)")
    print(f"[*] Nhận xét     : {out_val} là SỐ {'CHẴN (EVEN)' if is_even else 'LẺ (ODD)'}")
    print(f"===> KẾT LUẬN CHỌN ĐỀ: {chosen_set.upper()}")
    print("=" * 80)
    return chosen_set, out_val


def solve_sha1_padding(l):
    print("\n" + "=" * 80)
    print(f"1. HASH FUNCTIONS (4/20 ĐIỂM) - SHA-1 PADDING CHO l = {l} BITS")
    print("=" * 80)
    rem = (l + 1) % 512
    k = (448 - rem) % 512
    total_len = l + 1 + k + 64
    num_blocks = total_len // 512

    print(f"[BƯỚC 1] Quy tắc đệm chuẩn SHA-1 (FIPS PUB 180-1 / RFC 3174):")
    print(f"    - Thông điệp gốc gồm l = {l} bits.")
    print(f"    - Nối 1 bit '1' vào cuối thông điệp -> độ dài trở thành l + 1 = {l + 1} bits.")
    print(f"    - Nối k bit '0' sao cho: (l + 1 + k) ≡ 448 (mod 512).")
    print(f"    - Thay số: ({l + 1} + k) ≡ 448 (mod 512) => ({rem} + k) = 448 => k = {k} bit '0'.")
    print(f"    - Nối thêm trường độ dài 64-bit biểu diễn số l ({l} dạng nhị phân big-endian).")
    print(f"    - Chiều dài sau đệm: {l} + 1 + {k} + 64 = {total_len} bits.")
    print(f"    - Số khối 512-bit: N = {total_len} / 512 = {num_blocks} khối (M_1, ..., M_{num_blocks}).")

    print(f"\n[BƯỚC 2] Biểu diễn 64-bit chiều dài l = {l}:")
    print(f"    - Thập phân: {l}")
    print(f"    - Thập lục phân (Hex): 0x{l:016x}")
    print(f"    - Nhị phân 64-bit    : {l:064b}")

    print(f"\n[BƯỚC 3] Mô tả định dạng các khối M_1 đến M_{num_blocks}:")
    for i in range(num_blocks):
        start = i * 512
        end = (i + 1) * 512 - 1
        if end < l:
            print(f"    Khối M_{i+1} (bit {start:4d}..{end:4d}): Chứa toàn bộ 512 bit thông điệp gốc.")
        elif start < l:
            msg_remain = l - start
            print(f"    Khối M_{i+1} (bit {start:4d}..{end:4d}): Chứa {msg_remain} bit gốc cuối + 1 bit '1' + {k} bit '0' + 64 bit độ dài.")
        else:
            print(f"    Khối M_{i+1} (bit {start:4d}..{end:4d}): Chứa bit '0' và trường độ dài.")
    return total_len, num_blocks


def solve_dhke(p, alpha, a, b):
    print("\n" + "=" * 80)
    print(f"2. DIFFIE-HELLMAN KEY EXCHANGE (4/20 ĐIỂM) - p = {p}, alpha = {alpha}")
    print("=" * 80)
    print(f"Tham số hệ thống: Số nguyên tố p = {p}, phần tử sinh alpha = {alpha}")
    print(f"Số bí mật tự chọn: Alice chọn a = {a}, Bob chọn b = {b}")

    kA = pow(alpha, a, p)
    kB = pow(alpha, b, p)
    kAB_Alice = pow(kB, a, p)
    kAB_Bob = pow(kA, b, p)

    print(f"\n[BƯỚC 1] Alice tính khóa công khai k_A:")
    print(f"    k_A = alpha^a mod p = {alpha}^{a} mod {p} = {kA}")

    print(f"\n[BƯỚC 2] Bob tính khóa công khai k_B:")
    print(f"    k_B = alpha^b mod p = {alpha}^{b} mod {p} = {kB}")

    print(f"\n[BƯỚC 3] Tính khóa phiên bí mật chung k_AB:")
    print(f"    - Alice tính: k_AB = (k_B)^a mod p = {kB}^{a} mod {p} = {kAB_Alice}")
    print(f"    - Bob tính  : k_AB = (k_A)^b mod p = {kA}^{b} mod {p} = {kAB_Bob}")
    print(f"    - Kiểm tra  : {kAB_Alice} == {kAB_Bob} => Khóa chung trùng khớp hoàn toàn!")
    print(f"===> ĐÁP SỐ: k_A = {kA}, k_B = {kB}, k_AB = {kAB_Alice}")
    return kA, kB, kAB_Alice


def solve_elgamal_and_ca(p, alpha, d, x, ke, ver_list, kA, kB, keA, keB):
    print("\n" + "=" * 80)
    print(f"3. ELGAMAL DIGITAL SIGNATURE & CA (9/20 ĐIỂM) - p = {p}, alpha = {alpha}, d = {d}")
    print("=" * 80)
    beta = pow(alpha, d, p)
    print(f"Khóa bí mật Bob : d = {d}")
    print(f"Khóa công khai  : beta = alpha^d mod p = {alpha}^{d} mod {p} = {beta}")
    print(f"K_pub = (p = {p}, alpha = {alpha}, beta = {beta})")

    # 3.1 Sign x, ke
    print(f"\n--- 3.1 TÍNH CẶP CHỮ KÝ (r, s) CHO x = {x}, k_E = {ke} ---")
    gcd_ke = math.gcd(ke, p - 1)
    print(f"[BƯỚC 1] Kiểm tra điều kiện khả nghịch gcd(k_E, p-1):")
    print(f"    gcd({ke}, {p-1}) = {gcd_ke} => {'HỢP LỆ (nguyên tố cùng nhau)' if gcd_ke == 1 else 'KHÔNG TỒN TẠI NGHỊCH ĐẢO'}")
    ke_inv = pow(ke, -1, p - 1)
    print(f"    k_E^(-1) mod {p-1} = {ke_inv}")

    print(f"[BƯỚC 2] Tính r = alpha^k_E mod p:")
    r = pow(alpha, ke, p)
    print(f"    r = {alpha}^{ke} mod {p} = {r}")

    print(f"[BƯỚC 3] Tính s = (x - d * r) * k_E^(-1) mod (p - 1):")
    diff = x - d * r
    s = (diff * ke_inv) % (p - 1)
    print(f"    x - d * r = {x} - {d} * {r} = {diff}")
    print(f"    s = ({diff} * {ke_inv}) mod {p-1} = {s}")
    print(f"===> CẶP CHỮ KÝ: (r = {r}, s = {s})")

    print(f"[BƯỚC 4] Xác thực chữ ký:")
    v1 = (pow(beta, r, p) * pow(r, s, p)) % p
    v2 = pow(alpha, x, p)
    print(f"    v1 = beta^r * r^s mod p = ({beta}^{r} * {r}^{s}) mod {p} = {v1}")
    print(f"    v2 = alpha^x mod p = {alpha}^{x} mod {p} = {v2}")
    print(f"    v1 == v2 ({v1} == {v2}) => {'CHỮ KÝ HỢP LỆ!' if v1 == v2 else 'CHỮ KÝ KHÔNG HỢP LỆ!'}")

    # 3.2 Verify received messages
    print(f"\n--- 3.2 KIỂM TRA 2 THÔNG ĐIỆP NHẬN ĐƯỢC CÓ PHẢI TỪ BOB KHÔNG ---")
    for idx, (xi, ri, si) in enumerate(ver_list, start=1):
        v1i = (pow(beta, ri, p) * pow(ri, si, p)) % p
        v2i = pow(alpha, xi, p)
        match = (v1i == v2i)
        print(f"Thông điệp {idx}: (x_{idx}={xi}, r_{idx}={ri}, s_{idx}={si})")
        print(f"    v1 = ({beta}^{ri} * {ri}^{si}) mod {p} = {v1i}")
        print(f"    v2 = {alpha}^{xi} mod {p} = {v2i}")
        print(f"    Kết luận: v1 {'==' if match else '!='} v2 ({v1i} vs {v2i}) => {'[+] DO BOB KÝ (HỢP LỆ)' if match else '[-] KHÔNG PHẢI TỪ BOB (HOẶC BỊ GIẢ MẠO / LỖI THAM SỐ)'}")

    # 3.3 CA Certifications
    print(f"\n--- 3.3 CẤP VÀ XÁC THỰC CHỨNG CHỈ SỐ CA CHO ALICE & BOB ---")
    # Alice
    xA = 4 * kA + 1
    print(f"[+] Alice:")
    print(f"    - Khóa DHKE k_A = {kA}, ID(A) = 1")
    print(f"    - Thông điệp cần CA ký: x_A = 4 * k_A + ID(A) = 4 * {kA} + 1 = {xA}")
    print(f"    - Khóa tạm k_E-A = {keA}, gcd({keA}, {p-1}) = {math.gcd(keA, p-1)}")
    keA_inv = pow(keA, -1, p - 1)
    rA = pow(alpha, keA, p)
    sA = ((xA - d * rA) * keA_inv) % (p - 1)
    print(f"    - Chữ ký CA cho Alice Cert_A: r_A = {rA}, s_A = {sA}")
    v1_A = (pow(beta, rA, p) * pow(rA, sA, p)) % p
    v2_A = pow(alpha, xA, p)
    print(f"    - Xác thực Cert_A: v1 = {v1_A}, v2 = {v2_A} => {'HỢP LỆ' if v1_A == v2_A else 'KHÔNG HỢP LỆ'}")

    # Bob
    xB = 4 * kB + 2
    print(f"\n[+] Bob:")
    print(f"    - Khóa DHKE k_B = {kB}, ID(B) = 2")
    print(f"    - Thông điệp cần CA ký: x_B = 4 * k_B + ID(B) = 4 * {kB} + 2 = {xB}")
    print(f"    - Khóa tạm k_E-B = {keB}, gcd({keB}, {p-1}) = {math.gcd(keB, p-1)}")
    keB_inv = pow(keB, -1, p - 1)
    rB = pow(alpha, keB, p)
    sB = ((xB - d * rB) * keB_inv) % (p - 1)
    print(f"    - Chữ ký CA cho Bob Cert_B: r_B = {rB}, s_B = {sB}")
    v1_B = (pow(beta, rB, p) * pow(rB, sB, p)) % p
    v2_B = pow(alpha, xB, p)
    print(f"    - Xác thực Cert_B: v1 = {v1_B}, v2 = {v2_B} => {'HỢP LỆ' if v1_B == v2_B else 'KHÔNG HỢP LỆ'}")


if __name__ == "__main__":
    print("=" * 80)
    print("GIẢI ĐỀ THI CUỐI KỲ ICT3.001 - NĂM HỌC 2023-2024 (THỨ NĂM, 30/11/2023)")
    print("=" * 80)

    # 0. Question 0 for Student ID 23BA14056
    chosen_set, s1_out = solve_question_0("23BA14056")

    print("\n\n" + "#" * 80)
    print("PHẦN 1: LỜI GIẢI CHI TIẾT QUESTION SET 01 (S-BOX ODD / ĐỀ CHÍNH THỨC)")
    print("#" * 80)
    solve_sha1_padding(2096)
    kA1, kB1, kAB1 = solve_dhke(863, 2, 2023, 2024)
    solve_elgamal_and_ca(
        p=863, alpha=2, d=127, x=30, ke=215,
        ver_list=[(40, 306, 64), (55, 306, 465)],
        kA=kA1, kB=kB1, keA=213, keB=211
    )

    print("\n\n" + "#" * 80)
    print("PHẦN 2: LỜI GIẢI CHI TIẾT QUESTION SET 02 (S-BOX EVEN / ĐỀ MỞ RỘNG)")
    print("#" * 80)
    solve_sha1_padding(2225)
    kA2, kB2, kAB2 = solve_dhke(593, 2, 2023, 2024)
    solve_elgamal_and_ca(
        p=593, alpha=2, d=127, x=30, ke=215,
        ver_list=[(42, 306, 64), (50, 306, 465)],
        kA=kA2, kB=kB2, keA=213, keB=211
    )
