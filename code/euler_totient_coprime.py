"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Algorithm: Euler's Totient Function Phi(m) & Pairwise Coprime Analysis
Reference: Session 6 (Public Key), Lab 2 Exercise 2
Student ID: 23BA14056 (x = 56)
=============================================================================
Theory:
  1. Euler's Totient Function Phi(m):
     The number of positive integers <= m that are coprime to m (gcd(k, m) == 1).
     Formula:
         Phi(m) = m * PROD_{p | m} (1 - 1/p)
     If m = p * q (product of distinct primes, e.g. RSA):
         Phi(m) = (p - 1) * (q - 1)

  2. Coprimality:
     Integers a and b are coprime if and only if gcd(a, b) = 1.
=============================================================================
"""

import math
from typing import List, Tuple, Dict

def prime_factors(n: int) -> List[int]:
    """Returns a sorted list of unique prime factors of n."""
    factors = []
    d = 2
    temp = abs(n)
    while d * d <= temp:
        if temp % d == 0:
            factors.append(d)
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:
        factors.append(temp)
    return factors


def euler_totient(m: int, verbose: bool = False) -> int:
    """
    Computes Euler's Totient Phi(m) using prime factorization:
        Phi(m) = m * PROD_{p | m} (1 - 1/p)
    """
    if m <= 0:
        raise ValueError("m must be a positive integer.")
    if m == 1:
        return 1

    factors = prime_factors(m)
    result = m
    steps = []
    for p in factors:
        result = (result * (p - 1)) // p
        steps.append(f"(1 - 1/{p})")

    if verbose:
        formula_str = f"{m} * " + " * ".join(steps)
        factors_str = " * ".join(str(p) for p in factors)
        print(f"Phi({m:<3}): Prime factors = {factors} ==> Phi({m}) = {formula_str} = {result}")

    return result


def find_coprime_pairs(numbers: List[int]) -> List[Tuple[int, int]]:
    """
    Given a list of numbers, finds all unique pairs (a, b) with a < b such that gcd(a, b) == 1.
    """
    coprimes = []
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            a, b = numbers[i], numbers[j]
            if math.gcd(a, b) == 1:
                coprimes.append((a, b))
    return coprimes


def custom_input():
    print("\n" + "=" * 65)
    print("CUSTOM EXAM INPUT: EULER'S TOTIENT & COPRIME PAIRS")
    print("=" * 65)
    print("Choose calculation type:")
    print("  [1] Compute Phi(m), Prime Factors & Coprime Set Z_m*")
    print("  [2] Find All Pairwise Coprime Pairs from a List of Numbers")
    try:
        choice = input("Select [1/2, default 1]: ").strip()
        if choice == "2":
            val_list = input("Enter comma-separated integers [e.g. 10, 15, 21, 28, 33]: ").strip()
            if val_list:
                nums = [int(x.strip(), 0) for x in val_list.split(",") if x.strip()]
            else:
                nums = [10, 15, 21, 28, 33]
            pairs = find_coprime_pairs(nums)
            print(f"\n[+] Input list ({len(nums)} elements): {nums}")
            print(f"[+] Total possible pairs: C({len(nums)}, 2) = {len(nums)*(len(nums)-1)//2}")
            print(f"[+] Total coprime pairs found: {len(pairs)}")
            for idx, (a, b) in enumerate(pairs, 1):
                print(f"    {idx:>2}. gcd({a}, {b}) = 1")
        else:
            val_m = input("Enter integer m [e.g. 26]: ").strip()
            m = int(val_m, 0) if val_m else 26
            phi = euler_totient(m, verbose=True)
            coprimes = [k for k in range(1, m + 1) if math.gcd(k, m) == 1]
            print(f"[=>] Elements coprime to {m} (Z_{m}*): {coprimes}")
            print(f"[=>] Count |Z_{m}*| = {len(coprimes)} == Phi({m}) = {phi}")
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}")


def run_demo():
    print("=" * 65)
    print("DEMO: EULER'S TOTIENT FUNCTION & COPRIME PAIRS")
    print("=" * 65)

    # 1. Lab 2 Exercise 2:
    # Set A = {10, 15, 21, 28, 33, 35, 42, 55, 77, 91, 143, 165}
    A = [10, 15, 21, 28, 33, 35, 42, 55, 77, 91, 143, 165]
    print(f"\n[+] Set A ({len(A)} elements): {A}\n")

    print("[Part 1] Computing Euler's Totient Phi(m) for all m in Set A:")
    print("-" * 65)
    phi_results = {}
    for m in A:
        phi_results[m] = euler_totient(m, verbose=True)

    print("\n[Part 2] Finding all pairwise coprime pairs (gcd(a, b) = 1) in Set A:")
    print("-" * 65)
    coprime_pairs = find_coprime_pairs(A)
    total_pairs = len(A) * (len(A) - 1) // 2
    print(f"Total possible pairs: C({len(A)}, 2) = {total_pairs}")
    print(f"Total coprime pairs found: {len(coprime_pairs)}\n")

    # Display pairs in a clean formatted grid
    for idx, (a, b) in enumerate(coprime_pairs, 1):
        print(f"{idx:>2}. gcd({a:>3}, {b:>3}) = 1", end="   " if idx % 3 != 0 else "\n")
    if len(coprime_pairs) % 3 != 0:
        print()

    # 2. Session 1 Slide 26 Example:
    # What is Phi(m) for m = 3, 4, 5, 9, 26?
    print("\n" + "-" * 65)
    print("[Part 3] Session 1 Slide 26 Example: Phi(m) for m in {3, 4, 5, 9, 26}:")
    slide_m_list = [3, 4, 5, 9, 26]
    for m in slide_m_list:
        val = euler_totient(m, verbose=True)

    # 3. RSA Modulus Totient check
    print("\n" + "-" * 65)
    print("[Part 4] RSA Modulus Totient Calculation:")
    p, q = 139, 227
    n = p * q
    phi_n = euler_totient(n)
    print(f"RSA primes: p = {p}, q = {q}")
    print(f"Modulus n = p * q = {n}")
    print(f"Phi(n) = (p - 1) * (q - 1) = {p - 1} * {q - 1} = {phi_n}")

    # 4. Student ID Check
    student_id = 56
    print(f"\nStudent ID x = {student_id}:")
    phi_id = euler_totient(student_id, verbose=True)
    print(f"Phi({student_id}) = {phi_id}")


if __name__ == "__main__":
    import sys

    # Run demo test suite only if explicitly requested or in non-interactive test pipe
    if "--demo" in sys.argv or (not sys.stdin.isatty() and len(sys.argv) <= 1):
        run_demo()
        sys.exit(0)

    # Support CLI arguments: python euler_totient_coprime.py 26
    if len(sys.argv) > 1 and not sys.argv[1].startswith("-"):
        try:
            m = int(sys.argv[1], 0)
            euler_totient(m, verbose=True)
            sys.exit(0)
        except Exception:
            pass

    # Default: Open directly into Custom Exam Input prompt
    if sys.stdin.isatty():
        custom_input()
    else:
        run_demo()