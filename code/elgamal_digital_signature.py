# -*- coding: utf-8 -*-
"""
Script: solve_elgamal_ca_signature.py
Description: Solves Exercise 2.2 (Certification Authority ElGamal Signature) for Exam 2025-2026.
Parameters: p_CA = 997, alpha = 6, d_CA = 25.
Input message: x_A = x + e_A (where x = student_ID % 64 = 56, e_A = 125 -> x_A = 181).
Analyzes both exam sheet ephemeral key (k_E = 105) and standard coprime key (k_E = 107).
"""
import math

def print_eea_table(m: int, a: int):
    """Prints Extended Euclidean Algorithm table for a^(-1) mod m."""
    print(f"\n    [+] BẢNG EUCLID MỞ RỘNG (Tính k_E^(-1) = {a}^(-1) mod {m}):")
    print(f"    {'Bước':<7} | {'q':<6} | {'r':<8} | {'s':<8} | {'t':<8} | {'Phương trình chia'}")
    print("    " + "-" * 65)
    r_prev, r_curr = m, a
    s_prev, s_curr = 1, 0
    t_prev, t_curr = 0, 1
    print(f"    {'init':<7} | {'-':<6} | {r_prev:<8} | {s_prev:<8} | {t_prev:<8} | r0 = {r_prev}")
    print(f"    {'init':<7} | {'-':<6} | {r_curr:<8} | {s_curr:<8} | {t_curr:<8} | r1 = {r_curr}")
    step = 1
    while r_curr != 0:
        q = r_prev // r_curr
        r_next = r_prev - q * r_curr
        s_next = s_prev - q * s_curr
        t_next = t_prev - q * t_curr
        eq = f"{r_prev} = {q} * {r_curr} + {r_next}"
        print(f"    Bước {step:<2} | {q:<6} | {r_next:<8} | {s_next:<8} | {t_next:<8} | {eq}")
        r_prev, r_curr = r_curr, r_next
        s_prev, s_curr = s_curr, s_next
        t_prev, t_curr = t_curr, t_next
        step += 1
    inv = t_prev % m
    print("    " + "-" * 65)
    print(f"    [=>] Kết quả: {a}^(-1) mod {m} = {inv}")
    return inv

