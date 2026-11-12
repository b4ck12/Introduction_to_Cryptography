# -*- coding: utf-8 -*-
"""
Script: solve_rsa_encrypt_2025.py
Description: Solves Exercise 2.3 (RSA Encryption & Decryption) for Exam 2025-2026.
Evaluates both M = 56 (Student ID 23BA14056) and M = 20260 (Printed on exam paper).
Keypair from 2.1: N = 31553, e = 125, d = 30689.
"""

def square_and_multiply_trace(base: int, exponent: int, modulus: int, title: str = ""):
    x = base % modulus
    bin_exp = bin(exponent)[2:]
    print(f"\n    [+] BẢNG TÍNH LŨY THỪA NHANH (Square-and-Multiply) CHO {title}:")
    print(f"        {base}^{exponent} mod {modulus} (Số mũ nhị phân: {bin_exp}, {len(bin_exp)} bits)")
    print(f"        {'Bước':<6} | {'Bit':<4} | {'Phép toán':<10} | {'Tính toán':<24} | {'Giá trị hiện tại'}")
    print("        " + "-" * 62)
    y = 1
    step = 0
    for i, bit in enumerate(bin_exp):
        step += 1
        sq_val = (y * y) % modulus
        calc_sq = f"{y}^2 mod {modulus}"
        print(f"        {step:<6} | {bit:<4} | {'Square':<10} | {calc_sq:<24} | {sq_val}")
        y = sq_val
        if bit == '1':
            step += 1
            mul_val = (y * x) % modulus
            calc_mul = f"{y} * {x} mod {modulus}"
            print(f"        {step:<6} | {bit:<4} | {'Multiply':<10} | {calc_mul:<24} | {mul_val}")
            y = mul_val
    print("        " + "-" * 62)
    print(f"        ===> KẾT QUẢ: {base}^{exponent} mod {modulus} = {y}\n")
    return y

def solve_rsa_encryption(custom_m=None):
    import sys
    if custom_m is None and len(sys.argv) > 1:
        try:
            custom_m = int(sys.argv[1])
        except ValueError:
            pass
    M_val = custom_m if custom_m is not None else 56
    N = 31553
    e = 125
    d = 30689
    
    print("=" * 75)
    print("USTH FINAL EXAM 2025-2026 - EXERCISE 2.3: RSA ENCRYPT & DECRYPT (LỜI GIẢI TỰ LUẬN)")
    print("=" * 75)
    print(f"Tham số hệ thống đã cho: Modulus N = {N}, Khóa công khai e = {e}, Khóa bí mật d = {d}\n")
    
    # Case 1: Student ID (Default M = 56)
    print(f"[TRƯỜNG HỢP 1: THÔNG ĐIỆP MÃ SINH VIÊN (M = {M_val})]")
    print(f"[BƯỚC 1] Quá trình mã hóa (Encryption):")
    print(f"    Công thức: C = M^e mod N = {M_val}^{e} mod {N}")
    C1 = square_and_multiply_trace(M_val, e, N, f"Mã hóa C = {M_val}^{e} mod {N}")
    
    print(f"[BƯỚC 2] Quá trình giải mã (Decryption):")
    print(f"    Công thức: M = C^d mod N = {C1}^{d} mod {N}")
    M1_dec = pow(C1, d, N)
    print(f"    Kết quả giải mã: M = {C1}^{d} mod {N} = {M1_dec}")
    print(f"    Kiểm tra khôi phục bản rõ: {M1_dec} == {M_val} ({M1_dec == M_val} - Chính xác tuyệt đối!)\n")
    
    # Case 2: Printed on exam sheet (M = 20260)
    M2 = 20260
    print(f"[TRƯỜNG HỢP 2: THÔNG ĐIỆP ĐỀ IN TRÊN GIẤY (M = {M2})]")
    print(f"[BƯỚC 1] Quá trình mã hóa:")
    print(f"    C = {M2}^{e} mod {N}")
    C2 = pow(M2, e, N)
    print(f"    Bản mã C = {C2}")
    
    print(f"[BƯỚC 2] Quá trình giải mã:")
    print(f"    M = {C2}^{d} mod {N} = {pow(C2, d, N)}")
    print(f"    Kiểm tra: {pow(C2, d, N) == M2} (Chính xác!)")
    print("=" * 75)
    return {
        "case_student": {"M": M_val, "C": C1, "dec": M1_dec},
        "case_printed": {"M": M2, "C": C2, "dec": pow(C2, d, N)}
    }

def custom_rsa_calc(M: int, e: int, d: int, N: int):
    print("\n" + "=" * 75)
    print("CUSTOM RSA ENCRYPTION / DECRYPTION - LỜI GIẢI TỰ LUẬN TỪNG BƯỚC")
    print("=" * 75)
    print(f"Tham số: Modulus N = {N}, Public e = {e}, Plaintext M = {M}")
    print(f"\n[BƯỚC 1] Quá trình mã hóa C = M^e mod N = {M}^{e} mod {N}:")
    C = square_and_multiply_trace(M, e, N, f"Mã hóa C = {M}^{e} mod {N}")
    print(f"===> BẢN MÃ THU ĐƯỢC: C = {C}")

    if d:
        print(f"\n[BƯỚC 2] Quá trình giải mã M = C^d mod N = {C}^{d} mod {N}:")
        M_dec = square_and_multiply_trace(C, d, N, f"Giải mã M = {C}^{d} mod {N}")
        print(f"===> BẢN RÕ KHÔI PHỤC: M = {M_dec}")
        print(f"===> KIỂM TRA KHỚP BẢN RÕ GỐC: {M_dec == M} (Chính xác!)")
    print("=" * 75)



def custom_input():
    print("\n" + "=" * 65)
    print("CUSTOM EXAM INPUT: RSA ENCRYPTION / DECRYPTION")
    print("=" * 65)
    try:
        val_m = input("Enter message M [e.g. 56]: ").strip()
        m = int(val_m, 0) if val_m else 56
        val_n = input("Enter modulus N [e.g. 31553]: ").strip()
        n = int(val_n, 0) if val_n else 31553
        val_e = input("Enter public exponent e [e.g. 125]: ").strip()
        e = int(val_e, 0) if val_e else 125
        val_d = input("Enter private exponent d (optional, press Enter to skip) [e.g. 30689]: ").strip()
        d = int(val_d, 0) if val_d else None
        custom_rsa_calc(m, e, d, n)
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input cancelled or non-interactive: {err}. Falling back to exam defaults.")
        run_demo()


run_demo = solve_rsa_encryption


if __name__ == "__main__":
    import os
    import sys

    # Demo mode or non-interactive pipe
    if "--demo" in sys.argv:
        solve_rsa_encryption()
        sys.exit(0)

    # Support CLI arguments: python rsa_encryption_decryption.py 20260 125 31553 30689
    cli_args = [a for a in sys.argv[1:] if a.strip() and not a.startswith("-")]
    if len(cli_args) >= 3:
        try:
            m_arg = int(cli_args[0], 0)
            e_arg = int(cli_args[1], 0)
            n_arg = int(cli_args[2], 0)
            d_arg = int(cli_args[3], 0) if len(cli_args) > 3 else None
            custom_rsa_calc(m_arg, e_arg, d_arg, n_arg)
            sys.exit(0)
        except Exception as err:
            print(f"[-] CLI error: {err}")
            if os.environ.get("GUI_MODE") == "1":
                solve_rsa_encryption()
                sys.exit(0)

    # In GUI mode or non-interactive terminal, never prompt for stdin input
    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
    else:
        try:
            custom_input()
        except (EOFError, KeyboardInterrupt):
            run_demo()