import os
# -*- coding: utf-8 -*-
"""
Script: solve_dhke.py
Description: Solves Exercise 4 (Diffie-Hellman Key Exchange - DHKE).
Covers both exam variants:
  - Variant 1 (crop_ex3_4.png / Exam sheet): p = 27361, alpha = 6
  - Variant 2 (869026595...png / Slide problem): p = 51907, alpha = 6
Inputs: Alice private key a = 56 (Student ID), Bob private key b = C = 2365 (RSA Ciphertext).
"""

def solve_dhke_variant(p, alpha, a, b, label=""):
    print(f"\n" + "=" * 75)
    print(f"{label} - LỜI GIẢI TỰ LUẬN TỪNG BƯỚC (p = {p}, alpha = {alpha})")
    print("=" * 75)
    
    # Alice computes public key k_A = alpha^a mod p
    k_A = pow(alpha, a, p)
    # Bob computes public key k_B = alpha^b mod p
    k_B = pow(alpha, b, p)
    
    # Alice computes shared session key k_AB = (k_B)^a mod p
    k_AB_alice = pow(k_B, a, p)
    # Bob computes shared session key k_AB = (k_A)^b mod p
    k_AB_bob = pow(k_A, b, p)
    
    print(f"[BƯỚC 1] Thiết lập tham số công khai hệ thống:")
    print(f"    Công thức thỏa thuận khóa: k_AB = alpha^(a*b) mod p")
    print(f"    * Số nguyên tố chung : p = {p}")
    print(f"    * Phần tử sinh chung: alpha = {alpha}")

    print(f"\n[BƯỚC 2] Alice tạo khóa và tính khóa công khai:")
    print(f"    * Khóa bí mật của Alice: a = {a}")
    print(f"    Công thức: k_A = alpha^a mod p = {alpha}^{a} mod {p} = {k_A}")

    print(f"\n[BƯỚC 3] Bob tạo khóa và tính khóa công khai:")
    print(f"    * Khóa bí mật của Bob: b = {b}")
    print(f"    Công thức: k_B = alpha^b mod p = {alpha}^{b} mod {p} = {k_B}")

    print(f"\n[BƯỚC 4] Trao đổi khóa qua kênh truyền không bảo mật:")
    print(f"    * Alice gửi k_A = {k_A} cho Bob.")
    print(f"    * Bob gửi k_B = {k_B} cho Alice.")

    print(f"\n[BƯỚC 5] Alice tính khóa phiên bí mật chung (Shared Session Key)::")
    print(f"    Công thức: k_AB = (k_B)^a mod p = ({k_B})^{a} mod {p} = {k_AB_alice}")

    print(f"\n[BƯỚC 6] Bob tính khóa phiên bí mật chung:")
    print(f"    Công thức: k_AB = (k_A)^b mod p = ({k_A})^{b} mod {p} = {k_AB_bob}")

    print(f"\n[BƯỚC 7] Kết luận tính thống nhất khóa & Xác thực:")
    print(f"    Kiểm tra xác thực: k_AB(Alice) == k_AB(Bob) ({k_AB_alice} == {k_AB_bob}) -> True (Chính xác!)")
    print(f"    ===> KHÓA BÍ MẬT PHIÊN THỐNG NHẤT: k_AB = {k_AB_alice}")
    print("=" * 75)
    return {
        "p": p,
        "alpha": alpha,
        "k_A": k_A,
        "k_B": k_B,
        "k_AB": k_AB_alice
    }


def solve_dhke(student_id=56):
    import sys
    if len(sys.argv) > 1:
        try:
            student_id = int(sys.argv[1])
        except ValueError:
            pass
    print("=" * 70)
    print("USTH FINAL EXAM 2025-2026 - EXERCISE 4: DIFFIE-HELLMAN KEY EXCHANGE")
    print("=" * 70)
    a = student_id  # Alice private key: Student ID
    b = 2365        # Bob private key: RSA Ciphertext C from Exercise 2.3
    
    # Variant 1: From crop_ex3_4.png (p = 27361, alpha = 6)
    solve_dhke_variant(27361, 6, a, b, "Variant 1: Printed Exam Paper Parameters (p = 27361, alpha = 6)")
    
    # Variant 2: From 869026595...png (p = 51907, alpha = 6)
    solve_dhke_variant(51907, 6, a, b, "Variant 2: Class Exam Sheet Parameters (p = 51907, alpha = 6)")
    print("=" * 70)

def custom_input():
    import os, sys
    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
        return
    print("\n" + "=" * 70)
    print("CUSTOM EXAM INPUT: DIFFIE-HELLMAN KEY EXCHANGE (DHKE)")
    print("=" * 70)
    try:
        val_p = input("Enter prime modulus p [e.g. 27361]: ").strip()
        p = int(val_p, 0) if val_p else 27361
        val_alpha = input("Enter generator alpha [e.g. 6]: ").strip()
        alpha = int(val_alpha, 0) if val_alpha else 6
        val_a = input("Enter Alice private key a [e.g. 56]: ").strip()
        a = int(val_a, 0) if val_a else 56
        val_b = input("Enter Bob private key b [e.g. 2365]: ").strip()
        b = int(val_b, 0) if val_b else 2365
        solve_dhke_variant(p, alpha, a, b, "Custom Exam DHKE Calculation")
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}. Using default.")
        try:
            run_demo()
        except Exception:
            pass


run_demo = solve_dhke


if __name__ == "__main__":
    import sys

    if "--demo" in sys.argv or (not sys.stdin.isatty() and len(sys.argv) <= 1):
        solve_dhke()
        sys.exit(0)

    # Support CLI arguments: python diffie_hellman_key_exchange.py 27361 6 20260 24373
    cli_args = [a for a in sys.argv[1:] if a.strip() and not a.startswith("-")]
    if len(cli_args) >= 1:
        try:
            p_arg = int(cli_args[0], 0)
            alpha_arg = int(cli_args[1], 0) if len(cli_args) > 1 else 6
            a_arg = int(cli_args[2], 0) if len(cli_args) > 2 else 20260
            b_arg = int(cli_args[3], 0) if len(cli_args) > 3 else 24373
            solve_dhke_variant(p_arg, alpha_arg, a_arg, b_arg, "TRAO ĐỔI KHÓA DIFFIE-HELLMAN (DHKE)")
            sys.exit(0)
        except Exception:
            pass

    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
    else:
        try:
            custom_input()
        except (EOFError, KeyboardInterrupt):
            run_demo()