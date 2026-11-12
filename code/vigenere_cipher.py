"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Algorithm: Vigenère Cipher (Polyalphabetic Stream/Block Shift)
Reference: Session 2 (Classical Cryptosystems)
Student ID: 23BA14056 (x = 56)
=============================================================================
Theory:
  - Key: A keyword of length m, K = (k_0, k_1, ..., k_{m-1}).
  - Encryption:
      c_i = (m_i + k_{i mod m}) mod 26
  - Decryption:
      m_i = (c_i - k_{i mod m}) mod 26
  - Smooths letter frequency distribution compared to Caesar/monoalphabetic.
=============================================================================
"""

def vigenere_encrypt(plaintext: str, key: str, verbose: bool = True) -> str:
    """Encrypts plaintext with repeating Vigenère keyword."""
    clean_text = [c.upper() for c in plaintext if c.isalpha()]
    clean_key = [c.upper() for c in key if c.isalpha()]
    if not clean_key:
        raise ValueError("Key must contain at least one alphabetic character.")

    m = len(clean_key)
    ciphertext = []

    if verbose:
        print(f"\n[+] Vigenère Encryption Trace (Key = '{''.join(clean_key)}'):")
        print(f"{'Idx':<4} | {'Plain':<6} | {'Key':<5} | {'m_i':<4} | {'k_i':<4} | {'(m_i + k_i) mod 26':<20} | {'Cipher':<6}")
        print("-" * 65)

    for i, p_char in enumerate(clean_text):
        k_char = clean_key[i % m]
        m_val = ord(p_char) - ord('A')
        k_val = ord(k_char) - ord('A')
        c_val = (m_val + k_val) % 26
        c_char = chr(c_val + ord('A'))
        ciphertext.append(c_char)
        if verbose:
            calc = f"({m_val:>2} + {k_val:>2}) % 26 = {c_val:>2}"
            print(f"{i:<4} | {p_char:<6} | {k_char:<5} | {m_val:<4} | {k_val:<4} | {calc:<20} | {c_char:<6}")

    if verbose:
        print("-" * 65)

    return "".join(ciphertext)


def vigenere_decrypt(ciphertext: str, key: str, verbose: bool = True) -> str:
    """Decrypts ciphertext with repeating Vigenère keyword."""
    clean_cipher = [c.upper() for c in ciphertext if c.isalpha()]
    clean_key = [c.upper() for c in key if c.isalpha()]
    m = len(clean_key)
    plaintext = []

    if verbose:
        print(f"\n[+] Vigenère Decryption Trace (Key = '{''.join(clean_key)}'):")
        print(f"{'Idx':<4} | {'Cipher':<6} | {'Key':<5} | {'c_i':<4} | {'k_i':<4} | {'(c_i - k_i) mod 26':<20} | {'Plain':<6}")
        print("-" * 65)

    for i, c_char in enumerate(clean_cipher):
        k_char = clean_key[i % m]
        c_val = ord(c_char) - ord('A')
        k_val = ord(k_char) - ord('A')
        p_val = (c_val - k_val) % 26
        p_char = chr(p_val + ord('A'))
        plaintext.append(p_char)
        if verbose:
            calc = f"({c_val:>2} - {k_val:>2}) % 26 = {p_val:>2}"
            print(f"{i:<4} | {c_char:<6} | {k_char:<5} | {c_val:<4} | {k_val:<4} | {calc:<20} | {p_char:<6}")

    if verbose:
        print("-" * 65)

    return "".join(plaintext)


def custom_input():
    print("\n" + "=" * 65)
    print("CUSTOM EXAM INPUT: VIGENÈRE CIPHER CALCULATOR")
    print("=" * 65)
    print("Choose operation:")
    print("  [1] Encrypt text with keyword")
    print("  [2] Decrypt text with keyword")
    try:
        op = input("Select [1/2, default 1]: ").strip()
        txt = input("Enter text string [e.g. USTHCRYPTO]: ").strip()
        if not txt:
            txt = "USTHCRYPTO"
        kw = input("Enter keyword [e.g. KEY]: ").strip()
        if not kw:
            kw = "KEY"
        if op == "2":
            res = vigenere_decrypt(txt, kw, verbose=True)
            print(f"\n[=>] Decrypted text with keyword '{kw}': '{res}'")
        else:
            res = vigenere_encrypt(txt, kw, verbose=True)
            print(f"\n[=>] Encrypted ciphertext with keyword '{kw}': '{res}'")
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}")


def run_demo():
    print("=" * 65)
    print("DEMO: VIGENÈRE CIPHER (POLYALPHABETIC)")
    print("=" * 65)

    message = "USTHCRYPTO"
    keyword = "KEY"

    print(f"Original Text: {message}")
    print(f"Keyword      : {keyword}")

    cipher = vigenere_encrypt(message, keyword, verbose=True)
    print(f"[=>] Full Ciphertext: {cipher}")

    recovered = vigenere_decrypt(cipher, keyword, verbose=True)
    print(f"[=>] Full Recovered Plaintext: {recovered}")
    print(f"[=>] Verification Match: {recovered == message}")


if __name__ == "__main__":
    import sys

    # Run demo test suite only if explicitly requested or in non-interactive test pipe
    if "--demo" in sys.argv or (not sys.stdin.isatty() and len(sys.argv) <= 1):
        run_demo()
        sys.exit(0)

    # Support CLI arguments: python vigenere_cipher.py "USTH" "KEY"
    if len(sys.argv) > 1 and not sys.argv[1].startswith("-"):
        txt = sys.argv[1]
        kw = sys.argv[2] if len(sys.argv) > 2 else "KEY"
        print(f"Encrypted: {vigenere_encrypt(txt, kw, verbose=False)}")
        sys.exit(0)

    # Default: Open directly into Custom Exam Input prompt
    if sys.stdin.isatty():
        custom_input()
    else:
        run_demo()