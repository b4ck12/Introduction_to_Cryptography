# -*- coding: utf-8 -*-
"""
Script: solve_elgamal_ca_signature.py
Description: Solves Exercise 2.2 (Certification Authority ElGamal Signature) for Exam 2025-2026.
Parameters: p_CA = 997, alpha = 6, d_CA = 25.
Input message: x_A = x + e_A (where x = student_ID % 64 = 56, e_A = 125 -> x_A = 181).
Analyzes both exam sheet ephemeral key (k_E = 105) and standard coprime key (k_E = 107).
"""
import math

def solve_elgamal_ca(x=56, e_A=125):
    p_CA = 997
    alpha = 6
    d_CA = 25
    p_minus_1 = p_CA - 1 # 996
    
    # 1. Compute Public Key of CA: beta = alpha^d_CA mod p_CA
    beta = pow(alpha, d_CA, p_CA)
    
    # 2. Bound ID and public key
    x_A = x + e_A
    
    print("=" * 70)
    print("USTH FINAL EXAM 2025-2026 - EXERCISE 2.2: ELGAMAL CA SIGNATURE")
    print("=" * 70)
    print(f"CA Setup Parameters:          p_CA = {p_CA}, alpha = {alpha}, d_CA = {d_CA}")
    print(f"Totient of prime modulus:     p_CA - 1 = {p_minus_1}")
    print(f"CA Public Key beta:           6^{d_CA} mod {p_CA} = {beta}")
    print(f"  -> Public Key:  k_pubCA = (p_CA = {p_CA}, alpha = {alpha}, beta = {beta})")
    print(f"  -> Private Key: k_priCA = (d_CA = {d_CA})")
    print(f"\nMessage to Sign (User A):     x_A = x + e_A = {x} + {e_A} = {x_A}")
    
    # 3. Analyze k_E = 105 from the printed exam paper
    k_E_printed = 105
    g_printed = math.gcd(k_E_printed, p_minus_1)
    rhs_printed = (x_A - d_CA * pow(alpha, k_E_printed, p_CA)) % p_minus_1
    print("\n--- Case A: Analysis of Printed Ephemeral Key (k_E = 105) ---")
    print(f"gcd(k_E, p_CA - 1) = gcd(105, 996) = {g_printed}")
    print(f"Linear congruence for s: 105 * s = (x_A - d_CA * r) mod 996")
    r_printed = pow(alpha, k_E_printed, p_CA)
    rhs_val = (x_A - d_CA * r_printed) % p_minus_1
    print(f"  r = 6^105 mod 997 = {r_printed}")
    print(f"  RHS = ({x_A} - 25 * {r_printed}) mod 996 = {rhs_val}")
    print(f"  Divisibility test: {rhs_val} % {g_printed} = {rhs_val % g_printed}")
    if rhs_val % g_printed != 0:
        print("  -> RESULT: No integer solution for s! (Identified exam typo: k_E must be coprime to p-1).")
    
    # 4. Standard Coprime Ephemeral Key (k_E = 107)
    k_E_valid = 107
    print(f"\n--- Case B: Standard Ephemeral Key Coprime to 996 (k_E = {k_E_valid}) ---")
    g_valid = math.gcd(k_E_valid, p_minus_1)
    print(f"gcd({k_E_valid}, 996) = {g_valid} (Coprime!)")
    
    # Signature component r
    r = pow(alpha, k_E_valid, p_CA)
    
    # Signature component s: s = (x_A - d_CA * r) * k_E^-1 mod (p_CA - 1)
    k_E_inv = pow(k_E_valid, -1, p_minus_1)
    s = ((x_A - d_CA * r) * k_E_inv) % p_minus_1
    
    print(f"Signature component r:        r = {alpha}^{k_E_valid} mod {p_CA} = {r}")
    print(f"k_E inverse mod 996:          {k_E_valid}^-1 mod {p_minus_1} = {k_E_inv}")
    print(f"Signature component s:        s = ({x_A} - {d_CA} * {r}) * {k_E_inv} mod {p_minus_1} = {s}")
    print(f"Certificate of User A:        Cert_A = (x_A = {x_A}, (r = {r}, s = {s}))")
    
    # 5. Verification by User B
    v1 = (pow(beta, r, p_CA) * pow(r, s, p_CA)) % p_CA
    v2 = pow(alpha, x_A, p_CA)
    print("\n--- Verification of Certificate by User B ---")
    print(f"v1 = (beta^r * r^s) mod p:    ({beta}^{r} * {r}^{s}) mod {p_CA} = {v1}")
    print(f"v2 = alpha^x_A mod p:         {alpha}^{x_A} mod {p_CA} = {v2}")
    print(f"Signature Valid:              v1 == v2 -> {v1 == v2} (Verified!)")
    print("=" * 70)

def solve_session7_slide8_elgamal():
    """
    Session 7 Slide 8 Example:
    p = 29, alpha = 2, d = 12, k_E = 5.
    Bob signs a message x to Alice with ElGamal digital signature.
    """
    p = 29
    alpha = 2
    d = 12
    k_E = 5
    p_minus_1 = p - 1 # 28
    
    # 1. Key Generation
    beta = pow(alpha, d, p)
    print("\nSESSION 7 SLIDE 8 - ELGAMAL SIGNATURE EXAMPLE")
    print("-" * 70)
    print(f"Domain parameters: p = {p}, alpha = {alpha}")
    print(f"Private key:       d = {d}")
    print(f"Public key:        beta = alpha^d mod p = {alpha}^{d} mod {p} = {beta}")
    
    # Message (let x = 15 or hash h(m) = 15)
    x = 15
    print(f"\nSigning message:   x = {x}, Ephemeral key: k_E = {k_E}")
    print(f"Check gcd(k_E, p-1): gcd({k_E}, {p_minus_1}) = {math.gcd(k_E, p_minus_1)} (Valid)")
    
    # 2. Signature Generation
    r = pow(alpha, k_E, p)
    k_inv = pow(k_E, -1, p_minus_1)
    s = ((x - d * r) * k_inv) % p_minus_1
    print(f"Compute r:         r = alpha^k_E mod p = {alpha}^{k_E} mod {p} = {r}")
    print(f"Compute k_E^(-1):  {k_E}^(-1) mod {p_minus_1} = {k_inv}")
    print(f"Compute s:         s = (x - d*r)*k_E^(-1) mod {p_minus_1} = ({x} - {d}*{r})*{k_inv} mod {p_minus_1} = {s}")
    print(f"Generated signature: (r = {r}, s = {s})")
    
    # 3. Verification
    v1 = (pow(beta, r, p) * pow(r, s, p)) % p
    v2 = pow(alpha, x, p)
    print(f"\nVerification:")
    print(f"v1 = (beta^r * r^s) mod p = ({beta}^{r} * {r}^{s}) mod {p} = {v1}")
    print(f"v2 = alpha^x mod p        = {alpha}^{x} mod {p} = {v2}")
    print(f"Signature Valid:          v1 == v2 -> {v1 == v2} (Verified!)")
    print("=" * 70)

if __name__ == "__main__":
    solve_elgamal_ca(56, 125)
    solve_session7_slide8_elgamal()
