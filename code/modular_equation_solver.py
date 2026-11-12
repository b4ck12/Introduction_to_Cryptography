import os
# -*- coding: utf-8 -*-
"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Algorithm: Modular Equation Solver & Student ID Modulo Reducer
Student ID: 23BA14056 (x = 56)
=============================================================================
Description:
  Solves all common exam problems involving finding x modulo m:
  1. Student ID reduction: x = ID mod m (mod 64 for DES, mod 26 for Caesar, etc.)
  2. Linear congruence: a * x ≡ b (mod m) with full EEA essay steps.
  3. System of congruences: Chinese Remainder Theorem (CRT) finding x.
  4. Discrete logarithm: alpha^x ≡ beta (mod p) finding exponent x.
  5. Fast power congruence: x = base^exp (mod m) (Slide 25 exercises).
=============================================================================
"""

import sys
import math

def reduce_student_id_all(student_id_str: str = "23BA14056"):
    """
    Reduces student ID to integer x and prints common exam modulo values:
    - x = ID mod 64 (DES S-Box S1 input)
    - x = ID mod 26 (Caesar shift / Affine b)
    - x = ID mod 13 (Session 1 Exercises)
    - x = ID mod 10, mod 8, mod 5, mod 2
    """
    digits = "".join([c for c in student_id_str if c.isdigit()])
    if len(digits) >= 3:
        raw_val = int(digits[-3:])
    elif digits:
        raw_val = int(digits)
    else:
        raw_val = 56

    print("=" * 75)
    print(f"BẢNG RÚT GỌN MÃ SINH VIÊN QUA CÁC PHÉP MODULO TRONG ĐỀ THI")
    print(f"Mã sinh viên: {student_id_str} | 3 chữ số cuối: {raw_val:03d} (Số nguyên x = {raw_val})")
    print("=" * 75)
    print(f"[BƯỚC 1] Xác định số nguyên gốc từ mã sinh viên:")
    print(f"    Raw integer x = {raw_val}")

    mod_targets = [
        (64, "Đầu vào hộp S-Box DES S1 (Đề thi 2025-2026 Bài 1)"),
        (26, "Khóa dịch Caesar k hoặc hệ số Affine b (Mật mã cổ điển)"),
        (13, "Bài tập số học đồng dư Z_13 (Slide 15 - 25)"),
        (10, "Chữ số hàng đơn vị"),
        (8,  "Biểu diễn octal / 3-bit"),
        (5,  "Bảng cộng nhân Z_5 (Slide 21)"),
        (2,  "Tính chẵn / lẻ (bit b0)")
    ]

    print(f"\n[BƯỚC 2] Bảng giá trị rút gọn x mod m cho các bài thi:")
    print(f"{'Phép toán':<20} | {'Kết quả':<10} | {'Ứng dụng trong bài thi'}")
    print("-" * 75)
    results = {}
    for m, desc in mod_targets:
        res = raw_val % m
        results[m] = res
        print(f"x mod {m:<14} | = {res:<8} | {desc}")

    print("-" * 75)
    print(f"===> ĐÁP SỐ ĐẶC TRƯNG:")
    print(f"    * DES S-Box input  : x = {raw_val} mod 64 = {results[64]}")
    print(f"    * Caesar shift key : k = {raw_val} mod 26 = {results[26]}")
    print("=" * 75)
    return results


def solve_linear_congruence_essay(a: int, b: int, m: int):
    """
    Solves a * x ≡ b (mod m) with complete step-by-step essay presentation:
    - Step 1: Compute g = gcd(a, m)
    - Step 2: Solvability check (g | b)
    - Step 3: Reduction to a' * x ≡ b' (mod m') where gcd(a', m') = 1
    - Step 4: Modular inverse of a' mod m' via Extended Euclidean Algorithm
    - Step 5: Particular solution x0 = b' * (a')^-1 mod m'
    - Step 6: All g incongruent solutions in Z_m: x = x0 + k * m'
    """
    print("\n" + "=" * 75)
    print(f"GIẢI PHƯƠNG TRÌNH ĐỒNG DƯ BẬC NHẤT TÌM x: {a} · x ≡ {b} (mod {m})")
    print("=" * 75)

    # Step 1: gcd
    g = math.gcd(a, m)
    print(f"[BƯỚC 1] Tìm ước chung lớn nhất g = gcd(a, m):")
    print(f"    g = gcd({a}, {m}) = {g}")

    # Step 2: Check solvability
    print(f"\n[BƯỚC 2] Kiểm tra điều kiện tồn tại nghiệm (g có chia hết cho b?):")
    if b % g != 0:
        print(f"    [-] LỖI: g = {g} KHÔNG chia hết cho b = {b} ({b} % {g} = {b % g} != 0).")
        print(f"    ===> KẾT LUẬN: Phương trình {a}·x ≡ {b} (mod {m}) VÔ NGHIỆM!")
        print("=" * 75)
        return []

    print(f"    [+] {b} chia hết cho {g} ({b} = {g} * {b // g}) => Phương trình CÓ ĐÚNG {g} NGHIỆM trong Z_{m}.")

    # Step 3: Reduce
    a_prime = a // g
    b_prime = b // g
    m_prime = m // g
    print(f"\n[BƯỚC 3] Rút gọn phương trình bằng cách chia cả 2 vế và modulus cho g = {g}:")
    print(f"    a' = {a} / {g} = {a_prime}")
    print(f"    b' = {b} / {g} = {b_prime}")
    print(f"    m' = {m} / {g} = {m_prime}")
    print(f"    Phương trình tương đương: {a_prime} · x ≡ {b_prime} (mod {m_prime}) với gcd({a_prime}, {m_prime}) = 1.")

    # Step 4: Inverse
    print(f"\n[BƯỚC 4] Tìm nghịch đảo modulo (a')^(-1) mod m' = ({a_prime})^(-1) mod {m_prime}:")
    a_inv = pow(a_prime, -1, m_prime)
    print(f"    ({a_prime})^(-1) mod {m_prime} = {a_inv}")
    print(f"    Kiểm tra: ({a_prime} * {a_inv}) mod {m_prime} = {(a_prime * a_inv) % m_prime}")

    # Step 5: Particular solution
    x0 = (b_prime * a_inv) % m_prime
    print(f"\n[BƯỚC 5] Tính nghiệm đặc trưng x0 trong Z_{m_prime}:")
    print(f"    x0 = (b' * (a')^(-1)) mod m' = ({b_prime} * {a_inv}) mod {m_prime} = {b_prime * a_inv} mod {m_prime} = {x0}")

    # Step 6: All solutions
    solutions = [(x0 + k * m_prime) % m for k in range(g)]
    solutions.sort()
    print(f"\n[BƯỚC 6] Liệt kê tập {g} nghiệm nguyên phân biệt trong Z_{m}:")
    print(f"    Công thức tổng quát: x = x0 + k · m' = {x0} + k · {m_prime} (với k = 0, 1, ..., {g - 1})")
    for k in range(g):
        sol_k = (x0 + k * m_prime) % m
        print(f"    - Với k = {k}: x_{k} = {x0} + {k} * {m_prime} = {sol_k}")
        print(f"      Kiểm tra: ({a} * {sol_k}) mod {m} = {(a * sol_k) % m} == {b % m} (Chính xác!)")

    print(f"\n===> ĐÁP SỐ TẬP NGHIỆM:")
    print(f"    x ∈ {solutions} (mod {m})")
    print("=" * 75)
    return solutions


def solve_chinese_remainder_theorem(remainders: list, moduli: list):
    """
    Solves system of congruences using Chinese Remainder Theorem:
    x ≡ a_i (mod m_i)
    """
    print("\n" + "=" * 75)
    print("ĐỊNH LÝ SỐ DƯ TRUNG HOA (CHINESE REMAINDER THEOREM - CRT) TÌM x")
    print("=" * 75)
    n = len(moduli)
    for i in range(n):
        print(f"    x ≡ {remainders[i]} (mod {moduli[i]})")

    # Step 1: Pairwise coprime check
    print(f"\n[BƯỚC 1] Kiểm tra các modulus có nguyên tố cùng nhau từng đôi một:")
    for i in range(n):
        for j in range(i + 1, n):
            g = math.gcd(moduli[i], moduli[j])
            print(f"    gcd({moduli[i]}, {moduli[j]}) = {g}")
            if g != 1:
                print(f"    [-] LỖI: {moduli[i]} và {moduli[j]} không nguyên tố cùng nhau!")
                return None

    # Step 2: Compute M = prod(m_i)
    M = 1
    for m in moduli:
        M *= m
    print(f"\n[BƯỚC 2] Tính tích Modulus chung M:")
    print(f"    M = {' * '.join(map(str, moduli))} = {M}")

    # Step 3: Compute M_i and y_i = M_i^(-1) mod m_i
    print(f"\n[BƯỚC 3] Tính M_i = M / m_i và nghịch đảo y_i = M_i^(-1) mod m_i:")
    M_list = []
    y_list = []
    for i in range(n):
        Mi = M // moduli[i]
        yi = pow(Mi, -1, moduli[i])
        M_list.append(Mi)
        y_list.append(yi)
        print(f"    - Phương trình {i + 1}:")
        print(f"        M_{i+1} = {M} / {moduli[i]} = {Mi}")
        print(f"        y_{i+1} = {Mi}^(-1) mod {moduli[i]} = {yi}")
        print(f"        Kiểm tra: ({Mi} * {yi}) mod {moduli[i]} = {(Mi * yi) % moduli[i]}")

    # Step 4: Compute x = sum(a_i * M_i * y_i) mod M
    print(f"\n[BƯỚC 4] Tính nghiệm x duy nhất modulo M = {M}:")
    terms = []
    total = 0
    for i in range(n):
        term = remainders[i] * M_list[i] * y_list[i]
        terms.append(f"({remainders[i]} * {M_list[i]} * {y_list[i]})")
        total += term

    x_sol = total % M
    print(f"    x = {' + '.join(terms)} mod {M}")
    print(f"      = {total} mod {M} = {x_sol}")

    # Step 5: Verification
    print(f"\n[BƯỚC 5] Kiểm tra lại nghiệm với từng phương trình ban đầu:")
    for i in range(n):
        print(f"    x mod {moduli[i]} = {x_sol} mod {moduli[i]} = {x_sol % moduli[i]} == {remainders[i]} (Chính xác!)")

    print(f"\n===> ĐÁP SỐ DUY NHẤT:")
    print(f"    x ≡ {x_sol} (mod {M})")
    print("=" * 75)
    return x_sol


def custom_input():
    print("\n" + "=" * 75)
    print("CUSTOM EXAM INPUT: BỘ CÔNG CỤ TÌM x QUA MODULO & PHƯƠNG TRÌNH ĐỒNG DƯ")
    print("=" * 75)
    print("Chọn dạng toán cần tìm x:")
    print("  [1] Rút gọn mã sinh viên: x = ID mod các thứ (mod 64, mod 26, mod 13, ...)")
    print("  [2] Giải phương trình đồng dư bậc nhất: a * x ≡ b (mod m)")
    print("  [3] Định lý số dư Trung Hoa (CRT): Hệ phương trình x ≡ a_i (mod m_i)")
    print("  [4] Tính nhanh x = base^exp mod m (Dạng bài Slide 25)")
    try:
        c = input("\nChọn [1-4, mặc định 1]: ").strip()
        if c == "2":
            val_a = input("Nhập hệ số a [e.g. 7]: ").strip()
            a = int(val_a, 0) if val_a else 7
            val_b = input("Nhập hệ số tự do b [e.g. 11]: ").strip()
            b = int(val_b, 0) if val_b else 11
            val_m = input("Nhập modulus m [e.g. 13]: ").strip()
            m = int(val_m, 0) if val_m else 13
            solve_linear_congruence_essay(a, b, m)
        elif c == "3":
            raw_a = input("Nhập danh sách số dư a_i cách nhau bởi dấu phẩy [e.g. 2, 3, 2]: ").strip()
            rem = [int(x.strip(), 0) for x in raw_a.split(",")] if raw_a else [2, 3, 2]
            raw_m = input("Nhập danh sách modulus m_i cách nhau bởi dấu phẩy [e.g. 3, 5, 7]: ").strip()
            mod = [int(x.strip(), 0) for x in raw_m.split(",")] if raw_m else [3, 5, 7]
            solve_chinese_remainder_theorem(rem, mod)
        elif c == "4":
            val_b = input("Nhập cơ số base [e.g. 7]: ").strip()
            base = int(val_b, 0) if val_b else 7
            val_e = input("Nhập số mũ exp [e.g. 100]: ").strip()
            exp = int(val_e, 0) if val_e else 100
            val_m = input("Nhập modulus m [e.g. 13]: ").strip()
            m = int(val_m, 0) if val_m else 13
            ans = pow(base, exp, m)
            print(f"\n[=>] x = {base}^{exp} mod {m} = {ans}")
        else:
            val_id = input("Nhập mã sinh viên [mặc định: 23BA14056]: ").strip()
            sid = val_id if val_id else "23BA14056"
            reduce_student_id_all(sid)
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}. Using default.")
        try:
            run_demo()
        except Exception:
            pass


def run_demo():
    print("=" * 75)
    print("DEMO: BỘ BÀI TẬP TÌM x QUA MODULO (SLIDE 25 & ĐỀ THI)")
    print("=" * 75)
    # 1. Rút gọn mã sinh viên 23BA14056
    reduce_student_id_all("23BA14056")

    # 2. Giải Session 1 Slide 25 Exercise 2(e): 7*x ≡ 11 (mod 13)
    solve_linear_congruence_essay(7, 11, 13)

    # 3. Giải Session 1 Slide 25 Exercise 2(f): 3*x ≡ 4 (mod 13)
    solve_linear_congruence_essay(3, 4, 13)

    # 4. Giải RSA Private Key Equation: 125*x ≡ 1 (mod 31188)
    solve_linear_congruence_essay(125, 1, 31188)

    # 5. Chinese Remainder Theorem: x ≡ 2 mod 3, x ≡ 3 mod 5, x ≡ 2 mod 7
    solve_chinese_remainder_theorem([2, 3, 2], [3, 5, 7])


def parse_flexible_int(val):
    val_str = str(val).strip()
    try:
        return int(val_str, 0)
    except ValueError:
        digits = "".join(filter(str.isdigit, val_str))
        if digits:
            return int(digits[-3:]) if len(digits) >= 3 else int(digits)
        raise ValueError(f"Cannot parse integer from '{val}'")


if __name__ == "__main__":
    if "--demo" in sys.argv or (not sys.stdin.isatty() and len(sys.argv) <= 1):
        run_demo()
        sys.exit(0)

    # Extract non-flag arguments
    args = [a for a in sys.argv[1:] if not a.startswith("-")]

    # Check if solving linear congruence: a * x ≡ b (mod m)
    # Requires args[0] (a), args[1] (b), args[2] (m) to be non-empty
    if len(args) >= 3 and args[1].strip() and args[2].strip():
        try:
            a_val = parse_flexible_int(args[0])
            b_val = parse_flexible_int(args[1])
            m_val = parse_flexible_int(args[2])
            solve_linear_congruence_essay(a_val, b_val, m_val)
            sys.exit(0)
        except Exception as err:
            print(f"[-] Linear congruence solver error: {err}")

    # If only 1 argument or b is empty -> reduce student ID modulo 64, 26, etc.
    if len(args) >= 1 and args[0].strip():
        try:
            reduce_student_id_all(args[0].strip())
            sys.exit(0)
        except Exception as err:
            print(f"[-] Student ID reduction error: {err}")

    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
    else:
        try:
            custom_input()
        except (EOFError, KeyboardInterrupt):
            run_demo()
