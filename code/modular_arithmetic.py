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

if __name__ == "__main__":
    main()
