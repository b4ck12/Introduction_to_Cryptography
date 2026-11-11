# -*- coding: utf-8 -*-
"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Master Interactive Exam Calculator & Solver Suite
Student ID: 23BA14056 (x = 56)
=============================================================================
Description:
  Interactive menu-driven calculator designed specifically for taking exams
  and solving homework exercises with custom numbers and parameters.
=============================================================================
"""

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

# Import custom input handlers from each module
try:
    import modular_arithmetic
    import euclidean_gcd
    import extended_euclidean
    import euler_totient_coprime
    import square_and_multiply
    import string_integer_conversion
    import caesar_cipher
    import affine_cipher
    import vigenere_cipher
    import binary_xor_stream
    import a51_stream_cipher
    import rc4_stream_cipher
    import des_sbox_lookup
    import des_feistel_cipher
    import aes_galois_field
    import block_cipher_modes
    import rsa_key_generation
    import rsa_encryption_decryption
    import pki_rsa_certificate
    import diffie_hellman_key_exchange
    import dhke_mitm_attack
    import elgamal_digital_signature
    import dsa_digital_signature
    import sha1_padding_preprocess
    import sha1_compression_function
    import block_cipher_hash
    import birthday_attack_collision
    import hmac_sha1
    import session_slide_exercises
except ImportError as e:
    print(f"[-] Import error: {e}")

MENU = """
================================================================================
   USTH CRYPTOGRAPHY - ALL-IN-ONE EXAM SOLVER & INTERACTIVE CALCULATOR
================================================================================
[1]  Modular Arithmetic (a+b, a-b, a*b, a^b mod m, linear congruence a*x=b)
[2]  Euclidean Algorithm (GCD division steps)
[3]  Extended Euclidean Algorithm & Modular Inverse (a^-1 mod m)
[4]  Euler's Totient Phi(m) & Coprime Pairs Checker
[5]  Square-and-Multiply Fast Exponentiation (x^H mod m)
[6]  ASCII String <-> Integer Big-Endian Converter
[7]  Caesar Cipher (Shift Encrypt, Decrypt & 26-Key Brute-Force)
[8]  Affine Cipher (e(x) = a*x + b mod 26)
[9]  Vigenere Cipher (Polyalphabetic Encrypt & Decrypt)
[10] Bitwise XOR Stream Cipher & OTP Properties
[11] A5/1 Stream Cipher (LFSR Majority Clocking Simulation)
[12] RC4 Stream Cipher (KSA & PRGA Keystream Generator)
[13] DES S1-Box Lookup (Student ID or 6-bit Binary)
[14] DES 16-Round Feistel Cipher Network & Invertibility
[15] AES Galois Field GF(2^8) Arithmetic, xtime, S-Box & MixColumns
[16] Block Cipher Modes (ECB, CBC, CTR)
[17] RSA Key Generation (p, q, candidate e -> d)
[18] RSA Encryption & Decryption (C = M^e mod N, M = C^d mod N)
[19] PKI RSA Certificate Authority Digital Signature
[20] Diffie-Hellman Key Exchange (p, alpha, a, b -> shared key)
[21] Diffie-Hellman Man-in-the-Middle (MitM) Attack Simulation
[22] ElGamal Digital Signature (p, alpha, d, k_E, x -> (r, s))
[23] DSA Digital Signature (p, q, alpha, d, k_E, h -> (r, s))
[24] SHA-1 Message Preprocessing & Zero Padding (l bits -> k, L)
[25] SHA-1 80-Round Compression & 16-to-80 Expansion
[26] Block-Cipher-Based Hashes (Davies-Meyer, MMO, Miyaguchi-Preneel)
[27] Birthday Paradox & Collision Probability Bounds
[28] HMAC-SHA1 Keyed Hash Authentication Code (RFC 2104)
[29] Session Slide Exercises Suite (Sessions 1 - 8)
[0]  Exit
================================================================================
"""

DISPATCH = {
    1: lambda: modular_arithmetic.custom_input(),
    2: lambda: euclidean_gcd.custom_input(),
    3: lambda: extended_euclidean.custom_input(),
    4: lambda: euler_totient_coprime.custom_input(),
    5: lambda: square_and_multiply.custom_input(),
    6: lambda: string_integer_conversion.custom_input(),
    7: lambda: caesar_cipher.custom_input(),
    8: lambda: affine_cipher.custom_input(),
    9: lambda: vigenere_cipher.custom_input(),
    10: lambda: binary_xor_stream.custom_input(),
    11: lambda: a51_stream_cipher.custom_input(),
    12: lambda: rc4_stream_cipher.custom_input(),
    13: lambda: des_sbox_lookup.custom_input(),
    14: lambda: des_feistel_cipher.custom_input(),
    15: lambda: aes_galois_field.custom_input(),
    16: lambda: block_cipher_modes.custom_input(),
    17: lambda: rsa_key_generation.custom_input(),
    18: lambda: rsa_encryption_decryption.custom_input(),
    19: lambda: pki_rsa_certificate.custom_input(),
    20: lambda: diffie_hellman_key_exchange.custom_input(),
    21: lambda: dhke_mitm_attack.custom_input(),
    22: lambda: elgamal_digital_signature.custom_input(),
    23: lambda: dsa_digital_signature.custom_input(),
    24: lambda: sha1_padding_preprocess.custom_input(),
    25: lambda: sha1_compression_function.custom_input(),
    26: lambda: block_cipher_hash.custom_input(),
    27: lambda: birthday_attack_collision.custom_input(),
    28: lambda: hmac_sha1.custom_input(),
    29: lambda: session_slide_exercises.solve_all_slide_exercises(),
}

def main():
    while True:
        print(MENU)
        try:
            choice_str = input("Select an algorithm to solve [0-29]: ").strip()
            if not choice_str:
                continue
            choice = int(choice_str)
            if choice == 0:
                print("\n[+] Exiting Exam Solver. Good luck on your exam!\n")
                break
            if choice in DISPATCH:
                DISPATCH[choice]()
                input("\n[Press Enter to return to main menu...]")
            else:
                print(f"[-] Invalid option {choice}. Please choose between 0 and 29.")
        except (ValueError, KeyboardInterrupt, EOFError):
            print("\n[+] Exiting Exam Solver.\n")
            break

if __name__ == "__main__":
    main()
