import os
"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Algorithm: Galois Field GF(2^8) Arithmetic & AES S-Box / MixColumns
Reference: Session 5 (Advanced Encryption Standard - AES)
Student ID: 23BA14056 (x = 56)
=============================================================================
Theory:
  AES operates on byte elements of the finite field GF(2^8).
  - Irreducible polynomial: m(x) = x^8 + x^4 + x^3 + x + 1 (0x11B in hex).
  - Addition in GF(2^8): Bitwise XOR (^).
  - Multiplication by x (0x02) in GF(2^8) is called 'xtime':
      xtime(b) = ((b << 1) ^ 0x1B) & 0xFF  if (b & 0x80) != 0 else (b << 1)
  - Multiplication of any two elements a * b uses repeated xtime and addition.
  - AES MixColumns multiplies each 4-byte column by the circulant MDS matrix:
      [02 03 01 01]
      [01 02 03 01]
      [01 01 02 03]
      [03 01 01 02]
  - AES S-Box affine mapping:
      S(a) = Affine(a^(-1) in GF(2^8)) ^ 0x63
=============================================================================
"""

from typing import List, Tuple

IRREDUCIBLE_POLY = 0x11B  # x^8 + x^4 + x^3 + x + 1

def xtime(b: int) -> int:
    """Multiplies a byte by x (0x02) in GF(2^8)."""
    b &= 0xFF
    if b & 0x80:
        return ((b << 1) ^ 0x1B) & 0xFF
    return (b << 1) & 0xFF


def gf_multiply(a: int, b: int) -> int:
    """
    Multiplies two bytes a and b in GF(2^8) modulo x^8 + x^4 + x^3 + x + 1
    using Russian Peasant multiplication (repeated xtime and XOR).
    """
    res = 0
    temp_a = a & 0xFF
    temp_b = b & 0xFF
    while temp_b > 0:
        if temp_b & 1:
            res ^= temp_a
        temp_a = xtime(temp_a)
        temp_b >>= 1
    return res


def gf_inverse(a: int) -> int:
    """
    Finds the multiplicative inverse of a in GF(2^8).
    In GF(2^8), a^(255) = 1 ==> a^(-1) = a^(254).
    For a == 0, returns 0 by AES convention.
    """
    if a == 0:
        return 0
    res = 1
    base = a
    power = 254  # 2^8 - 2
    while power > 0:
        if power & 1:
            res = gf_multiply(res, base)
        base = gf_multiply(base, base)
        power >>= 1
    return res


def aes_sbox_byte(byte_val: int) -> int:
    """
    Computes AES S-box substitution for a single byte:
    1. Multiplicative inversion in GF(2^8).
    2. Affine transformation over GF(2).
    """
    inv = gf_inverse(byte_val)
    # Affine transformation
    s = inv
    transformed = 0
    for i in range(8):
        bit = (
            ((s >> i) & 1) ^
            ((s >> ((i + 4) % 8)) & 1) ^
            ((s >> ((i + 5) % 8)) & 1) ^
            ((s >> ((i + 6) % 8)) & 1) ^
            ((s >> ((i + 7) % 8)) & 1) ^
            ((0x63 >> i) & 1)
        )
        transformed |= (bit << i)
    return transformed


def aes_mix_single_column(col: List[int]) -> List[int]:
    """
    Multiplies a 4-byte column by the standard AES MixColumns matrix:
        [02 03 01 01]
        [01 02 03 01]
        [01 01 02 03]
        [03 01 01 02]
    """
    s0, s1, s2, s3 = col
    d0 = gf_multiply(0x02, s0) ^ gf_multiply(0x03, s1) ^ s2 ^ s3
    d1 = s0 ^ gf_multiply(0x02, s1) ^ gf_multiply(0x03, s2) ^ s3
    d2 = s0 ^ s1 ^ gf_multiply(0x02, s2) ^ gf_multiply(0x03, s3)
    d3 = gf_multiply(0x03, s0) ^ s1 ^ s2 ^ gf_multiply(0x02, s3)
    return [d0, d1, d2, d3]


def custom_input():
    print("\n" + "=" * 65)
    print("CUSTOM EXAM INPUT: AES GF(2^8) & S-BOX CALCULATOR")
    print("=" * 65)
    print("Choose operation:")
    print("  [1] Multiply two bytes in GF(2^8) (mod x^8 + x^4 + x^3 + x + 1)")
    print("  [2] Compute xtime(b) (multiplication by 0x02)")
    print("  [3] Compute GF(2^8) Inversion & AES S-Box output for a byte")
    print("  [4] AES MixColumns Transform for a 4-byte column")
    try:
        op = input("Select [1/2/3/4, default 1]: ").strip()
        if op == "2":
            val_b = input("Enter byte in hex [e.g. 57]: ").strip()
            b = int(val_b, 16) if val_b else 0x57
            res = xtime(b)
            print(f"\n[=>] xtime(0x{b:02X}) = 0x{res:02X} (Binary: {bin(res)})")
        elif op == "3":
            val_b = input("Enter byte in hex or int [e.g. 0x38 or 56]: ").strip()
            b = int(val_b, 0) if val_b else 0x38
            inv = gf_inverse(b)
            s_out = aes_sbox_byte(b)
            print(f"\n[=>] Input byte: 0x{b:02X}")
            print(f"    GF(2^8) Inverse : 0x{inv:02X} (Check: 0x{b:02X} * 0x{inv:02X} = 0x{gf_multiply(b, inv):02X})")
            print(f"    AES S-Box Output: 0x{s_out:02X}")
        elif op == "4":
            raw_col = input("Enter 4 hex bytes separated by spaces [e.g. DB 13 53 45]: ").strip()
            col = [int(x, 16) for x in raw_col.split()] if raw_col else [0xDB, 0x13, 0x53, 0x45]
            mixed = aes_mix_single_column(col)
            print(f"\n[=>] Input Column : {[f'0x{x:02X}' for x in col]}")
            print(f"    Output Column: {[f'0x{x:02X}' for x in mixed]}")
        else:
            val_a = input("Enter first byte in hex [e.g. 57]: ").strip()
            a = int(val_a, 16) if val_a else 0x57
            val_b = input("Enter second byte in hex [e.g. 83]: ").strip()
            b = int(val_b, 16) if val_b else 0x83
            prod = gf_multiply(a, b)
            print(f"\n[=>] 0x{a:02X} * 0x{b:02X} in GF(2^8) = 0x{prod:02X}")
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}. Using default.")
        try:
            run_demo()
        except Exception:
            pass


def run_demo():
    print("=" * 65)
    print("DEMO: AES GALOIS FIELD GF(2^8) ARITHMETIC & S-BOX")
    print("=" * 65)

    # 1. GF(2^8) multiplication demo
    a, b = 0x57, 0x83  # Classic textbook example
    prod = gf_multiply(a, b)
    print(f"\n1. GF(2^8) Multiplication:")
    print(f"   0x{a:02X} * 0x{b:02X} = 0x{prod:02X} (Expected: 0xC1, Match: {prod == 0xC1})")

    # 2. Inversion in GF(2^8)
    student_id = 56  # 0x38
    inv_56 = gf_inverse(student_id)
    check_inv = gf_multiply(student_id, inv_56)
    print(f"\n2. GF(2^8) Inversion for Student ID (0x{student_id:02X}):")
    print(f"   Inverse of 0x{student_id:02X} = 0x{inv_56:02X}")
    print(f"   Check: 0x{student_id:02X} * 0x{inv_56:02X} = 0x{check_inv:02X} (Expected: 0x01, Match: {check_inv == 0x01})")

    # 3. AES S-Box generation test
    print(f"\n3. AES S-Box Computation:")
    test_inputs = [0x00, 0x01, 0x53, 0x38]  # 0x38 is 56 (student ID)
    for inp in test_inputs:
        s_out = aes_sbox_byte(inp)
        print(f"   S-Box(0x{inp:02X}) = 0x{s_out:02X}")
    # Known standard: S(0x00) = 0x63, S(0x01) = 0x7C, S(0x53) = 0xED
    print(f"   Standard Validation: S(0x00) == 0x63 -> {aes_sbox_byte(0x00) == 0x63}")
    print(f"   Standard Validation: S(0x01) == 0x7C -> {aes_sbox_byte(0x01) == 0x7C}")
    print(f"   Standard Validation: S(0x53) == 0xED -> {aes_sbox_byte(0x53) == 0xED}")

    # 4. MixColumns demo
    print(f"\n4. AES MixColumns Single Column Transform:")
    sample_col = [0xDB, 0x13, 0x53, 0x45]
    mixed_col = aes_mix_single_column(sample_col)
    expected_mixed = [0x8E, 0x4D, 0xA1, 0xBC]
    print(f"   Input Column : {[f'0x{x:02X}' for x in sample_col]}")
    print(f"   Output Column: {[f'0x{x:02X}' for x in mixed_col]}")
    print(f"   Expected     : {[f'0x{x:02X}' for x in expected_mixed]}")
    print(f"   Match        : {mixed_col == expected_mixed}")


if __name__ == "__main__":
    import sys

    if "--demo" in sys.argv or (not sys.stdin.isatty() and len(sys.argv) <= 1):
        run_demo()
        sys.exit(0)

    # Support CLI arguments: python aes_galois_field.py 0x57 0x83
    if len(sys.argv) > 1 and sys.argv[1] not in ("-i", "--interactive", "--custom"):
        try:
            a = int(sys.argv[1], 0)
            b = int(sys.argv[2], 0) if len(sys.argv) > 2 else 0x02
            print(f"0x{a:02X} * 0x{b:02X} = 0x{gf_multiply(a, b):02X}")
            sys.exit(0)
        except Exception:
            pass

    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
    else:
        try:
            custom_input()
        except (EOFError, KeyboardInterrupt):
            run_demo()