"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Algorithm: Bitwise XOR Stream Cipher & ASCII Conversion
Reference: Session 3 (Stream Ciphers), Lab 1 Exercises 1, 2, 3
Student ID: 23BA14056 (x = 56)
=============================================================================
Theory:
  - Stream Cipher & One-Time Pad (OTP) rely on bitwise XOR (exclusive-OR, ^).
  - Algebraic properties:
      x ^ 0 = x
      x ^ x = 0
      (x ^ y) ^ y = x ^ (y ^ y) = x ^ 0 = x
  - Encryption:  c_i = m_i ^ k_i
  - Decryption:  m_i = c_i ^ k_i
=============================================================================
"""

from typing import List, Tuple

def str_to_bin_array(text: str) -> List[str]:
    """Converts a string into an array of 8-bit binary strings (Lab 1 Ex 1)."""
    return [format(ord(char), '08b') for char in text]


def bin_array_to_str(bin_list: List[str]) -> str:
    """Converts a list of 8-bit binary strings back to ASCII text."""
    return "".join([chr(int(b, 2)) for b in bin_list])


def xor_bytes(byte_seq_1: bytes, byte_seq_2: bytes) -> bytes:
    """Performs byte-by-byte XOR between two byte sequences."""
    return bytes([b1 ^ b2 for b1, b2 in zip(byte_seq_1, byte_seq_2)])


def stream_xor_demo(plaintext: str, key_bytes: bytes, verbose: bool = True) -> Tuple[bytes, str]:
    """
    Demonstrates stream encryption and decryption using XOR (Lab 1 Ex 2 & 3).
    """
    p_bytes = plaintext.encode('utf-8')
    if len(key_bytes) < len(p_bytes):
        # Repeat keystream if shorter
        key_bytes = (key_bytes * ((len(p_bytes) // len(key_bytes)) + 1))[:len(p_bytes)]

    c_bytes = xor_bytes(p_bytes, key_bytes)
    decrypted_bytes = xor_bytes(c_bytes, key_bytes)
    decrypted_text = decrypted_bytes.decode('utf-8', errors='replace')

    if verbose:
        print(f"\n[+] Stream Cipher XOR Demonstration:")
        print(f"{'Idx':<4} | {'Char':<5} | {'Plain (Hex)':<12} | {'Plain (Bin)':<10} | {'Key (Bin)':<10} | {'Cipher (Bin)':<12} | {'Cipher (Hex)':<12}")
        print("-" * 75)
        for i in range(len(p_bytes)):
            p = p_bytes[i]
            k = key_bytes[i]
            c = c_bytes[i]
            ch = chr(p) if 32 <= p <= 126 else '?'
            print(f"{i:<4} | {ch:<5} | 0x{p:02X}{'':<8} | {p:08b}   | {k:08b}  | {c:08b}     | 0x{c:02X}")
        print("-" * 75)

    return c_bytes, decrypted_text


if __name__ == "__main__":
    print("=" * 70)
    print("DEMO: BITWISE XOR STREAM CIPHER (LAB 1 EXERCISES 1, 2, 3)")
    print("=" * 70)

    # 1. Lab 1 Ex 1: String to Binary
    sample_text = "Crypto"
    bin_rep = str_to_bin_array(sample_text)
    print(f"\n1. Lab 1 Ex 1: String to Binary for '{sample_text}':")
    for ch, b in zip(sample_text, bin_rep):
        print(f"   '{ch}' -> ASCII {ord(ch):3d} -> Binary: {b}")

    # 2. Lab 1 Ex 2 & 3: Encrypt and Decrypt
    print("\n2. Lab 1 Ex 2 & 3: XOR Stream Cipher Encrypt & Decrypt:")
    msg = "USTH 2026"
    keystream = bytes([0x5A, 0x3F, 0x12, 0xA5, 0x88, 0x4B, 0x99, 0x21, 0x56])
    cipher_bytes, recovered = stream_xor_demo(msg, keystream, verbose=True)

    print(f"[=>] Ciphertext (Hex): {cipher_bytes.hex()}")
    print(f"[=>] Recovered Plaintext: '{recovered}'")
    print(f"[=>] Successful Decryption: {recovered == msg}")

    # 3. Student ID Check
    student_id = 56
    print(f"\n3. Student ID XOR property check (x = {student_id}):")
    k = 0xAA
    c = student_id ^ k
    m = c ^ k
    print(f"   ID: {student_id} (0x{student_id:02X}) ^ Key (0x{k:02X}) = Cipher: {c} (0x{c:02X})")
    print(f"   Cipher: {c} ^ Key (0x{k:02X}) = Original ID: {m} (Match: {m == student_id})")
