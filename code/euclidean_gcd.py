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
        print(f"\n[+] Computing GCD({a}, {b}) using Euclidean Algorithm:")
        print(f"{'Step':<6} | {'Division Equation':<35} | {'Remainder':<10}")
        print("-" * 55)

    r_prev, r_curr = abs(a), abs(b)
    if r_prev < r_curr:
        r_prev, r_curr = r_curr, r_prev

    step = 1
    while r_curr != 0:
        q = r_prev // r_curr
        r_next = r_prev % r_curr
        if verbose:
            eq = f"{r_prev} = {q} * {r_curr} + {r_next}"
            print(f"Step {step:<2} | {eq:<35} | r_{step} = {r_next}")
        r_prev, r_curr = r_curr, r_next
        step += 1

    if verbose:
        print("-" * 55)
        print(f"[=>] Result: gcd({a}, {b}) = {r_prev}\n")

    return r_prev


if __name__ == "__main__":
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
