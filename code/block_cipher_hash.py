import os
"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Algorithm: Block-Cipher-Based Hash Functions (Davies-Meyer, MMO, Miyaguchi-Preneel)
Reference: Session 7 (Hash Functions & Digital Signatures, Slides 16-21)
Student ID: 23BA14056 (x = 56)
=============================================================================
Theory:
  Given an ideal block cipher E_K(P):
  1. Davies-Meyer Construction:
     - Key is message block x_i
     - Plaintext is chaining variable h_{i-1}
     - Formula: h_i = E_{x_i}(h_{i-1}) ^ h_{i-1}
     - Used in MD4, MD5, SHA-1, SHA-2 family!

  2. Matyas-Meyer-Oseas (MMO) Construction:
     - Key is derived from chaining variable: g(h_{i-1})
     - Plaintext is message block x_i
     - Formula: h_i = E_{g(h_{i-1})}(x_i) ^ x_i

  3. Miyaguchi-Preneel Construction:
     - Extended MMO with 3-way XOR feed-forward:
     - Formula: h_i = E_{g(h_{i-1})}(x_i) ^ x_i ^ h_{i-1}
     - Used in ISO/IEC 10118-3 and Whirlpool!
=============================================================================
"""

from typing import List

BLOCK_SIZE = 8  # 64-bit blocks

def mock_block_cipher(key: bytes, plaintext: bytes) -> bytes:
    """Mock 64-bit block cipher E_k(P)."""
    k_int = int.from_bytes(key[:8].ljust(8, b'\x00'), 'big')
    p_int = int.from_bytes(plaintext[:8].ljust(8, b'\x00'), 'big')
    # Non-linear mixing simulation
    c_int = ((p_int ^ k_int) * 0x5bd1e9955bd1e995) & 0xFFFFFFFFFFFFFFFF
    c_int ^= (c_int >> 23)
    c_int = (c_int * 0x1b8735931b873593) & 0xFFFFFFFFFFFFFFFF
    return c_int.to_bytes(8, 'big')


def xor_bytes(b1: bytes, b2: bytes) -> bytes:
    return bytes([x ^ y for x, y in zip(b1, b2)])


def davies_meyer_step(h_prev: bytes, x_i: bytes) -> bytes:
    """h_i = E_{x_i}(h_{prev}) ^ h_{prev}"""
    enc = mock_block_cipher(key=x_i, plaintext=h_prev)
    return xor_bytes(enc, h_prev)


def matyas_meyer_oseas_step(h_prev: bytes, x_i: bytes) -> bytes:
    """h_i = E_{g(h_{prev})}(x_i) ^ x_i"""
    enc = mock_block_cipher(key=h_prev, plaintext=x_i)
    return xor_bytes(enc, x_i)


def miyaguchi_preneel_step(h_prev: bytes, x_i: bytes) -> bytes:
    """h_i = E_{g(h_{prev})}(x_i) ^ x_i ^ h_{prev}"""
    enc = mock_block_cipher(key=h_prev, plaintext=x_i)
    return xor_bytes(xor_bytes(enc, x_i), h_prev)


def custom_input():
    print("\n" + "=" * 70)
    print("CUSTOM EXAM INPUT: BLOCK CIPHER HASH CONSTRUCTIONS")
    print("=" * 70)
    try:
        raw_x = input("Enter 8-byte message block [e.g. MSG_BLK1]: ").strip()
        x_b = raw_x.encode("utf-8")[:8] if raw_x else b"MSG_BLK1"
        x_b = x_b.ljust(8, b'\0')
        raw_iv = input("Enter 8-byte initial IV [e.g. INITVEC0]: ").strip()
        iv_b = raw_iv.encode("utf-8")[:8] if raw_iv else b"INITVEC0"
        iv_b = iv_b.ljust(8, b'\0')

        h_dm = davies_meyer_step(iv_b, x_b)
        h_mmo = matyas_meyer_oseas_step(iv_b, x_b)
        h_mp = miyaguchi_preneel_step(iv_b, x_b)

        print(f"\n[+] Input Message Block x_i: {x_b} (Hex: 0x{x_b.hex()})")
        print(f"[+] Initial IV h_{{i-1}}   : {iv_b} (Hex: 0x{iv_b.hex()})")
        print(f"\n[=>] Davies-Meyer Step       : 0x{h_dm.hex()}")
        print(f"[=>] Matyas-Meyer-Oseas Step : 0x{h_mmo.hex()}")
        print(f"[=>] Miyaguchi-Preneel Step  : 0x{h_mp.hex()}")
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}. Using default.")
        try:
            run_demo()
        except Exception:
            pass


def run_demo():
    print("=" * 70)
    print("DEMO: BLOCK-CIPHER-BASED HASH CONSTRUCTIONS")
    print("=" * 70)

    # Initial chaining variable IV (64 bits)
    IV = b"INITVEC0"
    # Sequence of 3 64-bit message blocks
    blocks = [b"MSG_BLK1", b"MSG_BLK2", b"ID23BA56"]

    print(f"Initial Chaining IV: 0x{IV.hex()}")
    for idx, blk in enumerate(blocks):
        print(f"Message Block x_{idx+1}: '{blk.decode()}' (Hex: 0x{blk.hex()})")

    # 1. Davies-Meyer Hash
    print("\n1. Davies-Meyer Construction: h_i = E_{x_i}(h_{i-1}) ^ h_{i-1}")
    h_dm = IV
    for idx, blk in enumerate(blocks, 1):
        h_dm = davies_meyer_step(h_dm, blk)
        print(f"   Step {idx}: h_{idx} = 0x{h_dm.hex()}")
    print(f"   [=>] Final Davies-Meyer Digest: 0x{h_dm.hex()}")

    # 2. Matyas-Meyer-Oseas Hash
    print("\n2. Matyas-Meyer-Oseas Construction: h_i = E_{h_{i-1}}(x_i) ^ x_i")
    h_mmo = IV
    for idx, blk in enumerate(blocks, 1):
        h_mmo = matyas_meyer_oseas_step(h_mmo, blk)
        print(f"   Step {idx}: h_{idx} = 0x{h_mmo.hex()}")
    print(f"   [=>] Final MMO Digest: 0x{h_mmo.hex()}")

    # 3. Miyaguchi-Preneel Hash
    print("\n3. Miyaguchi-Preneel Construction: h_i = E_{h_{i-1}}(x_i) ^ x_i ^ h_{i-1}")
    h_mp = IV
    for idx, blk in enumerate(blocks, 1):
        h_mp = miyaguchi_preneel_step(h_mp, blk)
        print(f"   Step {idx}: h_{idx} = 0x{h_mp.hex()}")
    print(f"   [=>] Final Miyaguchi-Preneel Digest: 0x{h_mp.hex()}")


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