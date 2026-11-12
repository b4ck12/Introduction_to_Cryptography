import os
# -*- coding: utf-8 -*-
"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Algorithm: Modular Arithmetic Operations & Session 1 Slide Exercises
Reference: Session 1 (Information Security & Modular Arithmetic), Slides 15-25
Student ID: 23BA14056 (x = 56)
=============================================================================
Theory:
  - Modulo operation: a = q * m + r with 0 <= r < m (a = r mod m).
  - Equivalent classes: we can reduce intermediate numbers modulo m.
  - Linear congruence: a * x = b (mod m) has a solution if gcd(a, m) | b.
    When gcd(a, m) = 1, x = a^(-1) * b (mod m).
=============================================================================
"""

import math

def mod_add(a: int, b: int, m: int) -> int:
    return ((a % m) + (b % m)) % m

def mod_sub(a: int, b: int, m: int) -> int:
    return ((a % m) - (b % m) + m) % m

def mod_mul(a: int, b: int, m: int) -> int:
    return ((a % m) * (b % m)) % m

def mod_pow(base: int, exp: int, m: int) -> int:
    return pow(base, exp, m)

def solve_linear_congruence(a: int, b: int, m: int):
    """Solves a * x = b (mod m)."""
    g = math.gcd(a, m)
    if b % g != 0:
        return None
    a_prime = a // g
    b_prime = b // g
    m_prime = m // g
    a_inv = pow(a_prime, -1, m_prime)
    x0 = (b_prime * a_inv) % m_prime
    return [(x0 + i * m_prime) % m for i in range(g)]

def print_cayley_tables(m: int):
    print(f"\n--- Bảng Cộng trong Z_{m} ---")
    header = " + | " + " ".join(f"{i:2d}" for i in range(m))
    print(header)
    print("-" * len(header))
    for i in range(m):
        row = f"{i:2d} | " + " ".join(f"{mod_add(i, j, m):2d}" for j in range(m))
        print(row)

    print(f"\n--- Bảng Nhân trong Z_{m} ---")
    header = " * | " + " ".join(f"{i:2d}" for i in range(m))
    print(header)
    print("-" * len(header))
    for i in range(m):
        row = f"{i:2d} | " + " ".join(f"{mod_mul(i, j, m):2d}" for j in range(m))
        print(row)

def main():
    print("=" * 70)
    print("THUẬT TOÁN SỐ HỌC ĐỒNG DƯ (MODULAR ARITHMETIC) - SESSION 1 EXERCISES")
    print("=" * 70)

    # 1. Session 1 Slide 24: Exercise 1
    print("\n[1] Session 1 Slide 24 - Exercise 1 (Calculate without calculator):")
    m = 13
    p1 = mod_mul(15, 29, m)
    print(f"    (a) 15 * 29 mod 13 = (2 * 3) mod 13 = {p1}")
    p2 = mod_mul(2, 29, m)
    print(f"    (b) 2 * 29 mod 13  = (2 * 3) mod 13 = {p2}")
    p3 = mod_mul(2, 3, m)
    print(f"    (c) 2 * 3 mod 13   = {p3}")
    p4 = mod_mul(-11, 3, m)
    print(f"    (d) -11 * 3 mod 13 = (2 * 3) mod 13 = {p4}")

    # 2. Session 1 Slide 25: Exercise 2
    print("\n[2] Session 1 Slide 25 - Exercise 2 (Compute x as far as possible):")
    # (a) x = 3^2 mod 13
    x_a = mod_pow(3, 2, 13)
    print(f"    (a) x = 3^2 mod 13 = {x_a}")

    # (b) x = 7^2 mod 13
    x_b = mod_pow(7, 2, 13)
    print(f"    (b) x = 7^2 mod 13 = 49 mod 13 = {x_b} (Note: 49 = 3*13 + 10)")

    # (c) x = 3^10 mod 13
    # 3^3 = 27 = 1 mod 13 ==> 3^10 = (3^3)^3 * 3 = 1^3 * 3 = 3 mod 13
    x_c = mod_pow(3, 10, 13)
    print(f"    (c) x = 3^10 mod 13 = (3^3)^3 * 3 = 1^3 * 3 = {x_c}")

    # (d) x = 7^100 mod 13
    # 7^2 = 10 = -3 mod 13 ==> 7^4 = (-3)^2 = 9 = -4 mod 13
    # Fermat's Little Theorem: 7^12 = 1 mod 13 ==> 7^100 = (7^12)^8 * 7^4 = 1 * 9 = 9 mod 13
    x_d = mod_pow(7, 100, 13)
    print(f"    (d) x = 7^100 mod 13 = (7^12)^8 * 7^4 = 1^8 * 9 = {x_d}")

    # (e) 7*x = 11 mod 13
    # gcd(7, 13) = 1 ==> 7^(-1) mod 13 = 2 (since 7*2 = 14 = 1 mod 13)
    # x = 2 * 11 = 22 = 9 mod 13
    sols = solve_linear_congruence(7, 11, 13)
    print(f"    (e) Solve 7*x = 11 (mod 13):")
    print(f"        Inverse 7^(-1) mod 13 = {pow(7, -1, 13)}")
    print(f"        x = 7^(-1) * 11 mod 13 = {sols[0]} (Check: 7*{sols[0]} = {7*sols[0]} = { (7*sols[0])%13 } mod 13)")

    # 3. Student ID Check (x = 56)
    student_id = 56
    print(f"\n[3] Student ID Computation (x = {student_id}):")
    print(f"    56 mod 13 = {student_id % 13}")
    print(f"    56^2 mod 13 = {pow(student_id, 2, 13)}")
    print(f"    56^100 mod 13 = {pow(student_id, 100, 13)}")

    # 4. Cayley Table for Z_5
    print_cayley_tables(5)
    print("=" * 70)

def custom_input():
    import os, sys
    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
        return
    print("\n" + "=" * 70)
    print("CUSTOM EXAM INPUT: MODULAR ARITHMETIC CALCULATOR")
    print("=" * 70)
    print("Choose calculation type:")
    print("  [1] Basic Arithmetic: (a + b, a - b, a * b, a^b mod m)")
    print("  [2] Solve Linear Congruence: a * x = b (mod m)")
    print("  [3] Print Cayley Addition & Multiplication Tables for Z_m")
    try:
        choice = input("Select [1/2/3, default 1]: ").strip()
        if choice == "2":
            val_a = input("Enter a [e.g. 7]: ").strip()
            a = int(val_a, 0) if val_a else 7
            val_b = input("Enter b [e.g. 11]: ").strip()
            b = int(val_b, 0) if val_b else 11
            val_m = input("Enter modulus m [e.g. 13]: ").strip()
            m = int(val_m, 0) if val_m else 13
            sols = solve_linear_congruence(a, b, m)
            print(f"\n[=>] Solving {a} * x = {b} (mod {m}):")
            if sols is None:
                print(f"[-] No solution exists because gcd({a}, {m}) does not divide {b}.")
            else:
                print(f"[+] Solutions x in Z_{m}: {sols}")
                for s in sols:
                    print(f"    Verification: ({a} * {s}) mod {m} = {(a * s) % m}")
        elif choice == "3":
            val_m = input("Enter modulus m [e.g. 5]: ").strip()
            m = int(val_m, 0) if val_m else 5
            print_cayley_tables(m)
        else:
            val_a = input("Enter first integer a [e.g. 15]: ").strip()
            a = int(val_a, 0) if val_a else 15
            val_b = input("Enter second integer b [e.g. 29]: ").strip()
            b = int(val_b, 0) if val_b else 29
            val_m = input("Enter modulus m [e.g. 13]: ").strip()
            m = int(val_m, 0) if val_m else 13
            print(f"\n[=>] Results in Z_{m}:")
            print(f"    ({a} + {b}) mod {m}  = {mod_add(a, b, m)}")
            print(f"    ({a} - {b}) mod {m}  = {mod_sub(a, b, m)}")
            print(f"    ({a} * {b}) mod {m}  = {mod_mul(a, b, m)}")
            print(f"    ({a} ^ {b}) mod {m}  = {mod_pow(a, b, m)}")
            g = math.gcd(a, m)
            if g == 1:
                print(f"    ({a}^(-1)) mod {m}   = {pow(a, -1, m)}")
            else:
                print(f"    Modular inverse {a}^(-1) mod {m} does not exist (gcd={g} != 1)")
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}. Using default.")
        try:
            run_demo()
        except Exception:
            pass


def run_demo():
    main()


def solve_modular_arithmetic_detailed(a: int, b: int, m: int):
    add_val = mod_add(a, b, m)
    sub_val = mod_sub(a, b, m)
    mul_val = mod_mul(a, b, m)
    pow_val = mod_pow(a, b, m)
    g = math.gcd(a, m)
    inv_str = str(pow(a, -1, m)) if g == 1 else f"Không tồn tại (gcd={g} != 1)"

    print("=" * 75)
    print(f"CÁC PHÉP TOÁN SỐ HỌC TRÊN VÀNH MODULO Z_{m}")
    print("=" * 75)
    print(f"[BƯỚC 1] Thiết lập vành Z_{m} & Tham số đầu vào:")
    print(f"    Công thức: a ⊕ b = (a + b) mod m, a ⊗ b = (a · b) mod m, a^b mod m")
    print(f"    Tham số: Toán hạng a = {a}, Toán hạng b = {b}, Modulus m = {m}\n")

    print(f"[BƯỚC 2] Bảng vết tính toán chi tiết từng phép toán (Arithmetic Trace Table):")
    print(f"    {'Phép toán':<18} | {'Biểu thức tính toán':<32} | {'Kết quả trong Z_' + str(m)}")
    print("    " + "-" * 70)
    print(f"    {'Cộng (Add)':<18} | ({a} + {b}) mod {m} = {a+b} mod {m:<15} | {add_val}")
    print(f"    {'Trừ (Subtract)':<18} | ({a} - {b}) mod {m} = {a-b} mod {m:<15} | {sub_val}")
    print(f"    {'Nhân (Multiply)':<18} | ({a} * {b}) mod {m} = {a*b} mod {m:<15} | {mul_val}")
    print(f"    {'Lũy thừa (Power)':<18} | {a}^{b} mod {m:<28} | {pow_val}")
    print(f"    {'Nghịch đảo a^-1':<18} | {a}^(-1) mod {m:<26} | {inv_str}")
    print("    " + "-" * 70)

    print(f"\n[BƯỚC 3] Kết luận các giá trị đại số trong Z_{m}:")
    print(f"    Kiểm tra nguyên tố cùng nhau: gcd({a}, {m}) = {g} (Khả nghịch: {g == 1})")
    print(f"    ===> KẾT QUẢ SỐ HỌC MODULO: a+b={add_val}, a*b={mul_val}, a^b={pow_val}")
    print("=" * 75)


if __name__ == "__main__":
    import sys

    # Run demo test suite only if explicitly requested or in non-interactive test pipe with <= 1 arg
    if "--demo" in sys.argv or (not sys.stdin.isatty() and len(sys.argv) <= 1):
        main()
        sys.exit(0)

    # Support CLI arguments from GUI or terminal: python modular_arithmetic.py 56 139 26
    cli_args = [x for x in sys.argv[1:] if x.strip() and not x.startswith("-")]
    if len(cli_args) >= 3:
        try:
            a = int(cli_args[0], 0)
            b = int(cli_args[1], 0)
            m = int(cli_args[2], 0)
            solve_modular_arithmetic_detailed(a, b, m)
            sys.exit(0)
        except Exception:
            pass

    # Default: Open directly into Custom Exam Input prompt
    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
    else:
        try:
            custom_input()
        except (EOFError, KeyboardInterrupt):
            run_demo()
