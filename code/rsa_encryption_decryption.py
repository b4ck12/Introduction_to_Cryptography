# -*- coding: utf-8 -*-
"""
Script: solve_rsa_encrypt_2025.py
Description: Solves Exercise 2.3 (RSA Encryption & Decryption) for Exam 2025-2026.
Evaluates both M = 56 (Student ID 23BA14056) and M = 20260 (Printed on exam paper).
Keypair from 2.1: N = 31553, e = 125, d = 30689.
"""

def solve_rsa_encryption(custom_m=None):
    import sys
    if custom_m is None and len(sys.argv) > 1:
        try:
            custom_m = int(sys.argv[1])
        except ValueError:
            pass
    M_val = custom_m if custom_m is not None else 56
    N = 31553
    e = 125
    d = 30689
    
    print("=" * 65)
    print("USTH FINAL EXAM 2025-2026 - EXERCISE 2.3: RSA ENCRYPT & DECRYPT")
    print("=" * 65)
    print(f"System Parameters: Modulus N = {N}, Public e = {e}, Private d = {d}\n")
    
    # Case 1: Student ID (Default M = 56)
    M1 = M_val
    C1 = pow(M1, e, N)
    M1_dec = pow(C1, d, N)
    print("--- Case 1: Personalized Student ID (M = 56) ---")
    print(f"Plaintext message M:          {M1}")
    print(f"Encryption C = M^e mod N:     {M1}^{e} mod {N} = {C1}")
    print(f"Decryption M = C^d mod N:     {C1}^{d} mod {N} = {M1_dec}")
    print(f"Recovery Verified:            {M1 == M1_dec} (Correct!)\n")
    
    # Case 2: Printed on exam sheet (M = 20260)
    M2 = 20260
    C2 = pow(M2, e, N)
    M2_dec = pow(C2, d, N)
    print("--- Case 2: Printed Exam Sheet Message (M = 20260) ---")
    print(f"Plaintext message M:          {M2}")
    print(f"Encryption C = M^e mod N:     {M2}^{e} mod {N} = {C2}")
    print(f"Decryption M = C^d mod N:     {C2}^{d} mod {N} = {M2_dec}")
    print(f"Recovery Verified:            {M2 == M2_dec} (Correct!)")
    print("=" * 65)
    return {
        "case_student": {"M": M1, "C": C1, "dec": M1_dec},
        "case_printed": {"M": M2, "C": C2, "dec": M2_dec}
    }

if __name__ == "__main__":
    solve_rsa_encryption()
