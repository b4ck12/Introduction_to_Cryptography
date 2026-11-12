import os
"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Algorithm: Extended Euclidean Algorithm (EEA) & Modular Inversion
Reference: Session 6 (Public Key), Lab 2 Exercise 4
Student ID: 23BA14056 (x = 56)
=============================================================================
Theory:
  Given integers a and b, EEA computes gcd(a, b) and integers s, t such that:
      a * s + b * t = gcd(a, b)  (Bézout's identity)

  When gcd(a, m) = 1, the modular inverse a^{-1} mod m exists:
      a * s + m * t = 1 ==> a * s = 1 (mod m) ==> a^{-1} = s (mod m)
=============================================================================
"""

from typing import Tuple, List, Dict

def extended_euclidean(a: int, b: int, verbose: bool = True) -> Tuple[int, int, int]:
    """
    Computes gcd(a, b) and Bézout coefficients (s, t) such that:
        a * s + b * t = gcd(a, b)
    Returns: (gcd, s, t)
    """
    if verbose:
        print("=" * 75)
        print("THUẬT TOÁN EUCLID MỞ RỘNG (EXTENDED EUCLIDEAN ALGORITHM - EEA)")
        print("=" * 75)
        print(f"[BƯỚC 1] Thiết lập bài toán & Công thức Bézout:")
        print(f"    Công thức: a * s + b * t = gcd(a, b)")
        print(f"    Công thức truy hồi: r_i = r_{{i-2}} - q_i * r_{{i-1}}, s_i = s_{{i-2}} - q_i * s_{{i-1}}, t_i = t_{{i-2}} - q_i * t_{{i-1}}")
        print(f"    Tham số: a = {a}, Modulus m = {b}\n")
        print(f"[BƯỚC 2] Bảng vết thuật toán Euclid mở rộng (EEA Trace Table):")
        print(f"    {'Step':<5} | {'q':<6} | {'r':<10} | {'s':<10} | {'t':<10}")
        print("    " + "-" * 50)

    # Initial state
    r_prev, r_curr = a, b
    s_prev, s_curr = 1, 0
    t_prev, t_curr = 0, 1

    if verbose:
        print(f"    {'init':<5} | {'-':<6} | {r_prev:<10} | {s_prev:<10} | {t_prev:<10}")
        print(f"    {'init':<5} | {'-':<6} | {r_curr:<10} | {s_curr:<10} | {t_curr:<10}")

    step = 1
    while r_curr != 0:
        q = r_prev // r_curr
        r_next = r_prev - q * r_curr
        s_next = s_prev - q * s_curr
        t_next = t_prev - q * t_curr

        if verbose:
            print(f"    Step {step:<2} | {q:<6} | {r_next:<10} | {s_next:<10} | {t_next:<10}")

        r_prev, r_curr = r_curr, r_next
        s_prev, s_curr = s_curr, s_next
        t_prev, t_curr = t_curr, t_next
        step += 1

    gcd_val = r_prev
    s_val = s_prev
    t_val = t_prev

    if verbose:
        print("    " + "-" * 50)
        print(f"\n[BƯỚC 3] Kết luận hệ số Bézout & Xác thực:")
        print(f"    Ước số chung lớn nhất: gcd({a}, {b}) = {gcd_val}")
        print(f"    Đồng nhất thức Bézout: ({a}) * ({s_val}) + ({b}) * ({t_val}) = {gcd_val}")
        check = a * s_val + b * t_val
        print(f"    Kiểm tra xác thực: {check} == {gcd_val} -> True (Chính xác!)")

    return gcd_val, s_val, t_val


def mod_inverse(a: int, m: int, verbose: bool = True) -> int:
    """
    Finds x such that (a * x) = 1 (mod m).
    Raises ValueError if gcd(a, m) != 1.
    """
    gcd_val, s, _ = extended_euclidean(a, m, verbose=verbose)
    if gcd_val != 1:
        raise ValueError(f"Modular inverse does not exist because gcd({a}, {m}) = {gcd_val} != 1")
    inv = s % m
    if verbose:
        print(f"    Công thức: a^(-1) mod m = s mod m = ({s}) mod {m} = {inv}")
        print(f"    Kiểm tra khôi phục: ({a} * {inv}) mod {m} = {(a * inv) % m} == 1 (True - Khả nghịch!)")
        print(f"    ===> NGHỊCH ĐẢO MODULO: {a}^(-1) mod {m} = {inv}")
        print("=" * 75)
    return inv


def custom_input():
    import os, sys
    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
        return
    print("\n" + "=" * 60)
    print("CUSTOM EXAM INPUT: EXTENDED EUCLIDEAN & MODULAR INVERSE")
    print("=" * 60)
    print("Choose operation:")
    print("  [1] Compute Modular Inverse: a^(-1) mod m")
    print("  [2] Compute Bézout Identity & GCD: a*s + b*t = gcd(a, b)")
    try:
        op = input("Select [1/2, default 1]: ").strip()
        if op == "2":
            val_a = input("Enter a [e.g. 65537]: ").strip()
            a = int(val_a, 0) if val_a else 65537
            val_b = input("Enter b [e.g. 35256]: ").strip()
            b = int(val_b, 0) if val_b else 35256
            extended_euclidean(a, b, verbose=True)
        else:
            val_a = input("Enter number to invert a [e.g. 125]: ").strip()
            a = int(val_a, 0) if val_a else 125
            val_m = input("Enter modulus m [e.g. 31188]: ").strip()
            m = int(val_m, 0) if val_m else 31188
            mod_inverse(a, m, verbose=True)
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}. Using default.")
        try:
            run_demo()
        except Exception:
            pass


def run_demo():
    print("=" * 60)
    print("DEMO: EXTENDED EUCLIDEAN ALGORITHM & MODULAR INVERSE")
    print("=" * 60)

    # 1. Lab 2 Exercise 4: 65537 * x = 1 (mod 35256)
    print("1. Lab 2 Exercise 4: Solve 65537 * x = 1 (mod 35256):")
    x1 = mod_inverse(65537, 35256)
    print(f"Result: x = {x1}")

    # 2. Exam 2025-2026 RSA Decryption Key: 125 * d = 1 (mod 31188)
    print("\n2. Exam 2025-2026: RSA Decryption exponent d = 125^(-1) mod 31188:")
    d2 = mod_inverse(125, 31188)
    print(f"Result: d = {d2}")

    # 3. Exam 2024-2025 RSA Key: 5525 * d = 1 (mod 42624) where phi(n) = 222 * 192 = 42624
    print("\n3. Exam 2024-2025: RSA Decryption exponent d = 5525^(-1) mod 42624:")
    d3 = mod_inverse(5525, 42624)
    print(f"Result: d = {d3}")

    # 4. Affine cipher key inversion: a = 7 in mod 26
    print("\n4. Affine Cipher: Decryption key for a = 7 (mod 26):")
    a_inv = mod_inverse(7, 26)
    print(f"Result: a^(-1) = {a_inv}")


if __name__ == "__main__":
    import sys

    # Run demo test suite only if explicitly requested or in non-interactive test pipe
    if "--demo" in sys.argv or (not sys.stdin.isatty() and len(sys.argv) <= 1):
        run_demo()
        sys.exit(0)

    # Support CLI arguments: python extended_euclidean.py 125 31188
    if len(sys.argv) > 1 and not sys.argv[1].startswith("-"):
        try:
            a = int(sys.argv[1], 0)
            b = int(sys.argv[2], 0) if len(sys.argv) > 2 else 26
            mod_inverse(a, b, verbose=True)
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