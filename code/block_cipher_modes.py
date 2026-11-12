import os
"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Algorithm: Block Cipher Modes of Operation (ECB, CBC, CFB, OFB, CTR)
Reference: Session 5 (Modes of Operation)
Student ID: 23BA14056 (x = 56)
=============================================================================
Theory:
  Given a block cipher E_K(.) and D_K(.) operating on fixed block size (e.g. 8 bytes):
  1. ECB (Electronic Codebook):
     - Enc: C_i = E_K(P_i)
     - Dec: P_i = D_K(C_i)
     - Flaw: Preserves patterns; P_i == P_j ==> C_i == C_j.
  2. CBC (Cipher Block Chaining):
     - Enc: C_0 = IV; C_i = E_K(P_i ^ C_{i-1})
     - Dec: P_i = D_K(C_i) ^ C_{i-1}
  3. CFB (Cipher Feedback):
     - Enc: C_0 = IV; C_i = P_i ^ E_K(C_{i-1})
     - Dec: P_i = C_i ^ E_K(C_{i-1})
  4. OFB (Output Feedback):
     - Stream mode: s_0 = IV; s_i = E_K(s_{i-1}); C_i = P_i ^ s_i
     - Dec: P_i = C_i ^ s_i
  5. CTR (Counter Mode):
     - Stream mode: s_i = E_K(IV + i); C_i = P_i ^ s_i
     - Dec: P_i = C_i ^ s_i (Parallelizable, random access)
=============================================================================
"""

from typing import List, Tuple

BLOCK_SIZE = 8  # 8 bytes (64 bits)

def mock_encrypt_block(block: bytes, key: bytes) -> bytes:
    """Mock invertible block cipher encryption (XOR permutation hash)."""
    res = bytearray(BLOCK_SIZE)
    k_val = sum(key) & 0xFF
    for i in range(BLOCK_SIZE):
        b = (block[i] + k_val + i * 17) & 0xFF
        # rotate left by 3 bits
        b = ((b << 3) | (b >> 5)) & 0xFF
        res[i] = b ^ 0x5A
    return bytes(res)


def mock_decrypt_block(cipher_block: bytes, key: bytes) -> bytes:
    """Inverts mock_encrypt_block."""
    res = bytearray(BLOCK_SIZE)
    k_val = sum(key) & 0xFF
    for i in range(BLOCK_SIZE):
        b = cipher_block[i] ^ 0x5A
        # rotate right by 3 bits
        b = ((b >> 3) | (b << 5)) & 0xFF
        b = (b - k_val - i * 17) & 0xFF
        res[i] = b
    return bytes(res)


def pad(data: bytes) -> bytes:
    """PKCS#7 padding to 8-byte block size."""
    pad_len = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + bytes([pad_len] * pad_len)


def unpad(data: bytes) -> bytes:
    """Removes PKCS#7 padding."""
    pad_len = data[-1]
    return data[:-pad_len]


# --- Modes Implementation ---

def encrypt_ecb(data: bytes, key: bytes) -> bytes:
    padded = pad(data)
    out = b""
    for i in range(0, len(padded), BLOCK_SIZE):
        blk = padded[i:i+BLOCK_SIZE]
        out += mock_encrypt_block(blk, key)
    return out

def decrypt_ecb(cipher: bytes, key: bytes) -> bytes:
    out = b""
    for i in range(0, len(cipher), BLOCK_SIZE):
        blk = cipher[i:i+BLOCK_SIZE]
        out += mock_decrypt_block(blk, key)
    return unpad(out)


def encrypt_cbc(data: bytes, key: bytes, iv: bytes) -> bytes:
    padded = pad(data)
    out = b""
    prev = iv
    for i in range(0, len(padded), BLOCK_SIZE):
        blk = padded[i:i+BLOCK_SIZE]
        xored = bytes([b1 ^ b2 for b1, b2 in zip(blk, prev)])
        enc = mock_encrypt_block(xored, key)
        out += enc
        prev = enc
    return out

def decrypt_cbc(cipher: bytes, key: bytes, iv: bytes) -> bytes:
    out = b""
    prev = iv
    for i in range(0, len(cipher), BLOCK_SIZE):
        blk = cipher[i:i+BLOCK_SIZE]
        dec = mock_decrypt_block(blk, key)
        xored = bytes([b1 ^ b2 for b1, b2 in zip(dec, prev)])
        out += xored
        prev = blk
    return unpad(out)


