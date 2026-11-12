"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Algorithm: Square-and-Multiply (Fast Modular Exponentiation)
Reference: Session 6 (Public Key), Lab 2 Exercise 3
Student ID: 23BA14056 (x = 56)
=============================================================================
Theory:
  To compute y = x^e mod n efficiently in O(log e) multiplications:
  1. Express exponent e in binary: e = (b_k, b_{k-1}, ..., b_1, b_0)_2
  2. Left-to-Right Algorithm:
     - Set y = 1
     - For each bit b from MSB (leftmost) to LSB (rightmost):
         y = (y^2) mod n               (Square)
         if b == 1:
             y = (y * x) mod n         (Multiply)
=============================================================================
"""

from typing import List, Dict, Any

def square_and_multiply(base: int, exponent: int, modulus: int, verbose: bool = True) -> int:
    """
    Computes (base^exponent) % modulus using the Left-to-Right Square-and-Multiply algorithm.
    Prints an execution trace table when verbose=True.
    """
    if modulus <= 0:
        raise ValueError("Modulus must be positive.")
    if exponent == 0:
        return 1 % modulus

    # Reduce base mod n first
    x = base % modulus
    bin_exp = bin(exponent)[2:]  # Binary representation string

    if verbose:
        print(f"\n[+] Computing {base}^{exponent} mod {modulus} using Square-and-Multiply:")
        print(f"    Base x (reduced) = {x}")
        print(f"    Exponent e       = {exponent} (Binary: {bin_exp}, length: {len(bin_exp)} bits)")
        print(f"    Modulus n        = {modulus}")
        print("-" * 65)
        print(f"{'Step':<5} | {'Bit':<4} | {'Operation':<12} | {'Calculation':<22} | {'Current Value y':<15}")
        print("-" * 65)

    y = 1
    step = 0
    for i, bit in enumerate(bin_exp):
        step += 1
        # Square
        sq_val = (y * y) % modulus
        if verbose:
            calc_sq = f"{y}^2 mod {modulus}"
            print(f"{step:<5} | {bit:<4} | {'Square':<12} | {calc_sq:<22} | {sq_val:<15}")
        y = sq_val

        # Multiply if bit == 1
        if bit == '1':
            step += 1
            mul_val = (y * x) % modulus
            if verbose:
                calc_mul = f"{y} * {x} mod {modulus}"
                print(f"{step:<5} | {bit:<4} | {'Multiply':<12} | {calc_mul:<22} | {mul_val:<15}")
            y = mul_val

    if verbose:
        print("-" * 65)
        print(f"[=>] Result: {base}^{exponent} mod {modulus} = {y}")
        # Sanity check with Python built-in pow()
        check = pow(base, exponent, modulus)
        print(f"[=>] Verification with built-in pow(): {check} (Match: {check == y})\n")

    return y


def custom_input():
    print("\n" + "=" * 65)
    print("CUSTOM EXAM INPUT: SQUARE-AND-MULTIPLY EXPONENTIATION")
    print("=" * 65)
    try:
        val_base = input("Enter base x [e.g. 56]: ").strip()
        base = int(val_base, 0) if val_base else 56
        val_exp = input("Enter exponent e / H [e.g. 125]: ").strip()
        exp = int(val_exp, 0) if val_exp else 125
        val_mod = input("Enter modulus n / m [e.g. 31553]: ").strip()
        mod = int(val_mod, 0) if val_mod else 31553
        square_and_multiply(base, exp, mod, verbose=True)
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}")


def run_demo():
    print("=" * 65)
    print("DEMO: SQUARE-AND-MULTIPLY FAST EXPONENTIATION")
    print("=" * 65)

    # 1. Lab 2 Exercise 3: Compute 8^5625 mod 7
    print("1. Lab 2 Exercise 3: Compute 8^5625 mod 7:")
    print("   Note: Mathematically, 8 = 1 (mod 7).")
    print("   Therefore, 8^5625 = 1^5625 = 1 (mod 7).")
    print("   Let's verify with the algorithm:")
    res1 = square_and_multiply(8, 5625, 7, verbose=True)

    # 2. RSA Encryption from Exam 2025-2026 for Student ID (M = 56):
    # C = 56^125 mod 31553
    print("\n2. RSA Encryption: C = M^e mod n with M = 56, e = 125, n = 31553:")
    c2 = square_and_multiply(56, 125, 31553, verbose=True)
    print(f"Ciphertext C = {c2}")

    # 3. RSA Decryption from Exam 2025-2026:
    # M = C^d mod n with C = 2365, d = 30689, n = 31553
    print("\n3. RSA Decryption: M = C^d mod n with C = 2365, d = 30689, n = 31553:")
    m3 = square_and_multiply(2365, 30689, 31553, verbose=False)
    print(f"Decrypted Message M = {m3} (Expected: 56, Match: {m3 == 56})")

    # 4. Session 6 Slide 11: Repeated Squaring Example
    # (N, e) = (33, 23), M = 5. Calculate C = 5^23 mod 33
    print("\n4. Session 6 Slide 11: Compute C = 5^23 mod 33:")
    c4 = square_and_multiply(5, 23, 33, verbose=True)
    print(f"Slide 11 Ciphertext C = {c4} (Expected: 26, Match: {c4 == 26})")


if __name__ == "__main__":
    import sys

    # Run demo test suite only if explicitly requested or in non-interactive test pipe
    if "--demo" in sys.argv or (not sys.stdin.isatty() and len(sys.argv) <= 1):
        run_demo()
        sys.exit(0)

    # Support CLI arguments: python square_and_multiply.py 5 23 33
    if len(sys.argv) > 1 and not sys.argv[1].startswith("-"):
        try:
            b = int(sys.argv[1], 0)
            e = int(sys.argv[2], 0) if len(sys.argv) > 2 else 1
            m = int(sys.argv[3], 0) if len(sys.argv) > 3 else 1000000007
            square_and_multiply(b, e, m, verbose=True)
            sys.exit(0)
        except Exception:
            pass

    # Default: Open directly into Custom Exam Input prompt
    if sys.stdin.isatty():
        custom_input()
    else:
        run_demo()