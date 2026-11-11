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


if __name__ == "__main__":
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
