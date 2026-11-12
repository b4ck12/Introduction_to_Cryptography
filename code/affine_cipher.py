import os
"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Algorithm: Affine Cipher (Encryption, Decryption, Key Space Analysis)
Reference: Session 2 (Classical Cryptosystems)
Student ID: 23BA14056 (x = 56)
=============================================================================
Theory:
  - Key: Pair (a, b) where a, b in Z_26 and gcd(a, 26) = 1.
  - Number of valid 'a' choices = Phi(26) = 12.
    Valid a in {1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25}.
  - Number of 'b' choices = 26.
  - Total key space = 12 * 26 = 312 keys.
  - Encryption:  c = (a * m + b) mod 26
  - Decryption:  m = a^(-1) * (c - b) mod 26, where a * a^(-1) = 1 (mod 26).
=============================================================================
"""

import math
from typing import Tuple, List

def get_valid_multipliers() -> List[int]:
    """Returns all values of 'a' in Z_26 such that gcd(a, 26) == 1."""
    return [a for a in range(1, 26) if math.gcd(a, 26) == 1]


def mod_inverse_26(a: int) -> int:
    """Computes a^(-1) mod 26 using extended Euclidean algorithm."""
    if math.gcd(a, 26) != 1:
        raise ValueError(f"Multiplier {a} is not coprime to 26 (gcd={math.gcd(a, 26)}). Cannot invert!")
    return pow(a, -1, 26)


def affine_encrypt(plaintext: str, a: int, b: int) -> str:
    """Encrypts plaintext using key (a, b)."""
    if math.gcd(a, 26) != 1:
        raise ValueError(f"Invalid key 'a' = {a}: gcd({a}, 26) must be 1!")
    
    ciphertext = []
    for char in plaintext:
        if char.isupper():
            m = ord(char) - ord('A')
            c = (a * m + b) % 26
            ciphertext.append(chr(c + ord('A')))
        elif char.islower():
            m = ord(char) - ord('a')
            c = (a * m + b) % 26
            ciphertext.append(chr(c + ord('a')))
        else:
            ciphertext.append(char)
    return "".join(ciphertext)


def affine_decrypt(ciphertext: str, a: int, b: int) -> str:
    """Decrypts ciphertext using key (a, b)."""
    a_inv = mod_inverse_26(a)
    plaintext = []
    for char in ciphertext:
        if char.isupper():
            c = ord(char) - ord('A')
            m = (a_inv * (c - b)) % 26
            plaintext.append(chr(m + ord('A')))
        elif char.islower():
            c = ord(char) - ord('a')
            m = (a_inv * (c - b)) % 26
            plaintext.append(chr(m + ord('a')))
        else:
            plaintext.append(char)
    return "".join(plaintext)


def custom_input():
    print("\n" + "=" * 65)
    print("CUSTOM EXAM INPUT: AFFINE CIPHER CALCULATOR (e(x) = a*x + b mod 26)")
    print("=" * 65)
    print("Choose operation:")
    print("  [1] Encrypt text with key (a, b)")
    print("  [2] Decrypt text with key (a, b)")
    try:
        op = input("Select [1/2, default 1]: ").strip()
        txt = input("Enter text string [e.g. ATTACK AT DAWN]: ").strip()
        if not txt:
            txt = "ATTACK AT DAWN"
        val_a = input("Enter multiplier a (must have gcd(a, 26)=1) [default 7]: ").strip()
        a = int(val_a, 0) if val_a else 7
        if math.gcd(a, 26) != 1:
            print(f"[-] ERROR: gcd({a}, 26) = {math.gcd(a, 26)} != 1. Multiplier 'a' must be coprime to 26!")
            return
        val_b = input("Enter shift b [0-25, default 4]: ").strip()
        b = int(val_b, 0) if val_b else 4
        if op == "2":
            res = affine_decrypt(txt, a, b)
            print(f"\n[=>] Decrypted text with key ({a}, {b}): '{res}'")
        else:
            res = affine_encrypt(txt, a, b)
            print(f"\n[=>] Encrypted ciphertext with key ({a}, {b}): '{res}'")
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}. Using default.")
        try:
            run_demo()
        except Exception:
            pass


def run_demo():
    print("=" * 65)
    print("DEMO: AFFINE CIPHER (KEY VALIDATION, ENCRYPT, DECRYPT)")
    print("=" * 65)

    valid_a = get_valid_multipliers()
    print(f"[+] Valid values for multiplier 'a' (coprime to 26): {valid_a}")
    print(f"[+] Total valid 'a': {len(valid_a)} = Phi(26)")
    print(f"[+] Total possible keys (a, b): {len(valid_a)} * 26 = {len(valid_a) * 26}\n")

    # Inverses table for all valid 'a'
    print("[+] Inverses a^(-1) mod 26 table:")
    for a in valid_a:
        inv = mod_inverse_26(a)
        print(f"    a = {a:>2}  ==>  a^(-1) = {inv:>2}  (check: ({a} * {inv}) % 26 = {(a * inv) % 26})")

    # Demo with student ID:
    # ID: 56. Let a = 7 (coprime to 26), b = 56 mod 26 = 4
    a_key = 7
    b_key = 56 % 26
    msg = "ATTACK AT DAWN"
    print(f"\n[+] Encryption Demo:")
    print(f"    Plaintext : '{msg}'")
    print(f"    Key (a, b): ({a_key}, {b_key})")
    
    cipher = affine_encrypt(msg, a_key, b_key)
    print(f"    Ciphertext: '{cipher}'")

    print(f"\n[+] Decryption Demo:")
    inv_a = mod_inverse_26(a_key)
    print(f"    Inverting key: a^(-1) = {inv_a}")
    decrypted = affine_decrypt(cipher, a_key, b_key)
    print(f"    Decrypted : '{decrypted}'")
    print(f"    Match     : {decrypted == msg}")


if __name__ == "__main__":
    import sys

    # Run demo test suite only if explicitly requested or in non-interactive test pipe
    if "--demo" in sys.argv or (not sys.stdin.isatty() and len(sys.argv) <= 1):
        run_demo()
        sys.exit(0)

    # Support CLI arguments: python affine_cipher.py "HELLO" 7 4
    if len(sys.argv) > 1 and not sys.argv[1].startswith("-"):
        txt = sys.argv[1]
        a = int(sys.argv[2], 0) if len(sys.argv) > 2 else 7
        b = int(sys.argv[3], 0) if len(sys.argv) > 3 else 4
        print(f"Encrypted: {affine_encrypt(txt, a, b)}")
        sys.exit(0)

    # Default: Open directly into Custom Exam Input prompt
    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
    else:
        try:
            custom_input()
        except (EOFError, KeyboardInterrupt):
            run_demo()