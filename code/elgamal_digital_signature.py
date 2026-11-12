# -*- coding: utf-8 -*-
"""
Script: elgamal_digital_signature.py
Description: Solves Exercise 2.2 (Certification Authority ElGamal Signature) for Exam 2025-2026.
Parameters: p_CA = 997, alpha = 6, d_CA = 25.
Input message: x_A = x + e_A (where x = student_ID % 64 = 56, e_A = 125 -> x_A = 181).
Supports ephemeral keys:
  - k_E = 185 (Official Exam 2025-2026 value: gcd(185, 996) = 1 -> Valid signature)
  - k_E = 105 (Exam handwritten misreading analysis: gcd(105, 996) = 3 -> Unsolvable equation)
  - k_E = 107 (Alternative nearest coprime key: gcd(107, 996) = 1 -> Valid signature)
"""
import math
import sys

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
    print(f"    [=>] Kết quả nghịch đảo: {a}^(-1) mod {m} = {inv}")
    print(f"    [=>] Kiểm tra: ({a} * {inv}) mod {m} = {(a * inv) % m}")
    return inv

def custom_elgamal_sign(p: int, alpha: int, d: int, k_E: int, x: int):
    """
    Computes ElGamal Digital Signature with full pedagogical step-by-step essay format.
    Handles both valid coprime k_E and invalid non-coprime k_E with mathematical proofs.
    """
    p_minus_1 = p - 1
    beta = pow(alpha, d, p)
    g = math.gcd(k_E, p_minus_1)

    print("\n" + "=" * 75)
    print("CUSTOM ELGAMAL DIGITAL SIGNATURE - LỜI GIẢI TỰ LUẬN TỪNG BƯỚC")
    print("=" * 75)
    print(f"[BƯỚC 1] Thiết lập tham số hệ thống & tính khóa công khai:")
    print(f"    - Số nguyên tố p          : p = {p}")
    print(f"    - Phần tử sinh alpha       : alpha = {alpha}")
    print(f"    - Khóa bí mật của người ký : d = {d}")
    print(f"    - Tính khóa công khai beta : beta = alpha^d mod p = {alpha}^{d} mod {p} = {beta}")
    print(f"    * Khóa công khai (Public Key) : k_pub = (p = {p}, alpha = {alpha}, beta = {beta})")
    print(f"    * Khóa bí mật (Private Key)   : k_pri = d = {d}")

    print(f"\n[BƯỚC 2] Xác định thông điệp cần ký (Message to Sign):")
    print(f"    - Thông điệp x = {x}")
    if p == 997 and x == 181:
        print(f"      (Trong Đề thi 2025-2026 Bài 2.2: x_A = x + e_A = 56 + 125 = 181)")
    elif p == 997 and x == 56:
        print(f"      (Lưu ý Đề thi 2025-2026 Bài 2.2 yêu cầu ký thông điệp liên kết x_A = x + e_A = 56 + 125 = 181)")

    print(f"\n[BƯỚC 3] Kiểm tra điều kiện khóa tạm thời (Ephemeral key k_E = {k_E}):")
    print(f"    Điều kiện tiên quyết của chuẩn ElGamal: gcd(k_E, p - 1) = 1")
    print(f"    Tính: gcd({k_E}, {p - 1}) = {g}")

    if g != 1:
        # Trường hợp không nguyên tố cùng nhau (như k_E = 105)
        r = pow(alpha, k_E, p)
        dr = d * r
        diff = (x - dr) % p_minus_1
        print(f"    [-] LỖI TOÁN HỌC: gcd({k_E}, {p - 1}) = {g} != 1.")
        print(f"        Do đó k_E = {k_E} KHÔNG tồn tại nghịch đảo modulo {p - 1}!")
        print(f"\n    [!] Phân tích phương trình đồng dư tính s:")
        print(f"        k_E * s = (x - d * r) mod (p - 1)")
        print(f"        {k_E} * s = ({x} - {d} * {r}) = {x - dr} = {diff} (mod {p - 1})")
        if diff % g != 0:
            print(f"        Vì gcd({k_E}, {p - 1}) = {g} KHÔNG CHIA HẾT cho vế phải {diff} ({diff} mod {g} = {diff % g} != 0),")
            print(f"        ===> PHƯƠNG TRÌNH VÔ NGHIỆM! Không tồn tại số nguyên s để tạo chữ ký!")
        else:
            print(f"        Phương trình có {g} nghiệm nhưng chữ ký bị suy giảm tính duy nhất và suy yếu bảo mật.")

        if p == 997 and k_E == 105:
            print("\n    " + "#" * 71)
            print("    [!] GIẢI THÍCH ĐẶC BIỆT CHO ĐỀ THI 2025-2026 (USTH CRYPTOGRAPHY):")
            print("        Trong đề thi photo/viết tay, số 185 thường bị nhìn nhầm thành 105")
            print("        do nét cong số 8 mờ trông giống số 0.")
            print("        - Nếu đọc là k_E = 105: Thí sinh cần giải thích rõ phương trình vô nghiệm")
            print("          như trên để đạt điểm tối đa lý thuyết (3/3 điểm).")
            print("        - Đề bài chuẩn chính xác là k_E = 185 (gcd(185, 996) = 1) hoặc k_E = 107.")
            print("    " + "#" * 71)
        return

    print(f"    [+] gcd({k_E}, {p - 1}) == 1 (Thỏa mãn tuyệt đối điều kiện sinh chữ ký ElGamal)")

    # Bước 4: Tính r
    print(f"\n[BƯỚC 4] Tính thành phần chữ ký r:")
    r = pow(alpha, k_E, p)
    print(f"    r = alpha^k_E mod p = {alpha}^{k_E} mod {p} = {r}")

    # Bước 5: Bảng Euclid mở rộng tính k_E^(-1)
    print(f"\n[BƯỚC 5] Tìm nghịch đảo k_E^(-1) mod (p - 1) = {k_E}^(-1) mod {p_minus_1}:")
    k_inv = print_eea_table(p_minus_1, k_E)

    # Bước 6: Tính s
    print(f"\n[BƯỚC 6] Tính thành phần chữ ký s:")
    print(f"    Công thức: s = (x - d * r) * k_E^(-1) mod (p - 1)")
    dr = d * r
    diff = x - dr
    diff_mod = diff % p_minus_1
    s = (diff_mod * k_inv) % p_minus_1
    print(f"    Chi tiết các phép tính trung gian:")
    print(f"      1. d * r = {d} * {r} = {dr}")
    print(f"      2. x - d * r = {x} - {dr} = {diff}")
    print(f"      3. ({diff}) mod {p_minus_1} = {diff_mod}")
    print(f"      4. s = ({diff_mod} * {k_inv}) mod {p_minus_1} = {diff_mod * k_inv} mod {p_minus_1} = {s}")
    print(f"\n    ===> CẶP CHỮ KÝ SỐ: (r = {r}, s = {s})")
    print(f"    ===> CHỨNG CHỈ SỐ: Cert_A = (x = {x}, (r = {r}, s = {s}))")

    # Bước 7: Xác minh bởi Người nhận B
    print(f"\n[BƯỚC 7] Người nhận B xác minh tính hợp lệ của chữ ký (Verification):")
    print(f"    Điều kiện xác minh: v1 == v2 (mod p)")
    term_beta_r = pow(beta, r, p)
    term_r_s = pow(r, s, p)
    v1 = (term_beta_r * term_r_s) % p
    v2 = pow(alpha, x, p)
    print(f"    * Tính v1 = (beta^r * r^s) mod p:")
    print(f"        beta^r mod p = {beta}^{r} mod {p} = {term_beta_r}")
    print(f"        r^s mod p    = {r}^{s} mod {p} = {term_r_s}")
    print(f"        v1 = ({term_beta_r} * {term_r_s}) mod {p} = {v1}")
    print(f"    * Tính v2 = alpha^x mod p:")
    print(f"        v2 = {alpha}^{x} mod {p} = {v2}")
    print(f"    * So sánh kết quả:")
    print(f"        v1 = {v1}, v2 = {v2}")
    if v1 == v2:
        print(f"    ===> KẾT LUẬN: v1 == v2 ({v1} == {v2}) => CHỮ KÝ SỐ HOÀN TOÀN HỢP LỆ VÀ XÁC THỰC!")
    else:
        print(f"    ===> KẾT LUẬN: v1 != v2 ({v1} != {v2}) => CHỮ KÝ KHÔNG HỢP LỆ!")
    print("=" * 75)


