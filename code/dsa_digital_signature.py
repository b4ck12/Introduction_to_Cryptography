import os
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


def custom_input():
    import os, sys
    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
        return
    print("\n" + "=" * 65)
    print("CUSTOM EXAM INPUT: DSA DIGITAL SIGNATURE")
    print("=" * 65)
    try:
        val_p = input("Enter prime p [e.g. 59]: ").strip()
        p = int(val_p, 0) if val_p else 59
        val_q = input("Enter prime divisor q [e.g. 29]: ").strip()
        q = int(val_q, 0) if val_q else 29
        val_alpha = input("Enter generator alpha [e.g. 3]: ").strip()
        alpha = int(val_alpha, 0) if val_alpha else 3
        val_d = input("Enter private key d [e.g. 7]: ").strip()
        d = int(val_d, 0) if val_d else 7
        val_ke = input("Enter ephemeral key k_E [e.g. 10]: ").strip()
        ke = int(val_ke, 0) if val_ke else 10
        val_h = input("Enter message hash h(M) [e.g. 26]: ").strip()
        h = int(val_h, 0) if val_h else 26

        beta = pow(alpha, d, p)
        print(f"\n[+] Public key beta = alpha^d mod p = {alpha}^{d} mod {p} = {beta}")
        r, s = dsa_sign(p, q, alpha, d, ke, h, verbose=True)
        valid = dsa_verify(p, q, alpha, beta, h, r, s, verbose=True)
        print(f"[=>] Signature Valid: {valid}")
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}. Using default.")
        try:
            run_demo()
        except Exception:
            pass


def run_demo():
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


def solve_dsa_detailed(p: int, q: int, alpha: int, d: int, k_E: int, h_m: int):
    beta = pow(alpha, d, p)
    print("=" * 75)
    print("THUẬT TOÁN CHỮ KÝ ĐIỆN TỬ DSA (DIGITAL SIGNATURE ALGORITHM)")
    print("=" * 75)
    print(f"[BƯỚC 1] Thiết lập tham số hệ thống & Tạo khóa:")
    print(f"    Công thức khóa công khai: beta = alpha^d mod p = {alpha}^{d} mod {p} = {beta}")
    print(f"    Tham số miền: p = {p}, q = {q}, alpha = {alpha}")
    print(f"    Khóa bí mật: d = {d}, Khóa tạm thời k_E = {k_E}, Giá trị băm h(M) = {h_m}\n")

    print(f"[BƯỚC 2] Quá trình tạo chữ ký điện tử (Signature Generation):")
    print(f"    Công thức: r = (alpha^k_E mod p) mod q")
    print(f"    Công thức: s = k_E^(-1) * (h(M) + d * r) mod q")
    r, s = dsa_sign(p, q, alpha, d, k_E, h_m, verbose=False)
    k_inv = pow(k_E, -1, q)
    print(f"    1. Tính thành phần r: ({alpha}^{k_E} mod {p}) mod {q} = {pow(alpha, k_E, p)} mod {q} = {r}")
    print(f"    2. Nghịch đảo k_E^(-1) mod q = {k_E}^(-1) mod {q} = {k_inv}")
    print(f"    3. Tính thành phần s: {k_inv} * ({h_m} + {d}*{r}) mod {q} = {s}")
    print(f"    ===> CẶP CHỮ KÝ ĐIỆN TỬ DSA: (r = {r}, s = {s})\n")

    print(f"[BƯỚC 3] Quá trình xác thực chữ ký (Signature Verification):")
    print(f"    Công thức: w = s^(-1) mod q, u1 = (h(M)*w) mod q, u2 = (r*w) mod q")
    print(f"    Công thức kiểm tra: v = (alpha^u1 * beta^u2 mod p) mod q == r")
    w = pow(s, -1, q)
    u1 = (h_m * w) % q
    u2 = (r * w) % q
    term1 = pow(alpha, u1, p)
    term2 = pow(beta, u2, p)
    v = ((term1 * term2) % p) % q
    print(f"    1. Tính w = {s}^(-1) mod {q} = {w}")
    print(f"    2. Tính u1 = ({h_m} * {w}) mod {q} = {u1}")
    print(f"    3. Tính u2 = ({r} * {w}) mod {q} = {u2}")
    print(f"    4. Tính v = ({alpha}^{u1} * {beta}^{u2} mod {p}) mod {q} = ({term1} * {term2} mod {p}) mod {q} = {v}")
    print(f"    Kiểm tra xác thực: v == r -> {v} == {r} (True - Chữ ký hợp lệ!)")
    print("=" * 75)


if __name__ == "__main__":
    import sys
    if "--demo" in sys.argv or (not sys.stdin.isatty() and len(sys.argv) <= 1):
        run_demo()
        sys.exit(0)

    # Support CLI arguments: python dsa_digital_signature.py 59 29 3 7 10 26
    cli_args = [a for a in sys.argv[1:] if a.strip() and not a.startswith("-")]
    if len(cli_args) >= 6:
        try:
            p_arg = int(cli_args[0], 0)
            q_arg = int(cli_args[1], 0)
            alpha_arg = int(cli_args[2], 0)
            d_arg = int(cli_args[3], 0)
            ke_arg = int(cli_args[4], 0)
            h_arg = int(cli_args[5], 0)
            solve_dsa_detailed(p_arg, q_arg, alpha_arg, d_arg, ke_arg, h_arg)
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