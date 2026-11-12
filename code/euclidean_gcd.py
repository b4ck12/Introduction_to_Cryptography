import os
"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Algorithm: Euclidean Algorithm for Greatest Common Divisor (GCD)
Reference: Session 6 (Public Key), Lab 2 Exercise 1
Student ID: 23BA14056 (x = 56)
=============================================================================
Theory:
  Given two integers a and b (with a >= b > 0):
  r_0 = a, r_1 = b
  r_{i-1} = q_i * r_i + r_{i+1},  where 0 <= r_{i+1} < r_i
  The process terminates when r_{n+1} = 0, and gcd(a, b) = r_n.
=============================================================================
"""

def euclidean_gcd(a: int, b: int, verbose: bool = True) -> int:
    """
    Computes gcd(a, b) using Euclidean algorithm and prints the division steps.
    """
    if verbose:
        print("=" * 75)
        print("THUẬT TOÁN EUCLID TÌM ƯỚC SỐ CHUNG LỚN NHẤT (GCD)")
        print("=" * 75)
        print(f"[BƯỚC 1] Thiết lập bài toán & Định lý chia Euclid:")
        print(f"    Công thức: r_{{i-1}} = q_i * r_i + r_{{i+1}} (0 <= r_{{i+1}} < r_i)")
        print(f"    Tham số: a = {a}, b = {b}\n")
        print(f"[BƯỚC 2] Bảng vết các bước chia có dư (Division Steps Trace):")
        print(f"    {'Step':<6} | {'Phép chia có dư (Division Equation)':<38} | {'Số dư'}")
        print("    " + "-" * 60)

    r_prev, r_curr = abs(a), abs(b)
    if r_prev < r_curr:
        r_prev, r_curr = r_curr, r_prev

    step = 1
    while r_curr != 0:
        q = r_prev // r_curr
        r_next = r_prev % r_curr
        if verbose:
            eq = f"{r_prev} = {q} * {r_curr} + {r_next}"
            print(f"    Step {step:<2} | {eq:<38} | r_{step} = {r_next}")
        r_prev, r_curr = r_curr, r_next
        step += 1

    if verbose:
        print("    " + "-" * 60)
        print(f"\n[BƯỚC 3] Kết luận ước số chung lớn nhất:")
        print(f"    Ước số chung lớn nhất: gcd({a}, {b}) = {r_prev}")
        print(f"    Kiểm tra nguyên tố cùng nhau (Coprime): {r_prev == 1} (gcd == 1)")
        print(f"    ===> ƯỚC SỐ CHUNG LỚN NHẤT: gcd({a}, {b}) = {r_prev}")
        print("=" * 75)

    return r_prev


def custom_input():
    import os, sys
    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
        return
    print("\n" + "=" * 60)
    print("CUSTOM EXAM INPUT: EUCLIDEAN GCD")
    print("=" * 60)
    try:
        val_a = input("Enter first integer a [e.g. 61430]: ").strip()
        a = int(val_a, 0) if val_a else 61430
        val_b = input("Enter second integer b [e.g. 52698]: ").strip()
        b = int(val_b, 0) if val_b else 52698
        euclidean_gcd(a, b, verbose=True)
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}. Using default.")
        try:
            run_demo()
        except Exception:
            pass


def run_demo():
    print("=" * 60)
    print("DEMO: EUCLIDEAN ALGORITHM FOR GCD")
    print("=" * 60)

    # 1. Lab 2 Exercise 1: gcd(52698, 61430)
    print("1. Lab 2 Exercise 1:")
    g1 = euclidean_gcd(61430, 52698)

    # 2. RSA Coprimality check from Exam 2025-2026: gcd(e, phi(n)) = gcd(125, 31188)
    print("2. Exam 2025-2026: gcd(e, phi(n)) with e=125, phi(n)=31188:")
    g2 = euclidean_gcd(31188, 125)

    # 3. Student ID Check: gcd(56, 31188)
    print("3. Student ID check (x=56): gcd(31188, 56):")
    g3 = euclidean_gcd(31188, 56)


if __name__ == "__main__":
    import sys

    # Run demo test suite only if explicitly requested or in non-interactive test pipe
    if "--demo" in sys.argv or (not sys.stdin.isatty() and len(sys.argv) <= 1):
        run_demo()
        sys.exit(0)

    # Support CLI arguments: python euclidean_gcd.py 61430 52698
    if len(sys.argv) > 1 and not sys.argv[1].startswith("-"):
        try:
            a = int(sys.argv[1], 0)
            b = int(sys.argv[2], 0) if len(sys.argv) > 2 else 0
            euclidean_gcd(a, b, verbose=True)
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