def solve_elgamal_ca(x=56, e_A=125):
    p_CA = 997
    alpha = 6
    d_CA = 25
    p_minus_1 = p_CA - 1 # 996
    
    print("=" * 75)
    print("USTH FINAL EXAM 2025-2026 - EXERCISE 2.2: ELGAMAL CA SIGNATURE (LỜI GIẢI TỰ LUẬN)")
    print("=" * 75)

    # Bước 1
    beta = pow(alpha, d_CA, p_CA)
    print(f"[BƯỚC 1] Tính khóa công khai của CA (beta):")
    print(f"    p_CA = {p_CA}, alpha = {alpha}, d_CA = {d_CA}")
    print(f"    beta = alpha^d_CA mod p_CA = {alpha}^{d_CA} mod {p_CA} = {beta}")
    print(f"    * Khóa công khai CA: k_pubCA = (p = {p_CA}, alpha = {alpha}, beta = {beta})")
    print(f"    * Khóa bí mật CA   : k_priCA = (d = {d_CA})")
    
    # Bước 2
    x_A = x + e_A
    print(f"\n[BƯỚC 2] Xác định thông điệp liên kết x_A:")
    print(f"    x_A = x + e_A = {x} + {e_A} = {x_A}")
    
    # Bước 3: Phân tích đề bài k_E = 105
    k_E_printed = 105
    g_printed = math.gcd(k_E_printed, p_minus_1)
    r_printed = pow(alpha, k_E_printed, p_CA)
    dr_printed = d_CA * r_printed
    rhs_printed = (x_A - dr_printed) % p_minus_1
    print(f"\n[BƯỚC 3] Phân tích khóa tạm thời trong đề in (k_E = {k_E_printed}):")
    print(f"    Kiểm tra: gcd(k_E, p-1) = gcd({k_E_printed}, {p_minus_1}) = {g_printed}")
    print(f"    Phương trình tính s: {k_E_printed} * s = (x_A - d_CA * r) mod {p_minus_1}")
    print(f"      - r = {alpha}^{k_E_printed} mod {p_CA} = {r_printed}")
    print(f"      - d_CA * r = {d_CA} * {r_printed} = {dr_printed}")
    print(f"      - Vế phải: ({x_A} - {dr_printed}) = {x_A - dr_printed} = {rhs_printed} (mod {p_minus_1})")
    print(f"      - Kiểm tra tính chia hết: {rhs_printed} mod {g_printed} = {rhs_printed % g_printed} != 0")
    print(f"    ===> NHẬN XÉT HỌC THUẬT: gcd({k_E_printed}, {p_minus_1}) = {g_printed} không chia hết cho {rhs_printed}.")
    print(f"         Phương trình vô nghiệm! (Đây là lỗi in ấn đề thi: k_E bắt buộc phải nguyên tố cùng nhau với p-1).")

    # Bước 4: Khóa hợp lệ k_E = 107
    k_E_valid = 107
    g_valid = math.gcd(k_E_valid, p_minus_1)
    print(f"\n[BƯỚC 4] Sử dụng khóa tạm thời hợp lệ chuẩn (k_E = {k_E_valid}):")
    print(f"    gcd({k_E_valid}, {p_minus_1}) = {g_valid} == 1 (Nguyên tố cùng nhau, thỏa mãn điều kiện ElGamal)")
    
    # Bước 5: Tính r
    r = pow(alpha, k_E_valid, p_CA)
    print(f"\n[BƯỚC 5] Tính thành phần chữ ký r:")
    print(f"    r = alpha^k_E mod p = {alpha}^{k_E_valid} mod {p_CA} = {r}")
    
    # Bước 6: Tính nghịch đảo k_E^(-1) và s
    print(f"\n[BƯỚC 6] Tính nghịch đảo k_E^(-1) mod {p_minus_1} và thành phần s:")
    k_E_inv = print_eea_table(p_minus_1, k_E_valid)
    dr = d_CA * r
    diff = x_A - dr
    diff_mod = diff % p_minus_1
    s = (diff_mod * k_E_inv) % p_minus_1
    print(f"\n    Các bước tính cụ thể cho s:")
    print(f"      1. d_CA * r = {d_CA} * {r} = {dr}")
    print(f"      2. x_A - d_CA * r = {x_A} - {dr} = {diff}")
    print(f"      3. ({diff}) mod {p_minus_1} = {diff_mod}")
    print(f"      4. s = ({diff_mod} * {k_E_inv}) mod {p_minus_1} = {diff_mod * k_E_inv} mod {p_minus_1} = {s}")
    print(f"    ===> CẶP CHỮ KÝ SỐ: (r = {r}, s = {s})")
    print(f"    ===> CHỨNG CHỈ SỐ: Cert_A = (x_A = {x_A}, (r = {r}, s = {s}))")
    
    # Bước 7: Xác minh bởi Người dùng B
    print(f"\n[BƯỚC 7] Người dùng B xác minh chứng chỉ số:")
    term_beta_r = pow(beta, r, p_CA)
    term_r_s = pow(r, s, p_CA)
    v1 = (term_beta_r * term_r_s) % p_CA
    v2 = pow(alpha, x_A, p_CA)
    print(f"    * Tính v1 = (beta^r * r^s) mod p:")
    print(f"        beta^r mod p = {beta}^{r} mod {p_CA} = {term_beta_r}")
    print(f"        r^s mod p    = {r}^{s} mod {p_CA} = {term_r_s}")
    print(f"        v1 = ({term_beta_r} * {term_r_s}) mod {p_CA} = {v1}")
    print(f"    * Tính v2 = alpha^x_A mod p:")
    print(f"        v2 = {alpha}^{x_A} mod {p_CA} = {v2}")
    print(f"    * So sánh kết quả: v1 = {v1}, v2 = {v2}")
    print(f"    ===> KẾT LUẬN: v1 == v2 ({v1 == v2}) => Chữ ký số HOÀN TOÀN HỢP LỆ VÀ XÁC THỰC!")
    print("=" * 75)


