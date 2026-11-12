import os
"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Algorithm: Hash-based Message Authentication Code (HMAC-SHA1)
Reference: Session 8 (Message Authentication Codes - MACs)
Student ID: 23BA14056 (x = 56)
=============================================================================
Theory:
  HMAC is defined in RFC 2104 and FIPS 198:
      HMAC_K(M) = H( (K^+ ^ opad) || H( (K^+ ^ ipad) || M ) )
  where:
  - H: Cryptographic hash function (SHA-1, block size B = 64 bytes).
  - K^+: Key K zero-padded to B bytes (or hashed if len(K) > B).
  - ipad: Inner pad byte 0x36 repeated B times (64 bytes).
  - opad: Outer pad byte 0x5C repeated B times (64 bytes).
  - ||: Concatenation.
=============================================================================
"""

import hashlib
import hmac
from typing import Tuple

BLOCK_SIZE = 64  # SHA-1 block size B = 64 bytes (512 bits)
IPAD_BYTE = 0x36
OPAD_BYTE = 0x5C

def prepare_key(key: bytes) -> bytes:
    """Pads or hashes key K to exactly B = 64 bytes."""
    if len(key) > BLOCK_SIZE:
        key = hashlib.sha1(key).digest()
    return key.ljust(BLOCK_SIZE, b'\x00')


def hmac_sha1_manual(key: bytes, message: bytes, verbose: bool = True) -> bytes:
    """
    Computes HMAC-SHA1 step-by-step following RFC 2104.
    """
    K_plus = prepare_key(key)
    
    # 1. Compute K^+ ^ ipad and K^+ ^ opad
    k_xor_ipad = bytes([b ^ IPAD_BYTE for b in K_plus])
    k_xor_opad = bytes([b ^ OPAD_BYTE for b in K_plus])

    # 2. Inner hash: H((K^+ ^ ipad) || M)
    inner_input = k_xor_ipad + message
    inner_hash = hashlib.sha1(inner_input).digest()

    # 3. Outer hash: H((K^+ ^ opad) || inner_hash)
    outer_input = k_xor_opad + inner_hash
    mac_tag = hashlib.sha1(outer_input).digest()

    if verbose:
        print(f"\n[+] HMAC-SHA1 Step-by-Step Execution:")
        print(f"    Raw Key ({len(key)} bytes): {key}")
        print(f"    Padded K^+ ({len(K_plus)} bytes): 0x{K_plus.hex()[:32]}...")
        print(f"    K^+ ^ ipad (Hex): 0x{k_xor_ipad.hex()[:32]}...")
        print(f"    K^+ ^ opad (Hex): 0x{k_xor_opad.hex()[:32]}...")
        print(f"    Inner Hash H((K+ ^ ipad) || M): 0x{inner_hash.hex()}")
        print(f"    Outer Hash (Final MAC Tag)    : 0x{mac_tag.hex()}\n")

    return mac_tag


def custom_input():
    print("\n" + "=" * 65)
    print("CUSTOM EXAM INPUT: HMAC-SHA1 AUTHENTICATION CODE")
    print("=" * 65)
    try:
        raw_key = input("Enter secret key [e.g. Jefe]: ").strip()
        k_b = raw_key.encode("utf-8") if raw_key else b"Jefe"
        raw_msg = input("Enter message [e.g. hello world]: ").strip()
        m_b = raw_msg.encode("utf-8") if raw_msg else b"hello world"
        mac = hmac_sha1_manual(k_b, m_b, verbose=True)
        print(f"[=>] Final HMAC-SHA1 Tag: 0x{mac.hex()}")
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}. Using default.")
        try:
            run_demo()
        except Exception:
            pass


def run_demo():
    print("=" * 65)
    print("DEMO: HMAC-SHA1 (RFC 2104 & STUDENT ID 23BA14056)")
    print("=" * 65)

    # 1. RFC 2202 Test Vector 2:
    # Key = "Jefe", Data = "what do ya want for nothing?"
    # Expected: effcdf6ae5eb2fa2d27416d5f184df9c259a7c79
    key_rfc = b"Jefe"
    data_rfc = b"what do ya want for nothing?"
    expected_rfc = "effcdf6ae5eb2fa2d27416d5f184df9c259a7c79"

    print("1. Standard RFC 2202 Test Vector 2:")
    mac_rfc = hmac_sha1_manual(key_rfc, data_rfc, verbose=True)
    print(f"RFC Expected : {expected_rfc}")
    print(f"Computed MAC : {mac_rfc.hex()}")
    print(f"Verification : {mac_rfc.hex() == expected_rfc}")

    # 2. Student ID Authentication Demo:
    print("\n2. Student ID Authentication Demo:")
    student_key = b"Student_Key_23BA14056"
    student_msg = b"Transaction: Transfer 56 USD to USTH Account"
    
    mac_student = hmac_sha1_manual(student_key, student_msg, verbose=False)
    # Verify with standard hmac module
    std_mac = hmac.new(student_key, student_msg, hashlib.sha1).digest()
    print(f"Student Message: '{student_msg.decode()}'")
    print(f"Manual HMAC-SHA1  : 0x{mac_student.hex()}")
    print(f"Standard Library  : 0x{std_mac.hex()}")
    print(f"Verification Match: {mac_student == std_mac}")


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