def solve_elgamal_ca(x=56, e_A=125, k_E=185):
    """
    Solves Exam 2025-2026 Exercise 2.2 with k_E = 185 (Official) and explains k_E = 105 pitfall.
    """
    x_A = x + e_A
    print("=" * 75)
    print("USTH FINAL EXAM 2025-2026 - EXERCISE 2.2: ELGAMAL CA CERTIFICATE")
    print(f"Tham số CA: p = 997, alpha = 6, d = 25 | Thông điệp x_A = {x} + {e_A} = {x_A}")
    print("=" * 75)

    # 1. Official Solution with k_E = 185
    print("\n[PHẦN 1] LỜI GIẢI CHUẨN XÁC VỚI KHÓA TẠM THỜI k_E = 185:")
    custom_elgamal_sign(p=997, alpha=6, d=25, k_E=k_E, x=x_A)

    # 2. Pitfall Analysis with k_E = 105
    print("\n[PHẦN 2] PHÂN TÍCH HỌC THUẬT TRƯỜNG HỢP NHÌN NHẦM ĐỀ k_E = 105:")
    custom_elgamal_sign(p=997, alpha=6, d=25, k_E=105, x=x_A)


def solve_session7_slide8_elgamal():
    """
    Session 7 Slide 8 Example:
    p = 29, alpha = 2, d = 12, k_E = 5, x = 15.
    """
    custom_elgamal_sign(p=29, alpha=2, d=12, k_E=5, x=15)


