import os
"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Algorithm: RC4 Stream Cipher (KSA & PRGA)
Reference: Session 3 (Stream Ciphers)
Student ID: 23BA14056 (x = 56)
=============================================================================
Theory:
  RC4 is a byte-oriented stream cipher with variable key length (1 to 256 bytes).
  1. Key-Scheduling Algorithm (KSA):
     - Initialize state array S = [0, 1, ..., 255]
     - Permute S according to key K:
         j = 0
         For i = 0 to 255:
             j = (j + S[i] + K[i mod key_len]) mod 256
             Swap(S[i], S[j])
  2. Pseudo-Random Generation Algorithm (PRGA):
     - Generate keystream byte-by-byte:
         i = (i + 1) mod 256
         j = (j + S[i]) mod 256
         Swap(S[i], S[j])
         t = (S[i] + S[j]) mod 256
         keystream_byte = S[t]
=============================================================================
"""

from typing import List, Generator

class RC4:
    def __init__(self, key: bytes):
        """Initializes RC4 cipher and runs the Key-Scheduling Algorithm (KSA)."""
        self.key = key
        self.S = list(range(256))
        self._ksa()

    def _ksa(self) -> None:
        """Key-Scheduling Algorithm (KSA)."""
        j = 0
        key_len = len(self.key)
        for i in range(256):
            j = (j + self.S[i] + self.key[i % key_len]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]

    def prga_generator(self) -> Generator[int, None, None]:
        """Pseudo-Random Generation Algorithm (PRGA) byte generator."""
        i = 0
        j = 0
        # Copy state for generation
        S = list(self.S)
        while True:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            t = (S[i] + S[j]) % 256
            yield S[t]

    def crypt(self, data: bytes) -> bytes:
        """Encrypts or decrypts bytes (symmetric XOR operation)."""
        gen = self.prga_generator()
        return bytes([b ^ next(gen) for b in data])


def custom_input():
    import os, sys
    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
        return
    print("\n" + "=" * 65)
    print("CUSTOM EXAM INPUT: RC4 STREAM CIPHER")
    print("=" * 65)
    try:
        raw_key = input("Enter key string [e.g. SECRET]: ").strip()
        key_bytes = raw_key.encode("utf-8") if raw_key else b"SECRET"
        val_n = input("Enter number of keystream bytes to generate [default 8]: ").strip()
        n = int(val_n, 0) if val_n else 8
        rc4 = RC4(key_bytes)
        gen = rc4.prga_generator()
        ks = [next(gen) for _ in range(n)]
        print(f"\n[+] Key: {key_bytes}")
        print(f"[+] Keystream ({n} bytes):")
        print(f"    Decimal: {ks}")
        print(f"    Hex    : {[f'0x{b:02X}' for b in ks]}")

        raw_msg = input("\nEnter message to encrypt/decrypt (or press Enter to skip): ").strip()
        if raw_msg:
            msg_b = raw_msg.encode("utf-8")
            c = RC4(key_bytes).crypt(msg_b)
            print(f"[+] Ciphertext (Hex): {c.hex()}")
            p = RC4(key_bytes).crypt(c)
            print(f"[+] Decrypted text  : {p.decode(errors='replace')}")
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}. Using default.")
        try:
            run_demo()
        except Exception:
            pass


def run_demo():
    print("=" * 65)
    print("DEMO: RC4 STREAM CIPHER (KSA & PRGA)")
    print("=" * 65)

    # Key setup
    key = b"USTH_CRYPTO_KEY"
    print(f"Key: {key.decode()} (Hex: {key.hex()})")

    cipher_rc4 = RC4(key)
    
    # Generate first 10 keystream bytes
    gen = cipher_rc4.prga_generator()
    first_10_bytes = [next(gen) for _ in range(10)]
    print("\n[+] First 10 Generated Keystream Bytes:")
    print(f"    Decimal: {first_10_bytes}")
    print(f"    Hex    : {[hex(b) for b in first_10_bytes]}")

    # Encryption demo
    message = b"Secret Message for ID 23BA14056"
    print(f"\n[+] Plaintext: {message.decode()}")
    
    # Fresh instance for encryption
    ciphertext = RC4(key).crypt(message)
    print(f"[+] Ciphertext (Hex): {ciphertext.hex()}")

    # Decryption demo (using identical key)
    decrypted = RC4(key).crypt(ciphertext)
    print(f"[+] Decrypted: {decrypted.decode()}")
    print(f"[+] Verification Match: {decrypted == message}")


def solve_rc4_detailed(key_str: str, n_bytes: int = 8):
    key_bytes = key_str.encode('utf-8')
    rc4 = RC4(key_bytes)
    print("=" * 75)
    print("MÃ HÓA DÒNG RC4 (RC4 STREAM CIPHER) - LỜI GIẢI TỰ LUẬN TỪNG BƯỚC")
    print("=" * 75)
    print(f"[BƯỚC 1] Khởi tạo mảng trạng thái S và Thuật toán sinh khóa KSA:")
    print(f"    Công thức KSA: j = (j + S[i] + K[i mod key_len]) mod 256; swap(S[i], S[j])")
    print(f"    Công thức PRGA: i = (i+1) mod 256, j = (j+S[i]) mod 256, t = (S[i]+S[j]) mod 256, k = S[t]")
    print(f"    Tham số: Key = '{key_str}', Key bytes = {[b for b in key_bytes]}, Số byte dòng khóa = {n_bytes}\n")

    print(f"[BƯỚC 2] Bảng vết sinh dòng khóa PRGA (Pseudo-Random Generation Algorithm):")
    print(f"    {'Byte':<5} | {'i = (i+1) mod 256':<18} | {'j = (j+S[i]) mod 256':<20} | {'t = (S[i]+S[j]) mod 256':<22} | {'Keystream Byte'}")
    print("    " + "-" * 75)

    S = list(rc4.S)
    i = 0
    j = 0
    keystream = []
    for step in range(1, n_bytes + 1):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        k_byte = S[t]
        keystream.append(k_byte)
        print(f"    {step:<5} | i = {i:<14} | j = {j:<16} | t = {t:<18} | 0x{k_byte:02X} ({k_byte})")

    print("    " + "-" * 75)
    hex_str = " ".join(f"{b:02X}" for b in keystream)
    print(f"\n[BƯỚC 3] Kết luận dòng khóa keystream sinh ra:")
    print(f"    Dòng khóa (Hex)     : {hex_str}")
    print(f"    Dòng khóa (Decimals): {[b for b in keystream]}")
    print(f"    ===> DÒNG KHÓA RC4: {hex_str}")
    print("=" * 75)


if __name__ == "__main__":
    import sys

    # Run demo test suite only if explicitly requested or in non-interactive test pipe
    if "--demo" in sys.argv or (not sys.stdin.isatty() and len(sys.argv) <= 1):
        run_demo()
        sys.exit(0)

    # Support CLI arguments: python rc4_stream_cipher.py "USTH" 8
    cli_args = [a for a in sys.argv[1:] if a.strip() and not a.startswith("-")]
    if len(cli_args) >= 1:
        key_arg = cli_args[0]
        n_arg = int(cli_args[1], 0) if len(cli_args) > 1 else 8
        solve_rc4_detailed(key_arg, n_arg)
        sys.exit(0)

    # Default: Open directly into Custom Exam Input prompt
    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
    else:
        try:
            custom_input()
        except (EOFError, KeyboardInterrupt):
            run_demo()