# -*- coding: utf-8 -*-
"""
Script: solve_sha1_padding.py
Description: Solves Exercise 3 (SHA-1 Message Preprocessing & Padding).
Analyzes both l = 20260 bits (Printed on exam sheet) and l = 56 bits (Student ID).
"""

def solve_sha1_padding_for_len(l_bits, label=""):
    print(f"\n--- {label} (Length l = {l_bits} bits) ---")
    rem = l_bits % 512
    # Formula: (l + 1 + k) = 448 mod 512
    # k = (447 - (l mod 512)) mod 512
    k_zeros = (447 - rem) % 512
    
    # 64-bit Big-Endian binary representation of original length l
    length_bin_64 = f"{l_bits:064b}"
    length_hex_64 = f"0x{l_bits:016X}"
    
    total_len = l_bits + 1 + k_zeros + 64
    total_blocks = total_len // 512
    
    print(f"Original message length l:    {l_bits} bits")
    print(f"l mod 512:                    {rem} bits")
    print(f"Number of zero bits k to pad: (447 - {rem}) mod 512 = {k_zeros} bits")
    print(f"64-bit length field (Hex):    {length_hex_64}")
    print(f"Total length after padding:   {l_bits} + 1 + {k_zeros} + 64 = {total_len} bits")
    print(f"Total 512-bit blocks (L):     {total_len} / 512 = {total_blocks} blocks (Each block: 16 words x 32 bits)")
    return {
        "l": l_bits,
        "k_zeros": k_zeros,
        "hex_64": length_hex_64,
        "total_len": total_len,
        "blocks": total_blocks
    }

def solve_sha1_padding(custom_l=None):
    import sys
    if custom_l is None and len(sys.argv) > 1:
        try:
            custom_l = int(sys.argv[1])
        except ValueError:
            pass
    print("=" * 70)
    print("USTH FINAL EXAM 2025-2026 - EXERCISE 3: SHA-1 PADDING PREPROCESS")
    print("=" * 70)
    print("SHA-1 Preprocessing Rules (Session 7 Slide 20, Understanding Cryptography Sec 11.4):")
    print("  1. Append a single '1' bit to the original message.")
    print("  2. Append k '0' bits (0 <= k < 512) such that: (l + 1 + k) = 448 mod 512.")
    print("  3. Append the 64-bit Big-Endian binary representation of original length l.")
    print("  4. Total output length is an exact multiple of 512 bits (L * 512).")
    
    # Case 1: Printed on exam sheet (M = 20260 bits)
    solve_sha1_padding_for_len(20260, "Case A: Printed Exam Sheet Parameter (l = M = 20260 bits)")
    
    # Case 2: Personalized Student ID (l = 56 bits or custom)
    l_id = custom_l if custom_l is not None else 56
    solve_sha1_padding_for_len(l_id, f"Case B: Personalized Student ID (l = {l_id} bits)")
    print("=" * 70)

if __name__ == "__main__":
    solve_sha1_padding()
