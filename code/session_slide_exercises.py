"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Master Lecture Exercises Suite: Solves All Mathematical Exercises in Lecture Slides (Sessions 1 - 8)
Student ID: 23BA14056 (x = 56)
=============================================================================
"""

import math

def solve_all_slide_exercises():
    print("=" * 80)
    print("USTH CRYPTOGRAPHY - COMPLETE LECTURE SLIDE EXERCISE SOLUTIONS")
    print("=" * 80)

    # ---------------------------------------------------------
    # SESSION 1: MODULAR ARITHMETIC
    # ---------------------------------------------------------
    print("\n" + "=" * 75)
    print("1. SESSION 1 (Slides 24, 25, 26): MODULAR ARITHMETIC & EULER PHI")
    print("=" * 75)

    print("\n[Slide 24 - Exercise 1: Compute without calculator]")
    print(f"  (a) 15 * 29 mod 13 = (2 * 3) mod 13 = {(15 * 29) % 13}")
    print(f"  (b) 2 * 29 mod 13  = (2 * 3) mod 13 = {(2 * 29) % 13}")
    print(f"  (c) 2 * 3 mod 13   = {(2 * 3) % 13}")
    print(f"  (d) -11 * 3 mod 13 = (2 * 3) mod 13 = {(-11 * 3) % 13}")

    print("\n[Slide 25 - Exercise 2: Compute x as far as possible]")
    print(f"  (a) x = 3^2 mod 13   = {pow(3, 2, 13)}")
    print(f"  (b) x = 7^2 mod 13   = 49 mod 13 = {pow(7, 2, 13)}")
    print(f"  (c) x = 3^10 mod 13  = (3^3)^3 * 3 = 1^3 * 3 = {pow(3, 10, 13)}")
    print(f"  (d) x = 7^100 mod 13 = (7^12)^8 * 7^4 = 1^8 * 9 = {pow(7, 100, 13)}")
    inv_7 = pow(7, -1, 13)
    sol_x = (inv_7 * 11) % 13
    print(f"  (e) Solve 7*x = 11 mod 13:")
    print(f"      gcd(7, 13) = 1 ==> 7^(-1) mod 13 = {inv_7}")
    print(f"      x = 7^(-1) * 11 = {inv_7} * 11 mod 13 = {sol_x} (Check: (7 * {sol_x}) % 13 = {(7 * sol_x) % 13})")

    print("\n[Slide 26: Euler's Totient Phi(m) for m in {3, 4, 5, 9, 26}]")
    for m in [3, 4, 5, 9, 26]:
        factors = []
        d = 2
        temp = m
        while d * d <= temp:
            if temp % d == 0:
                factors.append(d)
                while temp % d == 0:
                    temp //= d
            d += 1
        if temp > 1:
            factors.append(temp)
        phi_val = m
        for p in factors:
            phi_val = (phi_val * (p - 1)) // p
        print(f"  Phi({m:<2}): prime factors {factors} ==> Phi({m}) = {phi_val}")

    # ---------------------------------------------------------
    # SESSION 2: CLASSICAL CIPHERS
    # ---------------------------------------------------------
    print("\n" + "=" * 75)
    print("2. SESSION 2 (Slide 15): SHIFT (CAESAR) CIPHER RULE DISCOVERY")
    print("=" * 75)
    p_text = "ictlab"
    c_text = "lfwode"
    k_rule = (ord(c_text[0]) - ord(p_text[0])) % 26
    print(f"  Plaintext : '{p_text}'")
    print(f"  Ciphertext: '{c_text}'")
    print(f"  Rule Discovery: 'i' ({ord('i') - ord('a')}) -> 'l' ({ord('l') - ord('a')}) ==> Shift key k = {k_rule}")
    enc_check = "".join(chr((ord(c) - ord('a') + k_rule) % 26 + ord('a')) for c in p_text)
    print(f"  Verification: Encrypting '{p_text}' with k={k_rule} gives '{enc_check}' (Match: {enc_check == c_text})")

    # ---------------------------------------------------------
    # SESSION 6: ASYMMETRIC CRYPTOGRAPHY (RSA)
    # ---------------------------------------------------------
    print("\n" + "=" * 75)
    print("3. SESSION 6 (Slides 10 & 11): RSA CRYPTOSYSTEM")
    print("=" * 75)
    print("[Slide 10: Textbook RSA Example]")
    p6, q6, e6 = 11, 3, 3
    n6 = p6 * q6
    phi6 = (p6 - 1) * (q6 - 1)
    d6 = pow(e6, -1, phi6)
    m6 = 15
    c6 = pow(m6, e6, n6)
    dec6 = pow(c6, d6, n6)
    print(f"  Primes: p = {p6}, q = {q6} ==> Modulus N = {n6}, Phi(N) = {phi6}")
    print(f"  Chosen e = {e6} ==> Private key d = {e6}^(-1) mod {phi6} = {d6}")
    print(f"  Encrypt M = {m6}: C = {m6}^{e6} mod {n6} = {c6}")
    print(f"  Decrypt C = {c6}: M = {c6}^{d6} mod {n6} = {dec6} (Match: {dec6 == m6})")

    print("\n[Slide 11: Repeated Squaring Method]")
    n6_2, e6_2, m6_2 = 33, 23, 5
    c6_2 = pow(m6_2, e6_2, n6_2)
    print(f"  Input: N = {n6_2}, e = {e6_2}, M = {m6_2}")
    print(f"  Exponent 23 in binary = {bin(e6_2)[2:]} (16 + 4 + 2 + 1)")
    print(f"  Calculation: C = 5^23 mod 33 = {c6_2}")

    # ---------------------------------------------------------
    # SESSION 7: DIGITAL SIGNATURES & HASHES
    # ---------------------------------------------------------
    print("\n" + "=" * 75)
    print("4. SESSION 7 (Slides 8, 12, 25): DIGITAL SIGNATURES & SHA-1")
    print("=" * 75)
    print("[Slide 8: ElGamal Digital Signature Example]")
    p7, a7, d7, k7 = 29, 2, 12, 5
    b7 = pow(a7, d7, p7)
    x7 = 15
    r7 = pow(a7, k7, p7)
    s7 = ((x7 - d7 * r7) * pow(k7, -1, p7 - 1)) % (p7 - 1)
    v1_7 = (pow(b7, r7, p7) * pow(r7, s7, p7)) % p7
    v2_7 = pow(a7, x7, p7)
    print(f"  Domain: p = {p7}, alpha = {a7}, private d = {d7} ==> public beta = {b7}")
    print(f"  Sign message x = {x7} with k_E = {k7}:")
    print(f"    r = {a7}^{k7} mod {p7} = {r7}")
    print(f"    s = ({x7} - {d7}*{r7})*{k7}^(-1) mod {p7-1} = {s7}")
    print(f"  Verify: v1 = (beta^r * r^s) mod p = {v1_7}, v2 = alpha^x mod p = {v2_7} ==> Valid: {v1_7 == v2_7}")

    print("\n[Slide 12: DSA Digital Signature Example]")
    p_dsa, q_dsa, a_dsa, d_dsa, k_dsa, h_dsa = 59, 29, 3, 7, 10, 26
    b_dsa = pow(a_dsa, d_dsa, p_dsa)
    r_dsa = pow(a_dsa, k_dsa, p_dsa) % q_dsa
    s_dsa = (pow(k_dsa, -1, q_dsa) * (h_dsa + d_dsa * r_dsa)) % q_dsa
    w_dsa = pow(s_dsa, -1, q_dsa)
    u1_dsa = (h_dsa * w_dsa) % q_dsa
    u2_dsa = (r_dsa * w_dsa) % q_dsa
    v_dsa = ((pow(a_dsa, u1_dsa, p_dsa) * pow(b_dsa, u2_dsa, p_dsa)) % p_dsa) % q_dsa
    print(f"  Params: p = {p_dsa}, q = {q_dsa}, alpha = {a_dsa}, d = {d_dsa}, k_E = {k_dsa}, h(x) = {h_dsa}")
    print(f"  Public key beta = {b_dsa}")
    print(f"  Signature: (r = {r_dsa}, s = {s_dsa})")
    print(f"  Verification: v = {v_dsa} == r ({r_dsa}) ==> Valid: {v_dsa == r_dsa}")

    print("\n[Slide 25: SHA-1 First Round Output]")
    print(f"  Condition: A0 = B0 = C0 = D0 = E0 = 0x00000000, Stage 1 (K_0 = 0x5A827999)")
    print(f"  For block x = 0...00: W_0 = 0x00000000 ==> A1 = 0x5A827999, B1=0, C1=0, D1=0, E1=0")
    print(f"  For block x = 0...01: W_0 = 0x00000000 (bit 512 is in W_15) ==> A1 = 0x5A827999, B1=0, C1=0, D1=0, E1=0")
    print(f"  Conclusion: Both inputs give IDENTICAL output (0x5A827999, 0, 0, 0, 0) after Round 1!")

    # ---------------------------------------------------------
    # SESSION 8: MITM ON DIFFIE-HELLMAN
    # ---------------------------------------------------------
    print("\n" + "=" * 75)
    print("5. SESSION 8 (Slide 18): ACTIVE MITM ATTACK ON DIFFIE-HELLMAN")
    print("=" * 75)
    p8, a8, a_priv, b_priv, o_priv = 467, 2, 228, 57, 16
    A_pub = pow(a8, a_priv, p8)
    B_pub = pow(a8, b_priv, p8)
    O_pub = pow(a8, o_priv, p8)
    
    # Oscar computations
    k_AO_oscar = pow(A_pub, o_priv, p8)
    k_BO_oscar = pow(B_pub, o_priv, p8)

    # Alice and Bob computations
    k_AO_alice = pow(O_pub, a_priv, p8)
    k_BO_bob = pow(O_pub, b_priv, p8)

    print(f"  Parameters: p = {p8}, alpha = {a8}")
    print(f"  Private: Alice a = {a_priv}, Bob b = {b_priv}, Oscar o = {o_priv}")
    print(f"  Public : Alice A = {A_pub}, Bob B = {B_pub}, Oscar O = {O_pub}")
    print(f"  (i)  Oscar calculates: k_AO = A^o mod p = {k_AO_oscar}, k_BO = B^o mod p = {k_BO_oscar}")
    print(f"  (ii) Alice & Bob calc: k_AO = O^a mod p = {k_AO_alice}, k_BO = O^b mod p = {k_BO_bob}")
    print(f"  --> Shared keys match: Alice-Oscar ({k_AO_alice == k_AO_oscar}), Bob-Oscar ({k_BO_bob == k_BO_oscar})")
    print("=" * 80)

def run_demo():
    solve_all_slide_exercises()


def custom_input():
    print("\n" + "=" * 75)
    print("SLIDE EXERCISES SELECTOR")
    print("=" * 75)
    print("Choose an option:")
    print("  [1] Run all slide exercise solutions (Sessions 2, 3, 6, 7, 8)")
    print("  [2] Open master interactive exam calculator (exam_calculator.py)")
    print("  [0] Exit")
    try:
        c = input("\nSelect [0-2, default 1]: ").strip()
        if c == "2":
            import exam_calculator
            exam_calculator.main_menu()
        elif c in ("", "1"):
            solve_all_slide_exercises()
        else:
            print("[*] Exiting.")
    except (KeyboardInterrupt, EOFError):
        pass


if __name__ == "__main__":
    import sys
    if "--demo" in sys.argv or (not sys.stdin.isatty() and len(sys.argv) <= 1):
        run_demo()
        sys.exit(0)
    if sys.stdin.isatty():
        custom_input()
    else:
        run_demo()