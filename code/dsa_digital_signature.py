"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Algorithm: Digital Signature Algorithm (DSA)
Reference: Session 7 (Hash Functions & Digital Signatures, Slides 12-14)
Student ID: 23BA14056 (x = 56)
=============================================================================
Theory:
  DSA Parameters:
  - Prime p and prime divisor q such that q | (p - 1).
  - Generator alpha in Z_p* with order q.
  - Private key: d in {1, ..., q-1}.
  - Public key:  beta = alpha^d mod p.

  Signing (Message hash h = H(M)):
  - Choose random ephemeral key k_E in {1, ..., q-1} coprime to q.
  - r = (alpha^(k_E) mod p) mod q.
  - s = k_E^(-1) * (h + d * r) mod q.
  - Signature is pair (r, s).

  Verification:
  - w   = s^(-1) mod q
  - u_1 = (h * w) mod q
  - u_2 = (r * w) mod q
  - v   = (alpha^(u_1) * beta^(u_2) mod p) mod q
  - Signature is VALID iff v == r.
=============================================================================
"""

import math
from typing import Tuple

def dsa_sign(p: int, q: int, alpha: int, d: int, k_E: int, h_m: int, verbose: bool = True) -> Tuple[int, int]:
    """Computes DSA signature (r, s)."""
    if verbose:
        print(f"\n[+] DSA Signing Process:")
        print(f"    Domain: p = {p}, q = {q}, alpha = {alpha}")
        print(f"    Private key d = {d}, Ephemeral k_E = {k_E}, Hash h(M) = {h_m}")

    # Compute r
    r = pow(alpha, k_E, p) % q
    if r == 0:
        raise ValueError("r = 0, choose a different k_E!")

    # Invert k_E mod q
    k_inv = pow(k_E, -1, q)

    # Compute s
    s = (k_inv * (h_m + d * r)) % q
    if s == 0:
        raise ValueError("s = 0, choose a different k_E!")

    if verbose:
        print(f"    1. Compute r = (alpha^k_E mod p) mod q = ({alpha}^{k_E} mod {p}) mod {q} = {pow(alpha, k_E, p)} mod {q} = {r}")
        print(f"    2. Compute k_E^(-1) mod q = {k_E}^(-1) mod {q} = {k_inv}")
        print(f"    3. Compute s = k_E^(-1) * (h(M) + d*r) mod q = {k_inv} * ({h_m} + {d}*{r}) mod {q} = {s}")
        print(f"[=>] Generated Signature: (r = {r}, s = {s})\n")

    return r, s


def dsa_verify(p: int, q: int, alpha: int, beta: int, h_m: int, r: int, s: int, verbose: bool = True) -> bool:
    """Verifies DSA signature (r, s)."""
    if verbose:
        print(f"[+] DSA Verification Process:")
        print(f"    Public key beta = {beta}, Hash h(M) = {h_m}, Signature (r = {r}, s = {s})")

    if not (0 < r < q and 0 < s < q):
        if verbose:
            print("[!] Verification Failed: r or s out of bounds [1, q-1]")
        return False

    w = pow(s, -1, q)
    u1 = (h_m * w) % q
    u2 = (r * w) % q
    v = ((pow(alpha, u1, p) * pow(beta, u2, p)) % p) % q

    if verbose:
        print(f"    1. Compute w = s^(-1) mod q = {s}^(-1) mod {q} = {w}")
        print(f"    2. Compute u1 = (h(M) * w) mod q = ({h_m} * {w}) mod {q} = {u1}")
        print(f"    3. Compute u2 = (r * w) mod q = ({r} * {w}) mod {q} = {u2}")
        print(f"    4. Compute v = (alpha^u1 * beta^u2 mod p) mod q")
        term1 = pow(alpha, u1, p)
        term2 = pow(beta, u2, p)
        print(f"       = ({alpha}^{u1} * {beta}^{u2} mod {p}) mod {q} = ({term1} * {term2} mod {p}) mod {q} = {v}")
        print(f"[=>] Check v == r: {v} == {r} -> {v == r}\n")

    return v == r


if __name__ == "__main__":
    print("=" * 65)
    print("DEMO: DSA DIGITAL SIGNATURE (SLIDE 12 TEST VECTOR & STUDENT ID)")
    print("=" * 65)

    # 1. Slide 12 Textbook Example:
    # p = 59, q = 29, alpha = 3, d = 7, k_E = 10, h(m) = 26
    p1 = 59
    q1 = 29
    alpha1 = 3
    d1 = 7
    k_E1 = 10
    h1 = 26
    beta1 = pow(alpha1, d1, p1)  # 3^7 mod 59 = 4

    print("1. Slide 12 Textbook Verification:")
    r1, s1 = dsa_sign(p1, q1, alpha1, d1, k_E1, h1, verbose=True)
    is_valid1 = dsa_verify(p1, q1, alpha1, beta1, h1, r1, s1, verbose=True)
    print(f"Slide 12 Verification Valid: {is_valid1} (r = {r1}, s = {s1})")

    # 2. Student ID Variant:
    # Use h(M) = 56 (Student ID 056)
    print("\n2. Student ID Evaluation (h(M) = 56):")
    h_student = 56
    r2, s2 = dsa_sign(p1, q1, alpha1, d1, k_E1, h_student, verbose=True)
    is_valid2 = dsa_verify(p1, q1, alpha1, beta1, h_student, r2, s2, verbose=True)
    print(f"Student ID Signature Verification Result: {is_valid2}")
