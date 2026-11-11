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
        print(f"[-] Input error or cancelled: {err}")


if __name__ == "__main__":
    import sys

    # Direct interactive flag: python rc4_stream_cipher.py -i
    if len(sys.argv) > 1 and sys.argv[1] in ("-i", "--interactive", "--custom"):
        custom_input()
        sys.exit(0)

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

    # Interactive prompt if user runs directly in terminal
    if sys.stdin.isatty():
        print("-" * 65)
        c = input("[?] Enter custom key/message for your exam? [y/N]: ").strip().lower()
        if c in ("y", "yes"):
            custom_input()