def custom_input():
    print("\n" + "=" * 70)
    print("CUSTOM EXAM INPUT: ELGAMAL DIGITAL SIGNATURE")
    print("=" * 70)
    try:
        val_p = input("Enter prime p [default 997]: ").strip()
        p = int(val_p, 0) if val_p else 997
        val_alpha = input("Enter generator alpha [default 6]: ").strip()
        alpha = int(val_alpha, 0) if val_alpha else 6
        val_d = input("Enter private key d [default 25]: ").strip()
        d = int(val_d, 0) if val_d else 25
        val_ke = input("Enter ephemeral key k_E [default 185]: ").strip()
        ke = int(val_ke, 0) if val_ke else 185
        val_x = input("Enter message x to sign [default 181]: ").strip()
        x = int(val_x, 0) if val_x else 181
        custom_elgamal_sign(p, alpha, d, ke, x)
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}")


def run_demo():
    solve_elgamal_ca(56, 125, 185)
    solve_session7_slide8_elgamal()


if __name__ == "__main__":
    if "--demo" in sys.argv:
        run_demo()
        sys.exit(0)

    # Extract non-flag arguments
    cli_args = [a for a in sys.argv[1:] if not a.startswith("-")]

    # If running in non-TTY mode (Tauri GUI subprocess, pipe, automated tests)
    # NEVER call input() to prevent EOFError!
    if not sys.stdin.isatty():
        try:
            p_arg = int(cli_args[0], 0) if len(cli_args) > 0 and cli_args[0].strip() else 997
            alpha_arg = int(cli_args[1], 0) if len(cli_args) > 1 and cli_args[1].strip() else 6
            d_arg = int(cli_args[2], 0) if len(cli_args) > 2 and cli_args[2].strip() else 25
            ke_arg = int(cli_args[3], 0) if len(cli_args) > 3 and cli_args[3].strip() else 185
            x_arg = int(cli_args[4], 0) if len(cli_args) > 4 and cli_args[4].strip() else 181
            custom_elgamal_sign(p_arg, alpha_arg, d_arg, ke_arg, x_arg)
        except Exception as e:
            print(f"[-] Input parsing error: {e}")
            run_demo()
        sys.exit(0)

    # If running interactively in CLI and arguments were passed
    if len(cli_args) >= 5:
        try:
            p_arg = int(cli_args[0], 0)
            alpha_arg = int(cli_args[1], 0)
            d_arg = int(cli_args[2], 0)
            ke_arg = int(cli_args[3], 0)
            x_arg = int(cli_args[4], 0)
            custom_elgamal_sign(p_arg, alpha_arg, d_arg, ke_arg, x_arg)
            sys.exit(0)
        except Exception:
            pass

    custom_input()