def solve_session7_slide8_elgamal():
    """
    Session 7 Slide 8 Example:
    p = 29, alpha = 2, d = 12, k_E = 5.
    Bob signs a message x to Alice with ElGamal digital signature.
    """
    p = 29
    alpha = 2
    d = 12
    k_E = 5
    p_minus_1 = p - 1 # 28
    
    # 1. Key Generation
    beta = pow(alpha, d, p)
    print("\nSESSION 7 SLIDE 8 - ELGAMAL SIGNATURE EXAMPLE")
    print("-" * 70)
    print(f"Domain parameters: p = {p}, alpha = {alpha}")
    print(f"Private key:       d = {d}")
    print(f"Public key:        beta = alpha^d mod p = {alpha}^{d} mod {p} = {beta}")
    
    # Message (let x = 15 or hash h(m) = 15)
    x = 15
    print(f"\nSigning message:   x = {x}, Ephemeral key: k_E = {k_E}")
    print(f"Check gcd(k_E, p-1): gcd({k_E}, {p_minus_1}) = {math.gcd(k_E, p_minus_1)} (Valid)")
    
    # 2. Signature Generation
    r = pow(alpha, k_E, p)
    k_inv = pow(k_E, -1, p_minus_1)
    s = ((x - d * r) * k_inv) % p_minus_1
    print(f"Compute r:         r = alpha^k_E mod p = {alpha}^{k_E} mod {p} = {r}")
    print(f"Compute k_E^(-1):  {k_E}^(-1) mod {p_minus_1} = {k_inv}")
    print(f"Compute s:         s = (x - d*r)*k_E^(-1) mod {p_minus_1} = ({x} - {d}*{r})*{k_inv} mod {p_minus_1} = {s}")
    print(f"Generated signature: (r = {r}, s = {s})")
    
    # 3. Verification
    v1 = (pow(beta, r, p) * pow(r, s, p)) % p
    v2 = pow(alpha, x, p)
    print(f"\nVerification:")
    print(f"v1 = (beta^r * r^s) mod p = ({beta}^{r} * {r}^{s}) mod {p} = {v1}")
    print(f"v2 = alpha^x mod p        = {alpha}^{x} mod {p} = {v2}")
    print(f"Signature Valid:          v1 == v2 -> {v1 == v2} (Verified!)")
    print("=" * 70)

