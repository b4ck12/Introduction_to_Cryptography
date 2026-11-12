import os
"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Algorithm: SHA-1 Full Compression Function & Message Expansion
Reference: Session 7 (Hash Functions & Digital Signatures, Slides 23-26)
Student ID: 23BA14056 (x = 56)
=============================================================================
Theory:
  SHA-1 processes 512-bit message blocks (16 words of 32 bits each).
  1. Message Expansion:
     - W_0 .. W_{15} are the 16 words from the block.
     - For t = 16 to 79:
         W_t = (W_{t-3} ^ W_{t-8} ^ W_{t-14} ^ W_{t-16}) <<< 1
  2. Four 20-round stages (80 rounds total) using:
     - Non-linear logical functions f_t(B, C, D)
     - Additive constants K_t
     - Round update:
         TEMP = (A <<< 5) + f_t(B, C, D) + E + W_t + K_t mod 2^32
         E = D; D = C; C = B <<< 30; B = A; A = TEMP
=============================================================================
"""

import struct
from typing import List, Tuple

def rol(value: int, shift: int, bits: int = 32) -> int:
    """Circular left shift (rotate left)."""
    mask = (1 << bits) - 1
    shift %= bits
    return ((value << shift) & mask) | ((value & mask) >> (bits - shift))


class SHA1Compressor:
    # Standard SHA-1 Initial Hash Values (IV)
    IV = [
        0x67452301,
        0xEFCDAB89,
        0x98BADCFE,
        0x10325476,
        0xC3D2E1F0
    ]

    # Additive constants for the 4 stages
    K = [
        0x5A827999,  # 0 <= t <= 19
        0x6ED9EBA1,  # 20 <= t <= 39
        0x8F1BBCDC,  # 40 <= t <= 59
        0xCA62C1D6   # 60 <= t <= 79
    ]

    @staticmethod
    def expand_block(block_512: bytes) -> List[int]:
        """Expands a 64-byte (512-bit) block into 80 32-bit words."""
        # Unpack first 16 words (Big-Endian)
        W = list(struct.unpack(">16I", block_512))
        for t in range(16, 80):
            val = W[t - 3] ^ W[t - 8] ^ W[t - 14] ^ W[t - 16]
            W.append(rol(val, 1))
        return W

    @staticmethod
    def f_round(t: int, B: int, C: int, D: int) -> Tuple[int, int]:
        """Returns (f_t(B, C, D), K_t) for round t."""
        mask = 0xFFFFFFFF
        if 0 <= t <= 19:
            # Ch(B, C, D) = (B and C) or (not B and D)
            f = (B & C) | (~B & D)
            k = SHA1Compressor.K[0]
        elif 20 <= t <= 39:
            # Parity(B, C, D) = B ^ C ^ D
            f = B ^ C ^ D
            k = SHA1Compressor.K[1]
        elif 40 <= t <= 59:
            # Maj(B, C, D) = (B and C) or (B and D) or (C and D)
            f = (B & C) | (B & D) | (C & D)
            k = SHA1Compressor.K[2]
        else:
            # Parity(B, C, D) = B ^ C ^ D
            f = B ^ C ^ D
            k = SHA1Compressor.K[3]
        return f & mask, k

    @classmethod
    def compress(cls, state: List[int], block_512: bytes, verbose: bool = True) -> List[int]:
        """Runs the 80-round compression function on a single 512-bit block."""
        W = cls.expand_block(block_512)
        A, B, C, D, E = state
        mask = 0xFFFFFFFF

        if verbose:
            print("\n[+] SHA-1 Compression Round Execution:")
            print(f"    Initial State: A={A:08X}, B={B:08X}, C={C:08X}, D={D:08X}, E={E:08X}")
            print(f"{'Rnd':<4} | {'W_t (Hex)':<10} | {'K_t (Hex)':<10} | {'A':<8} | {'B':<8} | {'C':<8} | {'D':<8} | {'E':<8}")
            print("-" * 75)

        for t in range(80):
            f, k = cls.f_round(t, B, C, D)
            temp = (rol(A, 5) + f + E + k + W[t]) & mask
            E = D
            D = C
            C = rol(B, 30)
            B = A
            A = temp

            if verbose and (t < 5 or t >= 75):
                print(f"{t:<4} | {W[t]:08X}{'':<2} | {k:08X}{'':<2} | {A:08X} | {B:08X} | {C:08X} | {D:08X} | {E:08X}")
            elif verbose and t == 5:
                print(f"{'...':<4} | {'...':<10} | {'...':<10} | (Intermediate rounds 5-74 omitted) ...")

        # Davis-Meyer feed-forward addition
        new_state = [
            (state[0] + A) & mask,
            (state[1] + B) & mask,
            (state[2] + C) & mask,
            (state[3] + D) & mask,
            (state[4] + E) & mask,
        ]

        if verbose:
            print("-" * 75)
            print(f"[=>] Updated State (H + Round_Output):")
            for idx, h in enumerate(new_state):
                print(f"     H_{idx} = 0x{h:08X}")
            digest = "".join(f"{h:08x}" for h in new_state)
            print(f"[=>] Resulting 160-bit Digest: {digest}\n")

        return new_state


def custom_input():
    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
        return
    print("\n" + "=" * 70)
    print("CUSTOM EXAM INPUT: SHA-1 COMPRESSION & HASH")
    print("=" * 70)
    try:
        raw_msg = input("Enter message string to hash [e.g. abc]: ").strip()
        msg_bytes = raw_msg.encode("utf-8") if raw_msg else b"abc"
        # Standard SHA-1 pad
        l_bits = len(msg_bytes) * 8
        rem = l_bits % 512
        k_zeros = (447 - rem) % 512
        pad = b"\x80" + b"\x00" * (k_zeros // 8) + l_bits.to_bytes(8, 'big')
        padded_msg = msg_bytes + pad
        print(f"\n[+] Total padded length: {len(padded_msg)} bytes ({len(padded_msg)*8} bits = {len(padded_msg)//64} blocks)")
        
        state = list(SHA1Compressor.IV)
        for blk_idx in range(len(padded_msg) // 64):
            blk = padded_msg[blk_idx*64 : (blk_idx+1)*64]
            print(f"\n--- Compressing Block {blk_idx+1}/{len(padded_msg)//64} ---")
            state = SHA1Compressor.compress(state, blk, verbose=True)

        final_hex = "".join(f"{h:08x}" for h in state)
        print(f"[=>] Final SHA-1 Digest: {final_hex}")
    except (ValueError, KeyboardInterrupt, EOFError):
        run_demo()


def run_demo():
    # Standard run:
    # Example 512-bit block containing ASCII for 'abc' with SHA-1 padding
    msg_abc = b"abc" + b"\x80" + b"\x00" * 52 + (24).to_bytes(8, 'big')
    print("=" * 70)
    print("DEMO: SHA-1 COMPRESSION FUNCTION & MESSAGE EXPANSION")
    print("=" * 70)
    print(f"Testing 512-bit padded block for 'abc' ({len(msg_abc)} bytes):")

    init_state = list(SHA1Compressor.IV)
    out_state = SHA1Compressor.compress(init_state, msg_abc, verbose=True)

    expected_sha1_abc = "a9993e364706816aba3e25717850c26c9cd0d89d"
    actual_hash = "".join(f"{h:08x}" for h in out_state)
    print(f"Expected SHA-1('abc'): {expected_sha1_abc}")
    print(f"Calculated Hash     : {actual_hash}")
    print(f"Verification Match  : {actual_hash == expected_sha1_abc}")

    # Session 7 Slide 25 Exercise:
    print("\n" + "=" * 70)
    print("SESSION 7 SLIDE 25 - FIRST ROUND OUTPUT EXERCISE")
    print("=" * 70)
    print("Conditions: A_0 = B_0 = C_0 = D_0 = E_0 = 0x00000000, Stage 1 (K_0 = 0x5A827999)")
    print("Round formula: T = (A_0 <<< 5) + f_0(B_0, C_0, D_0) + E_0 + K_0 + W_0 mod 2^32")
    print("               f_0(0, 0, 0) = (0 & 0) | (~0 & 0) = 0")
    print("               (A_0 <<< 5) = 0, E_0 = 0 ==> T = K_0 + W_0 = 0x5A827999 + W_0")
    
    blk1 = bytes(64)
    w1 = SHA1Compressor.expand_block(blk1)
    t1 = (0x5A827999 + w1[0]) & 0xFFFFFFFF
    print(f"\n1. For x = 0...00:")
    print(f"   First 32-bit word W_0 = 0x{w1[0]:08X}")
    print(f"   T = 0x5A827999 + 0x{w1[0]:08X} = 0x{t1:08X}")
    print(f"   First round output: A_1 = 0x{t1:08X}, B_1 = 0, C_1 = 0, D_1 = 0, E_1 = 0")

    blk2 = bytearray(64)
    blk2[-1] = 0x01
    w2 = SHA1Compressor.expand_block(bytes(blk2))
    t2 = (0x5A827999 + w2[0]) & 0xFFFFFFFF
    print(f"\n2. For x = 0...01 (bit 512 is one):")
    print(f"   Bit 512 resides in word W_15 (0x{w2[15]:08X}), so first word W_0 = 0x{w2[0]:08X}")
    print(f"   T = 0x5A827999 + 0x{w2[0]:08X} = 0x{t2:08X}")
    print(f"   First round output: A_1 = 0x{t2:08X}, B_1 = 0, C_1 = 0, D_1 = 0, E_1 = 0")
    print(f"   [=>] Conclusion: Both inputs produce IDENTICAL output (0x5A827999, 0, 0, 0, 0) after Round 1!")
    print("=" * 70)


if __name__ == "__main__":
    import os
    import sys

    if "--demo" in sys.argv:
        run_demo()
        sys.exit(0)

    cli_args = [a for a in sys.argv[1:] if a.strip() and not a.startswith("-")]
    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty() or len(cli_args) > 0:
        run_demo()
        sys.exit(0)

    custom_input()