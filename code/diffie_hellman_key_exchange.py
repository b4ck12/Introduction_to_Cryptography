# -*- coding: utf-8 -*-
"""
Script: solve_dhke.py
Description: Solves Exercise 4 (Diffie-Hellman Key Exchange - DHKE).
Covers both exam variants:
  - Variant 1 (crop_ex3_4.png / Exam sheet): p = 27361, alpha = 6
  - Variant 2 (869026595...png / Slide problem): p = 51907, alpha = 6
Inputs: Alice private key a = 56 (Student ID), Bob private key b = C = 2365 (RSA Ciphertext).
"""

def solve_dhke_variant(p, alpha, a, b, label=""):
    print(f"\n--- {label} (p = {p}, alpha = {alpha}) ---")
    # Alice computes public key k_A = alpha^a mod p
    k_A = pow(alpha, a, p)
    # Bob computes public key k_B = alpha^b mod p
    k_B = pow(alpha, b, p)
    
    # Alice computes shared session key k_AB = (k_B)^a mod p
    k_AB_alice = pow(k_B, a, p)
    # Bob computes shared session key k_AB = (k_A)^b mod p
    k_AB_bob = pow(k_A, b, p)
    
    print(f"Alice private key:            a = {a}")
    print(f"Bob private key:              b = {b}")
    print(f"Alice public key k_A:         {alpha}^{a} mod {p} = {k_A}")
    print(f"Bob public key k_B:           {alpha}^{b} mod {p} = {k_B}")
    print(f"Alice computes shared key:    ({k_B})^{a} mod {p} = {k_AB_alice}")
    print(f"Bob computes shared key:      ({k_A})^{b} mod {p} = {k_AB_bob}")
    print(f"Shared Session Key Match:     k_AB = {k_AB_alice} (Verified: {k_AB_alice == k_AB_bob})")
    return {
        "p": p,
        "alpha": alpha,
        "k_A": k_A,
        "k_B": k_B,
        "k_AB": k_AB_alice
    }

def solve_dhke(student_id=56):
    import sys
    if len(sys.argv) > 1:
        try:
            student_id = int(sys.argv[1])
        except ValueError:
            pass
    print("=" * 70)
    print("USTH FINAL EXAM 2025-2026 - EXERCISE 4: DIFFIE-HELLMAN KEY EXCHANGE")
    print("=" * 70)
    a = student_id  # Alice private key: Student ID
    b = 2365        # Bob private key: RSA Ciphertext C from Exercise 2.3
    
    # Variant 1: From crop_ex3_4.png (p = 27361, alpha = 6)
    solve_dhke_variant(27361, 6, a, b, "Variant 1: Printed Exam Paper Parameters (p = 27361, alpha = 6)")
    
    # Variant 2: From 869026595...png (p = 51907, alpha = 6)
    solve_dhke_variant(51907, 6, a, b, "Variant 2: Class Exam Sheet Parameters (p = 51907, alpha = 6)")
    print("=" * 70)

if __name__ == "__main__":
    solve_dhke()
