# -*- coding: utf-8 -*-
"""
Script: a51_stream_cipher.py
Description: Implementation of GSM A5/1 Stream Cipher Keystream Generator (Lab 1 Exercise 4).
Supports both standard hardware clocking conventions:
  - Option 1 (Standard USTH / Hardware Output-First): S = (0, 1, 0, 0, 0, 0, 0, 0, 0, 1)_2
  - Option 2 (Shift-First / Textbook Convention):      S = (1, 0, 0, 0, 0, 0, 0, 0, 1, 0)_2
"""

def int_to_bits(val, length):
    return [(val >> (length - 1 - i)) & 1 for i in range(length)]

def maj(x, y, z):
    return (x & y) | (y & z) | (x & z)

def run_a51(x_dec=513365, y_dec=3355443, z_dec=7401712, n=10, output_first=True):
    X = int_to_bits(x_dec, 19)
    Y = int_to_bits(y_dec, 22)
    Z = int_to_bits(z_dec, 23)
    
    convention_name = "Output First, Then Step (Standard USTH Hardware Convention)" if output_first else "Step First, Then Output (Textbook Convention)"
    print("=" * 75)
    print("A5/1 STREAM CIPHER KEY GENERATION (LAB 1 - EXERCISE 4)")
    print(f"Convention: {convention_name}")
    print("=" * 75)
    print(f"Initial X (19 bits): {x_dec} -> {''.join(map(str, X))} (clock x8={X[8]}, tail x18={X[18]})")
    print(f"Initial Y (22 bits): {y_dec} -> {''.join(map(str, Y))} (clock y10={Y[10]}, tail y21={Y[21]})")
    print(f"Initial Z (23 bits): {z_dec} -> {''.join(map(str, Z))} (clock z10={Z[10]}, tail z22={Z[22]})")
    print("\n" + "-" * 75)
    print(f"{'Cycle':<6} | {'Tail (x18, y21, z22)':<22} | {'Out s_t':<8} | {'Clock (x8,y10,z10)':<19} | {'maj':<4} | {'Stepped':<8}")
    print("-" * 75)
    
    keystream = []
    for t in range(1, n + 1):
        if output_first:
            # 1. Output bit generated from CURRENT register tails
            cur_tails = (X[18], Y[21], Z[22])
            s_t = X[18] ^ Y[21] ^ Z[22]
            keystream.append(s_t)
            
            # 2. Clock decision from current clock taps
            c_x, c_y, c_z = X[8], Y[10], Z[10]
            m = maj(c_x, c_y, c_z)
            
            # Feedback bits
            fb_x = X[13] ^ X[16] ^ X[17] ^ X[18]
            fb_y = Y[20] ^ Y[21]
            fb_z = Z[7] ^ Z[20] ^ Z[21] ^ Z[22]
            
            stepped = []
            if c_x == m: X = [fb_x] + X[:-1]; stepped.append('X')
            if c_y == m: Y = [fb_y] + Y[:-1]; stepped.append('Y')
            if c_z == m: Z = [fb_z] + Z[:-1]; stepped.append('Z')
            
            print(f"{t:<6} | {str(cur_tails):<22} | {s_t:<8} | ({c_x}, {c_y}, {c_z}){'':<7} | {m:<4} | {','.join(stepped):<8}")
        else:
            c_x, c_y, c_z = X[8], Y[10], Z[10]
            m = maj(c_x, c_y, c_z)
            fb_x = X[13] ^ X[16] ^ X[17] ^ X[18]
            fb_y = Y[20] ^ Y[21]
            fb_z = Z[7] ^ Z[20] ^ Z[21] ^ Z[22]
            stepped = []
            if c_x == m: X = [fb_x] + X[:-1]; stepped.append('X')
            if c_y == m: Y = [fb_y] + Y[:-1]; stepped.append('Y')
            if c_z == m: Z = [fb_z] + Z[:-1]; stepped.append('Z')
            cur_tails = (X[18], Y[21], Z[22])
            s_t = X[18] ^ Y[21] ^ Z[22]
            keystream.append(s_t)
            print(f"{t:<6} | {str(cur_tails):<22} | {s_t:<8} | ({c_x}, {c_y}, {c_z}){'':<7} | {m:<4} | {','.join(stepped):<8}")
            
    ks_str = "".join(map(str, keystream))
    print("-" * 75)
    print(f"Resulting {n}-bit Keystream: {keystream}")
    print(f"Binary String Representation: {ks_str}")
    print("=" * 75 + "\n")
    return keystream, ks_str

if __name__ == "__main__":
    print("=== OFFICIAL USTH RESULT (Option 1) ===")
    run_a51(output_first=True)
    
    print("=== TEXTBOOK RESULT (Option 2) ===")
    run_a51(output_first=False)
