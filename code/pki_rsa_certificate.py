# -*- coding: utf-8 -*-
"""
Script: solve_exam_2024.py
Description: Solves all calculation problems for USTH Final Exam 2024-2025 (Code 01).
  - Exercise 1.1: RSA Key Generation (p = 223, q = 193, candidates: {3525, 5525, 6525}).
  - Exercise 1.2: CA Digital Certificate with RSA (p_CA = 227, q_CA = 149, e_CA = 25537, M = 56).
"""
import math

def factorize(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def solve_exam_2024(student_id=56):
    import sys
    if len(sys.argv) > 1:
        try:
            student_id = int(sys.argv[1])
        except ValueError:
            pass
    print("=" * 70)
    print("USTH FINAL EXAM 2024-2025 - EXERCISE 1.1: RSA KEY GENERATION")
    print("=" * 70)
    p = 223
    q = 193
    N = p * q
    phi = (p - 1) * (q - 1)
    candidates = [3525, 5525, 6525]
    
    print(f"Given primes:                 p = {p}, q = {q}")
    print(f"Modulus N = p * q:            {p} * {q} = {N}")
    print(f"Totient phi(N) = (p-1)*(q-1): {p-1} * {q-1} = {phi}")
    print(f"Prime factorization of phi:   {phi} = {' * '.join(map(str, factorize(phi)))}")
    
    selected_e = None
    for e in candidates:
        g = math.gcd(e, phi)
        status = "ACCEPTED (Valid Public Exponent)" if g == 1 else f"REJECTED (gcd = {g} != 1)"
        print(f"  e = {e}: gcd({e}, {phi}) = {g} -> {status}")
        if g == 1 and selected_e is None:
            selected_e = e
            
    # Private key d
    d = pow(selected_e, -1, phi)
    print(f"\nSelected Public Exponent:     e = {selected_e}")
    print(f"Private Key d = e^-1 mod phi: {selected_e}^-1 mod {phi} = {d}")
    print(f"Verification: (e * d) mod phi: ({selected_e} * {d}) mod {phi} = {(selected_e * d) % phi} (Valid!)")
    
    print("\n" + "=" * 70)
    print("USTH FINAL EXAM 2024-2025 - EXERCISE 1.2: CA RSA DIGITAL CERTIFICATE")
    print("=" * 70)
    p_CA = 227
    q_CA = 149
    e_CA = 25537
    M = student_id # Student ID (Default 56)
    
    N_CA = p_CA * q_CA
    phi_CA = (p_CA - 1) * (q_CA - 1)
    d_CA = pow(e_CA, -1, phi_CA)
    
    print(f"CA Setup Parameters:          p_CA = {p_CA}, q_CA = {q_CA}, e_CA = {e_CA}")
    print(f"CA Modulus N_CA:              {p_CA} * {q_CA} = {N_CA}")
    print(f"CA Totient phi(N_CA):         {p_CA - 1} * {q_CA - 1} = {phi_CA}")
    print(f"CA Private Key d_CA:          {e_CA}^-1 mod {phi_CA} = {d_CA}")
    print(f"Verification (e_CA * d_CA):   ({e_CA} * {d_CA}) mod {phi_CA} = {(e_CA * d_CA) % phi_CA} (Valid!)")
    
    # Sign student ID
    S_CA = pow(M, d_CA, N_CA)
    print(f"\nUser A ID Message to Sign:   M = {M}")
    print(f"CA Digital Signature S_CA:    S_CA = M^d_CA mod N_CA = {M}^{d_CA} mod {N_CA} = {S_CA}")
    
    # Verification by User B
    V = pow(S_CA, e_CA, N_CA)
    print(f"User B Verifies:              V = S_CA^e_CA mod N_CA = {S_CA}^{e_CA} mod {N_CA} = {V}")
    print(f"Signature Validity:           V == M -> {V == M} (Certificate Valid & Authentic!)")
    print("=" * 70)

if __name__ == "__main__":
    solve_exam_2024()
