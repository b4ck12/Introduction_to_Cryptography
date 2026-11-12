# -*- coding: utf-8 -*-
"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Algorithm: Direct Modulo Calculator (a mod m, Expression mod m, Negative mod m)
Student ID: 23BA14056 (x = 56)
=============================================================================
Description:
  Computes direct modulo: r = a mod m (such that a = q * m + r with 0 <= r < m).
  Supports:
  1. Standard integers: 56 mod 64 = 56, 56 mod 26 = 4.
  2. Negative numbers: -11 mod 13 = 2, -14594 mod 996 = 346.
  3. Mathematical expressions: 15*29 mod 13, -11*3 mod 13.
  4. Student ID strings: '23BA14056' mod 64 = 56.
=============================================================================
"""

import sys
import os
import math
import re

def safe_eval_expr(expr_str: str) -> int:
    """Safely evaluates basic arithmetic expressions (+, -, *, //, %, parentheses)."""
    s = str(expr_str).strip()
    # If student ID like 23BA14056
    digits = re.findall(r'\d+', s)
    if any(c.isalpha() for c in s) and digits:
        last = digits[-1]
        return int(last[-3:]) if len(last) >= 3 else int(last)

    # Clean arithmetic expression
    allowed = set("0123456789+-*/() \t_")
    if not set(s).issubset(allowed):
        raise ValueError(f"Biểu thức chứa ký tự không hợp lệ: '{s}'")
    
    # Replace single / with // for integer division
    clean = re.sub(r'(?<!/)/(?!/)', '//', s)
    return int(eval(clean, {"__builtins__": None}, {}))


def calculate_modulo_detail(a_input, m_input):
    """
    Solves a mod m with comprehensive step-by-step written essay derivation.
    """
    if isinstance(a_input, str):
        a_val = safe_eval_expr(a_input)
    else:
        a_val = int(a_input)

    if isinstance(m_input, str):
        m_val = safe_eval_expr(m_input)
    else:
        m_val = int(m_input)

    if m_val <= 0:
        raise ValueError(f"Modulus m phải là số nguyên dương (m > 0), nhận được: {m_val}")

    q = a_val // m_val
    r = a_val % m_val

    print("=" * 75)
    print(f"PHÉP TÍNH MODULO (MODULAR ARITHMETIC): {a_input} mod {m_val}")
    print("=" * 75)
    print(f"[BƯỚC 1] Thiết lập bài toán & Định nghĩa phép Modulo:")
    print(f"    Công thức tổng quát: a = q * m + r  (với điều kiện tiên quyết: 0 <= r < m)")
    print(f"    * Số bị chia a = {a_val} (từ biểu thức: '{a_input}')")
    print(f"    * Số chia Modulus m = {m_val}\n")

    print(f"[BƯỚC 2] Quá trình chia Euclid để tìm thương số q và số dư chuẩn r:")
    print(f"    * Thương số nguyên: q = floor({a_val} / {m_val}) = {q}")
    print(f"    * Phần dư chuẩn  : r = a - (q * m) = {a_val} - ({q} * {m_val}) = {r}")
    print(f"    * Đẳng thức chia Euclid: {a_val} = {q} * {m_val} + {r}")
    if a_val < 0:
        print(f"    [!] LƯU Ý SỐ ÂM (Chuẩn giảng đường USTH):")
        print(f"        Trong toán học đồng dư, phần dư r LUÔN LUÔN không âm (0 <= r < {m_val}).")
        print(f"        Vì {a_val} < 0, ta lùi thương q xuống floor({a_val}/{m_val}) = {q}")
        print(f"        Do đó: {a_val} = {q} * {m_val} + {r}  ===> Phần dư chuẩn là r = {r}.\n")
    else:
        print(f"    Kiểm tra điều kiện: 0 <= {r} < {m_val} -> True (Chính xác tuyệt đối!)\n")

    print(f"[BƯỚC 3] Biểu diễn đồng dư (Modular Congruence):")
    print(f"    {a_val} ≡ {r} (mod {m_val})")
    print(f"    ===> KẾT QUẢ ĐỒNG DƯ: {a_input} mod {m_val} = {r}\n")

    # Step 4: Exam applications
    print(f"[BƯỚC 4] Ý nghĩa & Ứng dụng trong các bài thi USTH Cryptography:")
    if m_val == 64:
        bin6 = bin(r)[2:].zfill(6)
        row = int(bin6[0] + bin6[5], 2)
        col = int(bin6[1:5], 2)
        print(f"    - Ứng dụng Hộp S-Box DES S1 (Bài 1 Đề thi 2025-2026):")
        print(f"      Đầu vào x = {a_val} mod 64 = {r}.")
        print(f"      Biểu diễn 6 bit nhị phân: {r} = {bin6}₂ (b1={bin6[0]}, b2={bin6[1]}, b3={bin6[2]}, b4={bin6[3]}, b5={bin6[4]}, b6={bin6[5]}).")
        print(f"      Hàng r = (b1 b6)₂ = ({bin6[0]}{bin6[5]})₂ = {row}")
        print(f"      Cột c  = (b2 b3 b4 b5)₂ = ({bin6[1:5]})₂ = {col}")
    elif m_val == 26:
        print(f"    - Ứng dụng Mật mã Cổ điển (Caesar / Affine / Vigenère):")
        print(f"      Khóa dịch k = {a_val} mod 26 = {r}.")
        print(f"      Ký tự tương ứng trong bảng chữ cái (A=0, B=1, ...): '{chr(ord('A') + r)}'")
    elif m_val == 13:
        print(f"    - Ứng dụng Bài tập Số học Đồng dư Z_13 (Slide 24, 25 Session 1):")
        print(f"      Phần tử đại diện trong Z_13 = {r}.")
    else:
        print(f"    - Ứng dụng rút gọn số trong hệ mã hóa khóa công khai (RSA / ElGamal / DHKE):")
        print(f"      Thu gọn giá trị trung gian về không gian Z_{m_val}: {r}.")

    print("=" * 75)
    return {"a": a_val, "m": m_val, "q": q, "r": r}


def run_demo():
    print("=" * 75)
    print("DEMO: CÁC PHÉP TÍNH MODULO KINH ĐIỂN TRONG ĐỀ THI USTH")
    print("=" * 75)
    calculate_modulo_detail("56", 64)
    print("\n")
    calculate_modulo_detail("56", 26)
    print("\n")
    calculate_modulo_detail("-11", 13)


def custom_input():
    import os, sys
    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
        return

    print("\n" + "=" * 65)
    print("CUSTOM EXAM INPUT: PHÉP TÍNH MODULO (a mod m)")
    print("=" * 65)
    try:
        val_a = input("Nhập số a hoặc biểu thức [mặc định: 56]: ").strip()
        a_in = val_a if val_a else "56"
        val_m = input("Nhập modulus m [mặc định: 64]: ").strip()
        m_in = val_m if val_m else "64"
        calculate_modulo_detail(a_in, m_in)
    except (KeyboardInterrupt, EOFError, ValueError) as err:
        print(f"[-] Input error: {err}. Chạy bộ đề thi mẫu...")
        run_demo()


if __name__ == "__main__":
    if "--demo" in sys.argv:
        run_demo()
        sys.exit(0)

    cli_args = [a for a in sys.argv[1:] if a.strip() and not (a.startswith("-") and not (len(a) > 1 and a[1].isdigit()))]
    if len(cli_args) >= 2:
        try:
            calculate_modulo_detail(cli_args[0], cli_args[1])
            sys.exit(0)
        except Exception as err:
            print(f"[-] CLI error: {err}")
            sys.exit(1)
    elif len(cli_args) == 1:
        try:
            calculate_modulo_detail(cli_args[0], 64)
            sys.exit(0)
        except Exception as err:
            print(f"[-] CLI error: {err}")
            sys.exit(1)

    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
    else:
        try:
            custom_input()
        except (EOFError, KeyboardInterrupt):
            run_demo()