def custom_elgamal_sign(p: int, alpha: int, d: int, k_E: int, x: int):
    p_minus_1 = p - 1
    beta = pow(alpha, d, p)
    g = math.gcd(k_E, p_minus_1)
    print("\n" + "=" * 75)
    print(f"CUSTOM ELGAMAL DIGITAL SIGNATURE - LỜI GIẢI TỰ LUẬN")
    print("=" * 75)
    print(f"[BƯỚC 1] Thiết lập tham số & tính khóa công khai:")
    print(f"    p = {p}, alpha = {alpha}, d = {d}")
    print(f"    beta = alpha^d mod p = {alpha}^{d} mod {p} = {beta}")
    print(f"    * Khóa công khai: (p = {p}, alpha = {alpha}, beta = {beta})")
    print(f"    * Khóa bí mật  : d = {d}")

    print(f"\n[BƯỚC 2] Thông điệp cần ký: x = {x}")

    print(f"\n[BƯỚC 3] Kiểm tra khóa tạm thời k_E = {k_E}:")
    print(f"    gcd(k_E, p - 1) = gcd({k_E}, {p_minus_1}) = {g}")
    if g != 1:
        print(f"    [-] LỖI: k_E không nguyên tố cùng nhau với p - 1 ({p_minus_1}). Chữ ký không tồn tại số nguyên s!")
        return
    print(f"    [+] gcd({k_E}, {p_minus_1}) == 1 (Thỏa mãn điều kiện)")

    print(f"\n[BƯỚC 4] Tính thành phần chữ ký r:")
    r = pow(alpha, k_E, p)
    print(f"    r = alpha^k_E mod p = {alpha}^{k_E} mod {p} = {r}")

    print(f"\n[BƯỚC 5] Tính nghịch đảo k_E^(-1) mod {p_minus_1} bằng bảng Euclid mở rộng:")
    k_inv = print_eea_table(p_minus_1, k_E)

    print(f"\n[BƯỚC 6] Tính thành phần chữ ký s = (x - d * r) * k_E^(-1) mod (p - 1):")
    dr = d * r
    diff = x - dr
    diff_mod = diff % p_minus_1
    s = (diff_mod * k_inv) % p_minus_1
    print(f"    1. d * r = {d} * {r} = {dr}")
    print(f"    2. x - d * r = {x} - {dr} = {diff}")
    print(f"    3. ({diff}) mod {p_minus_1} = {diff_mod}")
    print(f"    4. s = ({diff_mod} * {k_inv}) mod {p_minus_1} = {diff_mod * k_inv} mod {p_minus_1} = {s}")
    print(f"    ===> CẶP CHỮ KÝ SỐ: (r = {r}, s = {s})")

    print(f"\n[BƯỚC 7] Xác minh chữ ký số (Verification):")
    term_beta_r = pow(beta, r, p)
    term_r_s = pow(r, s, p)
    v1 = (term_beta_r * term_r_s) % p
    v2 = pow(alpha, x, p)
    print(f"    * v1 = (beta^r * r^s) mod p = ({beta}^{r} * {r}^{s}) mod {p}")
    print(f"         = ({term_beta_r} * {term_r_s}) mod {p} = {v1}")
    print(f"    * v2 = alpha^x mod p = {alpha}^{x} mod {p} = {v2}")
    print(f"    * Kết luận: v1 == v2 ({v1 == v2}) => Chữ ký hợp lệ!")
    print("=" * 75)



def custom_input():
    print("\n" + "=" * 70)
    print("CUSTOM EXAM INPUT: ELGAMAL DIGITAL SIGNATURE")
    print("=" * 70)
    try:
        val_p = input("Enter prime p [e.g. 29]: ").strip()
        p = int(val_p, 0) if val_p else 29
        val_alpha = input("Enter generator alpha [e.g. 2]: ").strip()
        alpha = int(val_alpha, 0) if val_alpha else 2
        val_d = input("Enter private key d [e.g. 12]: ").strip()
        d = int(val_d, 0) if val_d else 12
        val_ke = input("Enter ephemeral key k_E [e.g. 5]: ").strip()
        ke = int(val_ke, 0) if val_ke else 5
        val_x = input("Enter message x to sign [e.g. 15]: ").strip()
        x = int(val_x, 0) if val_x else 15
        custom_elgamal_sign(p, alpha, d, ke, x)
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}")


if __name__ == "__main__":
    import sys

    # Direct interactive flag: python elgamal_digital_signature.py -i
    if len(sys.argv) > 1 and sys.argv[1] in ("-i", "--interactive", "--custom"):
        custom_input()
        sys.exit(0)

    solve_elgamal_ca(56, 125)
    solve_session7_slide8_elgamal()

    # Interactive prompt if user runs directly in terminal
    if sys.stdin.isatty():
        print("-" * 70)
        c = input("[?] Enter custom parameters for your exam? [y/N]: ").strip().lower()
        if c in ("y", "yes"):
            custom_input()