def encrypt_ctr(data: bytes, key: bytes, nonce: int) -> bytes:
    out = bytearray()
    for idx, b in enumerate(data):
        blk_idx = idx // BLOCK_SIZE
        byte_offset = idx % BLOCK_SIZE
        counter_block = ((nonce + blk_idx) & 0xFFFFFFFFFFFFFFFF).to_bytes(BLOCK_SIZE, 'big')
        keystream_block = mock_encrypt_block(counter_block, key)
        out.append(b ^ keystream_block[byte_offset])
    return bytes(out)


def custom_input():
    print("\n" + "=" * 65)
    print("CUSTOM EXAM INPUT: BLOCK CIPHER MODES (ECB, CBC, CTR)")
    print("=" * 65)
    try:
        raw_pt = input("Enter plaintext string [e.g. SECRET EXAM MESSAGE]: ").strip()
        pt = raw_pt.encode("utf-8") if raw_pt else b"SECRET EXAM MESSAGE"
        raw_key = input("Enter 8-byte key [e.g. USTH2026]: ").strip()
        k = raw_key.encode("utf-8")[:8] if raw_key else b"USTH2026"
        k = k.ljust(8, b'\0')
        raw_iv = input("Enter 8-byte IV for CBC [e.g. INITVEC1]: ").strip()
        iv_b = raw_iv.encode("utf-8")[:8] if raw_iv else b"INITVEC1"
        iv_b = iv_b.ljust(8, b'\0')

        print(f"\n[+] Input Plaintext: {pt}")
        print(f"[+] Key (8 bytes)  : {k}")
        print(f"[+] IV (8 bytes)   : {iv_b}")

        c_ecb = encrypt_ecb(pt, k)
        c_cbc = encrypt_cbc(pt, k, iv_b)
        c_ctr = encrypt_ctr(pt, k, 1000)

        print(f"\n[=>] ECB Ciphertext (Hex): {c_ecb.hex()}")
        print(f"[=>] CBC Ciphertext (Hex): {c_cbc.hex()}")
        print(f"[=>] CTR Ciphertext (Hex): {c_ctr.hex()}")
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}. Using default.")
        try:
            run_demo()
        except Exception:
            pass


def run_demo():
    print("=" * 65)
    print("DEMO: BLOCK CIPHER MODES OF OPERATION (ECB, CBC, CTR)")
    print("=" * 65)

    key = b"USTH2026"
    iv = b"INITVEC1"
    nonce = 1000

    # Test pattern leakage in ECB: identical repeated blocks
    plaintext = b"HELLO_CRYPTOGRAPHY_STUDENT_ID_056_HELLO_CRYPTOGRAPHY"
    print(f"Plaintext: {plaintext}")

    # 1. ECB Mode
    c_ecb = encrypt_ecb(plaintext, key)
    p_ecb = decrypt_ecb(c_ecb, key)
    print(f"\n[+] ECB Mode:")
    print(f"    Ciphertext (Hex): {c_ecb.hex()[:48]}...")
    print(f"    Decrypted text  : {p_ecb}")
    print(f"    Match           : {p_ecb == plaintext}")

    # 2. CBC Mode
    c_cbc = encrypt_cbc(plaintext, key, iv)
    p_cbc = decrypt_cbc(c_cbc, key, iv)
    print(f"\n[+] CBC Mode:")
    print(f"    Ciphertext (Hex): {c_cbc.hex()[:48]}...")
    print(f"    Decrypted text  : {p_cbc}")
    print(f"    Match           : {p_cbc == plaintext}")

    # 3. CTR Mode (No padding required)
    c_ctr = encrypt_ctr(plaintext, key, nonce)
    p_ctr = encrypt_ctr(c_ctr, key, nonce)  # CTR decrypt is encrypt
    print(f"\n[+] CTR Mode (Counter stream):")
    print(f"    Ciphertext (Hex): {c_ctr.hex()[:48]}...")
    print(f"    Decrypted text  : {p_ctr}")
    print(f"    Match           : {p_ctr == plaintext}")


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