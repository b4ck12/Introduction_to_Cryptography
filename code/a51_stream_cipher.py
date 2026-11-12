import os
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
    print("=" * 75)
    print("MÃ HÓA DÒNG A5/1 (GSM LFSR STREAM CIPHER) - LỜI GIẢI TỰ LUẬN TỪNG BƯỚC")
    print("=" * 75)
    print(f"[BƯỚC 1] Khởi tạo các thanh ghi LFSR & Cơ chế điều khiển xung nhịp:")
    print(f"    Công thức Majority: maj(x8, y10, z10) = (x&y) | (y&z) | (x&z)")
    print(f"    Công thức sinh bit khóa: s_t = x18 ^ y21 ^ z22")
    print(f"    Tham số: Initial X = {x_dec} (19 bits), Y = {y_dec} (22 bits), Z = {z_dec} (23 bits), Số chu kỳ = {n}")
    print(f"    Trạng thái X: {''.join(map(str, X))} (clock x8={X[8]}, tail x18={X[18]})")
    print(f"    Trạng thái Y: {''.join(map(str, Y))} (clock y10={Y[10]}, tail y21={Y[21]})")
    print(f"    Trạng thái Z: {''.join(map(str, Z))} (clock z10={Z[10]}, tail z22={Z[22]})\n")
    print(f"[BƯỚC 2] Bảng vết chu kỳ xung nhịp A5/1 (Clock Cycles Trace Table):")
    print(f"    {'Cycle':<6} | {'Tail (x18, y21, z22)':<22} | {'Out s_t':<8} | {'Clock (x8,y10,z10)':<19} | {'maj':<4} | {'Stepped':<8}")
    print("    " + "-" * 75)
    
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
            
            print(f"    {t:<6} | {str(cur_tails):<22} | {s_t:<8} | ({c_x}, {c_y}, {c_z}){'':<7} | {m:<4} | {','.join(stepped):<8}")
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
            print(f"    {t:<6} | {str(cur_tails):<22} | {s_t:<8} | ({c_x}, {c_y}, {c_z}){'':<7} | {m:<4} | {','.join(stepped):<8}")

    print("    " + "-" * 75)
    ks_str = "".join(map(str, keystream))
    print(f"\n[BƯỚC 3] Kết luận chuỗi dòng khóa sinh ra:")
    print(f"    Dòng khóa nhị phân (Binary): {ks_str}")
    print(f"    ===> DÒNG KHÓA A5/1: {ks_str}")
    print("=" * 75)
    return keystream
            
    ks_str = "".join(map(str, keystream))
    print("-" * 75)
    print(f"Resulting {n}-bit Keystream: {keystream}")
    print(f"Binary String Representation: {ks_str}")
    print("=" * 75 + "\n")
    return keystream, ks_str

def custom_input():
    import os, sys
    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
        return
    print("\n" + "=" * 75)
    print("CUSTOM EXAM INPUT: A5/1 STREAM CIPHER")
    print("=" * 75)
    try:
        val_n = input("Enter number of keystream bits to generate [default 10]: ").strip()
        n = int(val_n, 0) if val_n else 10
        print("Choose clocking convention:")
        print("  [1] Option 1 (USTH Official Exam Standard: Output at t=0 before shift)")
        print("  [2] Option 2 (Textbook Shift-First: Clock active registers, then output)")
        opt = input("Select convention [1/2, default 1]: ").strip()
        out_first = (opt != "2")

        custom_regs = input("Use custom initial register states? [y/N]: ").strip().lower()
        if custom_regs in ("y", "yes"):
            raw_x = input("Enter 19-bit state for X [e.g. 1010101010101010101]: ").strip()
            raw_y = input("Enter 22-bit state for Y [e.g. 1100110011001100110011]: ").strip()
            raw_z = input("Enter 23-bit state for Z [e.g. 11100011100011100011100]: ").strip()
            x = [int(b) for b in raw_x] if len(raw_x) == 19 else None
            y = [int(b) for b in raw_y] if len(raw_y) == 22 else None
            z = [int(b) for b in raw_z] if len(raw_z) == 23 else None
            run_a51(x, y, z, n=n, output_first=out_first)
        else:
            run_a51(n=n, output_first=out_first)
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}. Using default.")
        try:
            run_demo()
        except Exception:
            pass


def run_demo():
    print("=== OFFICIAL USTH RESULT (Option 1) ===")
    run_a51(output_first=True)
    
    print("=== TEXTBOOK RESULT (Option 2) ===")
    run_a51(output_first=False)


if __name__ == "__main__":
    import sys

    # Run demo test suite only if explicitly requested or in non-interactive test pipe
    if "--demo" in sys.argv or (not sys.stdin.isatty() and len(sys.argv) <= 1):
        run_demo()
        sys.exit(0)

    # Support CLI arguments: python a51_stream_cipher.py 0x12345 0x234567 0x345678 16
    cli_args = [a for a in sys.argv[1:] if a.strip() and not a.startswith("-")]
    if len(cli_args) >= 3:
        try:
            r1_arg = int(cli_args[0], 0)
            r2_arg = int(cli_args[1], 0)
            r3_arg = int(cli_args[2], 0)
            steps_arg = int(cli_args[3], 0) if len(cli_args) > 3 else 16
            simulate_a51(r1_arg, r2_arg, r3_arg, n=steps_arg, output_first=True, convention_name="CLI Custom Input")
            sys.exit(0)
        except Exception:
            pass

    # Default: Open directly into Custom Exam Input prompt
    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
    else:
        try:
            custom_input()
        except (EOFError, KeyboardInterrupt):
            run_demo()