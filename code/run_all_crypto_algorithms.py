"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Master Execution Script: Run All 28 Cryptographic Calculation & Algorithm Scripts
Student ID: 23BA14056 (x = 56)
=============================================================================
"""

import os
import subprocess
import sys
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

ALGORITHM_SCRIPTS = [
    # 1. Modular Arithmetic & Foundations
    ("modular_arithmetic.py", "Modular Addition, Multiplication, Cayley Tables"),
    ("euclidean_gcd.py", "Euclidean Algorithm for GCD (Lab 2 Ex 1)"),
    ("extended_euclidean.py", "Extended Euclidean Algorithm & Modular Inverse (Lab 2 Ex 4)"),
    ("euler_totient_coprime.py", "Euler's Totient Phi(m) & Pairwise Coprimes (Lab 2 Ex 2)"),
    ("square_and_multiply.py", "Square-and-Multiply Fast Exponentiation (Lab 2 Ex 3)"),
    ("string_integer_conversion.py", "ASCII String <-> Integer Big-Endian Conversion (Lab 3 Ex 1 & 2)"),

    # 2. Classical Ciphers
    ("caesar_cipher.py", "Caesar Shift Cipher & 26-Key Brute-Force"),
    ("affine_cipher.py", "Affine Cipher (ax + b mod 26) & Key Validation"),
    ("vigenere_cipher.py", "Vigenère Polyalphabetic Cipher & Key Schedule"),

    # 3. Stream Ciphers
    ("binary_xor_stream.py", "Bitwise XOR Stream Cipher & OTP Properties (Lab 1 Ex 1, 2, 3)"),
    ("a51_stream_cipher.py", "A5/1 Stream Cipher (LFSR Majority Voting, Option 1 & 2)"),
    ("rc4_stream_cipher.py", "RC4 Stream Cipher (KSA & PRGA Keystream Generation)"),

    # 4. Block Ciphers & Modes
    ("des_sbox_lookup.py", "DES S-Box S1 Calculation for Student ID (56 -> 3)"),
    ("des_feistel_cipher.py", "DES 16-Round Feistel Network & Decryption Invertibility"),
    ("aes_galois_field.py", "AES Galois Field GF(2^8) Arithmetic, xtime & S-Box"),
    ("block_cipher_modes.py", "Block Cipher Modes: ECB, CBC, CFB, OFB, CTR"),

    # 5. Asymmetric Cryptosystems
    ("rsa_key_generation.py", "RSA Key Generation (p=139, q=227, e=125 -> d=30689)"),
    ("rsa_encryption_decryption.py", "RSA Encryption/Decryption (M=56 -> C=2365, M=20260)"),
    ("pki_rsa_certificate.py", "PKI Certificate Authority Verification (Exam 2024-2025)"),
    ("diffie_hellman_key_exchange.py", "Diffie-Hellman Key Exchange (p=27361 & p=51907)"),
    ("dhke_mitm_attack.py", "Man-in-the-Middle Attack Simulation on Unauthenticated DHKE"),

    # 6. Digital Signatures & Hash Functions
    ("elgamal_digital_signature.py", "ElGamal Digital Signature (k_E=105 vs k_E=107)"),
    ("dsa_digital_signature.py", "Digital Signature Algorithm (DSA) Generation & Verification"),
    ("sha1_padding_preprocess.py", "SHA-1 Padding & Block Count (l=20260 bits & l=56 bits)"),
    ("sha1_compression_function.py", "SHA-1 Full 80-Round Compression & 16-to-80 Expansion"),
    ("block_cipher_hash.py", "Block-Cipher-Based Hashes: Davies-Meyer, MMO, Miyaguchi-Preneel"),
    ("birthday_attack_collision.py", "Birthday Paradox & Collision Probability Bounds"),
    ("hmac_sha1.py", "HMAC-SHA1 Keyed Hash Authentication Code (RFC 2104)"),
    ("session_slide_exercises.py", "Master Lecture Slide Exercises Suite (Sessions 1 - 8)"),
]

def main():
    print("=" * 80)
    print("USTH CRYPTOGRAPHY - MASTER ALGORITHM & CALCULATION RUNNER")
    print("Student ID: 23BA14056 (x = 56)")
    print(f"Total Standalone Algorithm Scripts: {len(ALGORITHM_SCRIPTS)}")
    print("=" * 80)

    success_count = 0
    failure_count = 0
    results = []

    start_total_time = time.time()

    for idx, (filename, description) in enumerate(ALGORITHM_SCRIPTS, 1):
        file_path = os.path.join(SCRIPT_DIR, filename)
        print(f"\n[{idx:02d}/{len(ALGORITHM_SCRIPTS):02d}] Running: {filename}")
        print(f"       Topic: {description}")
        print("-" * 75)

        if not os.path.exists(file_path):
            print(f"[-] ERROR: File not found: {file_path}")
            failure_count += 1
            results.append((filename, False, 0.0, "File not found"))
            continue

        t0 = time.time()
        res = subprocess.run([sys.executable, file_path], capture_output=True, text=True)
        elapsed = time.time() - t0

        if res.returncode == 0:
            success_count += 1
            results.append((filename, True, elapsed, "PASSED"))
            # Print last 3 lines of output as summary
            lines = [ln for ln in res.stdout.strip().split("\n") if ln.strip()]
            summary_snippet = " | ".join(lines[-2:]) if len(lines) >= 2 else (lines[-1] if lines else "")
            print(f"       [+] Status: PASSED in {elapsed:.3f}s")
            print(f"       Summary: {summary_snippet[:90]}")
        else:
            failure_count += 1
            results.append((filename, False, elapsed, "FAILED"))
            print(f"       [-] Status: FAILED with exit code {res.returncode}")
            print(f"       Error: {res.stderr[:200]}")

    total_elapsed = time.time() - start_total_time

    print("\n" + "=" * 80)
    print("EXECUTION SUMMARY REPORT")
    print("=" * 80)
    print(f"{'Idx':<4} | {'Filename':<30} | {'Status':<8} | {'Elapsed':<8}")
    print("-" * 60)
    for idx, (fname, passed, elapsed, status) in enumerate(results, 1):
        status_str = "[OK]" if passed else "[FAIL]"
        print(f"{idx:<4} | {fname:<30} | {status_str:<8} | {elapsed:.3f}s")
    print("-" * 60)
    print(f"Total Scripts: {len(ALGORITHM_SCRIPTS)} | Passed: {success_count} | Failed: {failure_count}")
    print(f"Total Execution Time: {total_elapsed:.2f} seconds")
    print("=" * 80)

    if failure_count > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
