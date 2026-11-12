import os
"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Algorithm: DES (Data Encryption Standard) & Feistel Network
Reference: Session 4 (Block Ciphers & DES)
Student ID: 23BA14056 (x = 56)
=============================================================================
Theory:
  DES is a 16-round Feistel cipher operating on 64-bit blocks with 56-bit keys.
  - Feistel round equations:
      L_i = R_{i-1}
      R_i = L_{i-1} ^ F(R_{i-1}, K_i)
  - Feistel decryption (reversal):
      R_{i-1} = L_i
      L_{i-1} = R_i ^ F(L_i, K_i)
  - Crucial Property: Decryption is identical to encryption, simply using
    the subkeys in reverse order (K_16 down to K_1), regardless of F!
=============================================================================
"""

from typing import List, Tuple

# Key Schedule Shifts per round (16 rounds)
ROUND_SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def feistel_round(L_prev: int, R_prev: int, round_key: int, mask_32: int = 0xFFFFFFFF) -> Tuple[int, int]:
    """
    Simulates one Feistel round:
        L_curr = R_prev
        R_curr = L_prev ^ F(R_prev, round_key)
    """
    # Round function F (non-linear mixing function)
    # Using a hash-like bit mixer simulating E-box + S-box + P-box
    def F(R: int, K: int) -> int:
        temp = ((R * 0x5bd1e995) ^ K) & mask_32
        temp = ((temp >> 13) | (temp << 19)) & mask_32
        temp = (temp * 0xe6546b64) & mask_32
        return temp

    L_curr = R_prev
    R_curr = (L_prev ^ F(R_prev, round_key)) & mask_32
    return L_curr, R_curr


def feistel_reverse_round(L_curr: int, R_curr: int, round_key: int, mask_32: int = 0xFFFFFFFF) -> Tuple[int, int]:
    """
    Reverses one Feistel round:
        R_prev = L_curr
        L_prev = R_curr ^ F(L_curr, round_key)
    """
    def F(R: int, K: int) -> int:
        temp = ((R * 0x5bd1e995) ^ K) & mask_32
        temp = ((temp >> 13) | (temp << 19)) & mask_32
        temp = (temp * 0xe6546b64) & mask_32
        return temp

    R_prev = L_curr
    L_prev = (R_curr ^ F(L_curr, round_key)) & mask_32
    return L_prev, R_prev


def run_feistel_cipher(plaintext_64: int, keys: List[int], verbose: bool = True) -> int:
    """Runs 16-round Feistel encryption."""
    mask_32 = 0xFFFFFFFF
    L = (plaintext_64 >> 32) & mask_32
    R = plaintext_64 & mask_32

    if verbose:
        print(f"\n[+] Feistel Encryption (Plaintext = 0x{plaintext_64:016X}):")
        print(f"{'Round':<6} | {'Subkey K_i':<14} | {'L_i (Hex)':<12} | {'R_i (Hex)':<12}")
        print("-" * 55)
        print(f"{'init':<6} | {'-':<14} | {L:08X}{'':<4} | {R:08X}")

    for round_num, k in enumerate(keys, 1):
        L, R = feistel_round(L, R, k, mask_32)
        if verbose:
            print(f"Rnd {round_num:<2} | 0x{k:08X}{'':<4} | {L:08X}{'':<4} | {R:08X}")

    # Final swap: (R_16 || L_16)
    ciphertext_64 = (R << 32) | L
    if verbose:
        print("-" * 55)
        print(f"[=>] Ciphertext (after final swap): 0x{ciphertext_64:016X}\n")

    return ciphertext_64


def run_feistel_decipher(ciphertext_64: int, keys: List[int], verbose: bool = True) -> int:
    """Runs 16-round Feistel decryption using reversed keys."""
    mask_32 = 0xFFFFFFFF
    # In standard DES, the input to decipher is the ciphertext block
    # Upper 32 bits = R_16, Lower 32 bits = L_16
    L = (ciphertext_64 >> 32) & mask_32
    R = ciphertext_64 & mask_32

    if verbose:
        print(f"[+] Feistel Decryption (Ciphertext = 0x{ciphertext_64:016X}):")
        print(f"{'Round':<6} | {'Subkey K_i':<14} | {'L_i (Hex)':<12} | {'R_i (Hex)':<12}")
        print("-" * 55)
        print(f"{'init':<6} | {'-':<14} | {L:08X}{'':<4} | {R:08X}")

    reversed_keys = list(reversed(keys))
    for round_num, k in enumerate(reversed_keys, 1):
        L, R = feistel_round(L, R, k, mask_32)
        if verbose:
            print(f"Rnd {round_num:<2} | 0x{k:08X}{'':<4} | {L:08X}{'':<4} | {R:08X}")

    # Final swap on decryption restores (L_0 || R_0)
    plaintext_64 = (R << 32) | L
    if verbose:
        print("-" * 55)
        print(f"[=>] Recovered Plaintext: 0x{plaintext_64:016X}\n")

    return plaintext_64


def custom_input():
    print("\n" + "=" * 65)
    print("CUSTOM EXAM INPUT: 16-ROUND FEISTEL CIPHER")
    print("=" * 65)
    try:
        val_pt = input("Enter 64-bit plaintext hex [e.g. 0x0123456789ABCDEF]: ").strip()
        pt = int(val_pt, 16) if val_pt else 0x0123456789ABCDEF
        val_id = input("Enter seed/student ID for subkey derivation [default 56]: ").strip()
        sid = int(val_id, 0) if val_id else 56
        keys = [((sid * 104729 + i * 7919) & 0xFFFFFFFF) for i in range(16)]
        c = run_feistel_cipher(pt, keys, verbose=True)
        dec = run_feistel_decipher(c, keys, verbose=True)
        print(f"[=>] Invertibility: {dec == pt}")
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}. Using default.")
        try:
            run_demo()
        except Exception:
            pass


def run_demo():
    print("=" * 65)
    print("DEMO: DES FEISTEL STRUCTURE & INVERTIBILITY PROOF")
    print("=" * 65)

    # 16 sample 32-bit subkeys derived from student ID 56
    base_id = 56
    subkeys = [((base_id * 104729 + i * 7919) & 0xFFFFFFFF) for i in range(16)]

    # 64-bit plaintext
    plaintext = 0x0123456789ABCDEF

    # Run Encryption
    cipher = run_feistel_cipher(plaintext, subkeys, verbose=True)

    # Run Decryption
    decrypted = run_feistel_decipher(cipher, subkeys, verbose=True)

    print(f"Original Plaintext : 0x{plaintext:016X}")
    print(f"Decrypted Plaintext: 0x{decrypted:016X}")
    print(f"Feistel Invertibility Verified: {decrypted == plaintext}")


if __name__ == "__main__":
    import sys
    if "--demo" in sys.argv or (not sys.stdin.isatty() and len(sys.argv) <= 1):
        run_demo()
        sys.exit(0)
    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
    else:
        try:
            custom_input()
        except (EOFError, KeyboardInterrupt):
            run_demo()