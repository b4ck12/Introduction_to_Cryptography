import os
"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Algorithm: Caesar Cipher (Shift Cipher) & Brute-Force Cryptanalysis
Reference: Session 2 (Classical Cryptosystems)
Student ID: 23BA14056 (x = 56 ==> Shift k = 56 mod 26 = 4)
=============================================================================
Theory:
  Let alphabet be Z_26 = {0, 1, ..., 25} (A=0, B=1, ..., Z=25).
  - Key: k in {0, 1, ..., 25}
  - Encryption:  e_k(m) = (m + k) mod 26
  - Decryption:  d_k(c) = (c - k) mod 26
  - Security: Key space size is only 26, completely vulnerable to brute-force!
=============================================================================
"""

from typing import List, Tuple

def caesar_encrypt(plaintext: str, key: int) -> str:
    """Encrypts plaintext with Caesar shift key."""
    ciphertext = []
    k = key % 26
    for char in plaintext:
        if char.isupper():
            c = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            ciphertext.append(c)
        elif char.islower():
            c = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            ciphertext.append(c)
        else:
            ciphertext.append(char)
    return "".join(ciphertext)


def caesar_decrypt(ciphertext: str, key: int) -> str:
    """Decrypts ciphertext with Caesar shift key."""
    return caesar_encrypt(ciphertext, -key)


def caesar_brute_force(ciphertext: str) -> List[Tuple[int, str]]:
    """Tries all 26 possible shift keys and returns candidates."""
    candidates = []
    for k in range(26):
        decrypted = caesar_decrypt(ciphertext, k)
        candidates.append((k, decrypted))
    return candidates


def custom_input():
    print("\n" + "=" * 65)
    print("CUSTOM EXAM INPUT: CAESAR CIPHER CALCULATOR")
    print("=" * 65)
    print("Choose operation:")
    print("  [1] Encrypt text with key k")
    print("  [2] Decrypt text with key k")
    print("  [3] Brute-force Attack (Try all 26 keys on ciphertext)")
    try:
        op = input("Select [1/2/3, default 1]: ").strip()
        txt = input("Enter text string [e.g. HELLO USTH]: ").strip()
        if not txt:
            txt = "HELLO USTH"
        if op == "3":
            print(f"\n[+] Brute-force decryption of '{txt}':")
            print(f"{'Key k':<6} | {'Candidate Plaintext'}")
            print("-" * 45)
            for k, cand in caesar_brute_force(txt):
                print(f"k = {k:<2}  | {cand}")
        elif op == "2":
            val_k = input("Enter shift key k [0-25, default 3]: ").strip()
            k = int(val_k, 0) if val_k else 3
            res = caesar_decrypt(txt, k)
            print(f"\n[=>] Decrypted text (k={k}): '{res}'")
        else:
            val_k = input("Enter shift key k [0-25, default 3]: ").strip()
            k = int(val_k, 0) if val_k else 3
            res = caesar_encrypt(txt, k)
            print(f"\n[=>] Encrypted ciphertext (k={k}): '{res}'")
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}. Using default.")
        try:
            run_demo()
        except Exception:
            pass


def run_demo():
    print("=" * 65)
    print("DEMO: CAESAR CIPHER (ENCRYPTION, DECRYPTION, BRUTE-FORCE)")
    print("=" * 65)

    msg = "CRYPTOGRAPHY IS FUN"
    # Using Student ID: 56 mod 26 = 4 (or k = 3 classic Caesar)
    student_id = 56
    key = student_id % 26
    print(f"Plaintext: '{msg}'")
    print(f"Student ID = {student_id} ==> Effective Key k = {student_id} mod 26 = {key}\n")

    # Encryption
    cipher = caesar_encrypt(msg, key)
    print(f"[+] Encrypted Ciphertext: '{cipher}'")

    # Decryption
    decrypted = caesar_decrypt(cipher, key)
    print(f"[+] Decrypted Plaintext : '{decrypted}'")
    print(f"[+] Matches Original: {decrypted == msg}\n")

    # 2. Session 2 Slide 15 Example:
    print("-" * 65)
    print("2. Session 2 Slide 15 Example: Determine Shift Rule:")
    p_slide = "ictlab"
    c_slide = "lfwode"
    shift_rule = (ord(c_slide[0]) - ord(p_slide[0])) % 26
    print(f"   Plaintext : '{p_slide}'")
    print(f"   Ciphertext: '{c_slide}'")
    print(f"   Analysis  : '{p_slide[0]}' ({ord(p_slide[0]) - ord('a')}) -> '{c_slide[0]}' ({ord(c_slide[0]) - ord('a')})")
    print(f"   [=>] Detected Rule: Caesar shift key k = {shift_rule}")
    print(f"   Verification: caesar_encrypt('{p_slide}', {shift_rule}) = '{caesar_encrypt(p_slide, shift_rule)}' (Match: {caesar_encrypt(p_slide, shift_rule) == c_slide})")
    print("-" * 65)

    # Brute-force cryptanalysis
    print("\n3. Brute-force Attack on Student ID Ciphertext (All 26 possible keys):")
    print(f"{'Key k':<6} | {'Decrypted Candidate Plaintext'}")
    print("-" * 45)
    candidates = caesar_brute_force(cipher)
    for k, text in candidates:
        flag = " <== CORRECT KEY" if k == key else ""
        print(f"k = {k:<2}  | {text}{flag}")


if __name__ == "__main__":
    import sys

    # Run demo test suite only if explicitly requested or in non-interactive test pipe
    if "--demo" in sys.argv or (not sys.stdin.isatty() and len(sys.argv) <= 1):
        run_demo()
        sys.exit(0)

    # Support CLI arguments: python caesar_cipher.py "HELLO" 3
    if len(sys.argv) > 1 and not sys.argv[1].startswith("-"):
        txt = sys.argv[1]
        k = int(sys.argv[2], 0) if len(sys.argv) > 2 else 3
        print(f"Encrypted: {caesar_encrypt(txt, k)}")
        sys.exit(0)

    # Default: Open directly into Custom Exam Input prompt
    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
    else:
        try:
            custom_input()
        except (EOFError, KeyboardInterrupt):
            run_demo()