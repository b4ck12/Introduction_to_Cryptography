# -*- coding: utf-8 -*-
"""
Script: solve_sha1_padding.py
Description: Solves Exercise 3 (SHA-1 Message Preprocessing & Padding).
Analyzes both l = 20260 bits (Printed on exam sheet) and l = 56 bits (Student ID).
"""

def solve_sha1_padding_for_len(l_bits, label=""):
    print(f"\n" + "=" * 75)
    print(f"{label} - LỜI GIẢI TỰ LUẬN TỪNG BƯỚC (l = {l_bits} bits)")
    print("=" * 75)
    rem = l_bits % 512
    # Formula: (l + 1 + k) = 448 mod 512
    # k = (447 - (l mod 512)) mod 512
    k_zeros = (447 - rem) % 512
    
    # 64-bit Big-Endian binary representation of original length l
    length_bin_64 = f"{l_bits:064b}"
    length_hex_64 = f"0x{l_bits:016X}"
    
    total_len = l_bits + 1 + k_zeros + 64
    total_blocks = total_len // 512
    
    print(f"[BƯỚC 1] Xác định chiều dài thông điệp ban đầu:")
    print(f"    l = {l_bits} bits")

    print(f"\n[BƯỚC 2] Tính số dư khi chia cho kích thước khối 512 bits:")
    print(f"    l mod 512 = {l_bits} mod 512 = {rem} bits")

    print(f"\n[BƯỚC 3] Áp dụng quy tắc đệm bit 1 và k bit 0 theo chuẩn SHA-1:")
    print(f"    - Thêm 1 bit '1' ngay sau thông điệp.")
    print(f"    - Thêm k bit '0' sao cho: (l + 1 + k) = 448 (mod 512)")
    print(f"    - Suy ra công thức tính k:")
    print(f"        k = (447 - (l mod 512)) mod 512 = (447 - {rem}) mod 512 = {k_zeros} bit 0")
    print(f"    ===> SỐ BIT 0 CẦN CHÈN THÊM: k = {k_zeros} bit 0")

    print(f"\n[BƯỚC 4] Biểu diễn trường chiều dài 64-bit của thông điệp gốc l (Big-Endian):")
    print(f"    - Giá trị thập phân : l = {l_bits}")
    print(f"    - Biểu diễn Hex 64-bit: {length_hex_64}")
    print(f"    - Biểu diễn Nhị phân  : {length_bin_64[:32]} {length_bin_64[32:]}")

    print(f"\n[BƯỚC 5] Cấu trúc thông điệp sau đệm hoàn chỉnh:")
    print(f"    Message_Padded = M (l bits) || '1' (1 bit) || '0'^{k_zeros} ({k_zeros} bits) || Length_64 (64 bits)")

    print(f"\n[BƯỚC 6] Tính tổng chiều dài thông điệp sau khi đệm:")
    print(f"    Total_Length = l + 1 + k + 64 = {l_bits} + 1 + {k_zeros} + 64 = {total_len} bits")
    print(f"    Kiểm tra tính chia hết: {total_len} % 512 = {total_len % 512} == 0 (Chính xác!)")

    print(f"\n[BƯỚC 7] Tính tổng số khối 512-bit (L):")
    print(f"    L = Total_Length / 512 = {total_len} / 512 = {total_blocks} khối")
    print(f"    (Mỗi khối gồm 16 từ 32-bit: W_0, W_1, ..., W_15)")
    print("=" * 75)
    return {
        "l": l_bits,
        "k_zeros": k_zeros,
        "hex_64": length_hex_64,
        "total_len": total_len,
        "blocks": total_blocks
    }


def solve_sha1_padding(custom_l=None):
    import sys
    if custom_l is None and len(sys.argv) > 1:
        try:
            custom_l = int(sys.argv[1])
        except ValueError:
            pass
    print("=" * 70)
    print("USTH FINAL EXAM 2025-2026 - EXERCISE 3: SHA-1 PADDING PREPROCESS")
    print("=" * 70)
    print("SHA-1 Preprocessing Rules (Session 7 Slide 20, Understanding Cryptography Sec 11.4):")
    print("  1. Append a single '1' bit to the original message.")
    print("  2. Append k '0' bits (0 <= k < 512) such that: (l + 1 + k) = 448 mod 512.")
    print("  3. Append the 64-bit Big-Endian binary representation of original length l.")
    print("  4. Total output length is an exact multiple of 512 bits (L * 512).")
    
    # Case 1: Printed on exam sheet (M = 20260 bits)
    solve_sha1_padding_for_len(20260, "Case A: Printed Exam Sheet Parameter (l = M = 20260 bits)")
    
    # Case 2: Personalized Student ID (l = 56 bits or custom)
    l_id = custom_l if custom_l is not None else 56
    solve_sha1_padding_for_len(l_id, f"Case B: Personalized Student ID (l = {l_id} bits)")
    print("=" * 70)

def custom_input():
    print("\n" + "=" * 70)
    print("CUSTOM EXAM INPUT: SHA-1 PADDING PREPROCESS")
    print("=" * 70)
    print("Choose input format:")
    print("  [1] Message bit length l directly (e.g. 20260 bits)")
    print("  [2] Text message string (length calculated in bits)")
    try:
        choice = input("Select [1/2, default 1]: ").strip()
        if choice == "2":
            txt = input("Enter text string [e.g. hello]: ")
            if not txt:
                txt = "hello"
            l_bits = len(txt.encode("utf-8")) * 8
            solve_sha1_padding_for_len(l_bits, f"Custom Text '{txt}' ({len(txt)} chars = {l_bits} bits)")
        else:
            val_l = input("Enter message bit length l [e.g. 20260]: ").strip()
            l_bits = int(val_l, 0) if val_l else 20260
            solve_sha1_padding_for_len(l_bits, f"Custom Bit Length l = {l_bits}")
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}")


if __name__ == "__main__":
    import sys

    # Direct interactive flag: python sha1_padding_preprocess.py -i
    if len(sys.argv) > 1 and sys.argv[1] in ("-i", "--interactive", "--custom"):
        custom_input()
        sys.exit(0)

    solve_sha1_padding()

    # Interactive prompt if user runs directly in terminal
    if sys.stdin.isatty():
        print("-" * 70)
        c = input("[?] Enter custom bit length l for your exam? [y/N]: ").strip().lower()
        if c in ("y", "yes"):
            custom_input()

