# -*- coding: utf-8 -*-
"""
Script: solve_rsa_keygen_2025.py
Description: Solves Exercise 2.1 (RSA Key Generation) for Exam 2025-2026.
Parameters: p = 139, q = 227, Candidate exponents = {122, 123, 124, 125}.
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

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inv(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"No modular inverse for {a} mod {m}")
    return (x % m + m) % m

def solve_rsa_keygen():
    p = 139
    q = 227
    candidates = [122, 123, 124, 125]
    
    N = p * q
    phi = (p - 1) * (q - 1)
    phi_factors = factorize(phi)
    
    print("=" * 65)
    print("USTH FINAL EXAM 2025-2026 - EXERCISE 2.1: RSA KEY GENERATION")
    print("=" * 65)
    print(f"Given primes:                 p = {p}, q = {q}")
    print(f"Modulus N = p * q:            {p} * {q} = {N}")
    print(f"Totient phi(N) = (p-1)*(q-1): {p-1} * {q-1} = {phi}")
    print(f"Prime factorization of phi:   {phi} = {' * '.join(map(str, phi_factors))}")
    print("\n--- Evaluating Candidate Exponents e in {122, 123, 124, 125} ---")
    
    selected_e = None
    for e in candidates:
        g = math.gcd(e, phi)
        is_coprime = (g == 1)
        status = "ACCEPTED (Valid Public Exponent)" if is_coprime else f"REJECTED (gcd = {g} != 1)"
        print(f"  e = {e:3d}: gcd({e}, {phi}) = {g:2d} -> {status}")
        if is_coprime and selected_e is None:
            selected_e = e
            
    # Calculate private key d
    d = mod_inv(selected_e, phi)
    verification = (selected_e * d) % phi
    
    print("\n--- Extended Euclidean Algorithm Result for Private Key d ---")
    print(f"Selected Public Exponent:     e = {selected_e}")
    print(f"Private Key d = e^-1 mod phi: d = {selected_e}^-1 mod {phi} = {d}")
    print(f"Verification: (e * d) mod phi = ({selected_e} * {d}) mod {phi} = {verification} (Valid!)")
    print("\nSummary of Keypair for User A:")
    print(f"  Public Key:  k_pubA = (N = {N}, e = {selected_e})")
    print(f"  Private Key: k_priA = (d = {d})")
    print("=" * 65)

    # Session 6 Slide 10: Textbook RSA Example
    print("\nSESSION 6 SLIDE 10: TEXTBOOK RSA EXAMPLE")
    print("-" * 65)
    p_tb, q_tb, e_tb = 11, 3, 3
    n_tb = p_tb * q_tb
    phi_tb = (p_tb - 1) * (q_tb - 1)
    d_tb = mod_inv(e_tb, phi_tb)
    print(f"Given primes:                 p = {p_tb}, q = {q_tb}")
    print(f"Modulus N = p * q:            {n_tb}")
    print(f"Totient phi(N) = (p-1)*(q-1): {phi_tb}")
    print(f"Public Exponent e:            {e_tb} (gcd({e_tb}, {phi_tb}) = {math.gcd(e_tb, phi_tb)})")
    print(f"Private Key d = e^-1 mod phi: {e_tb}^-1 mod {phi_tb} = {d_tb}")
    print(f"Public Key: (N = {n_tb}, e = {e_tb}), Private Key: (d = {d_tb})")
    
    # Encrypt and Decrypt M = 15
    m_tb = 15
    c_tb = pow(m_tb, e_tb, n_tb)
    dec_tb = pow(c_tb, d_tb, n_tb)
    print(f"Encryption of M = {m_tb}:     C = {m_tb}^{e_tb} mod {n_tb} = {c_tb}")
    print(f"Decryption of C = {c_tb}:      M = {c_tb}^{d_tb} mod {n_tb} = {dec_tb} (Match: {dec_tb == m_tb})")
    print("=" * 65)

    return {
        "p": p,
        "q": q,
        "N": N,
        "phi": phi,
        "e": selected_e,
        "d": d
    }

if __name__ == "__main__":
    solve_rsa_keygen()
