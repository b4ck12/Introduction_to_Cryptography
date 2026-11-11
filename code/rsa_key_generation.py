# -*- coding: utf-8 -*-
"""
Script: solve_rsa_keygen_2025.py
Description: Solves Exercise 2.1 (RSA Key Generation) for Exam 2025-2026.
Parameters: p = 139, q = 227, Candidate exponents = {122, 123, 124, 125}.
"""
import math

def factorize(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inv(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"No modular inverse for {a} mod {m}")
    return (x % m + m) % m

def print_eea_table(m: int, a: int):
    """Prints the step-by-step Extended Euclidean Algorithm table to solve a*d = 1 (mod m)."""
    print(f"\n    [+] BẢNG THUẬT TOÁN EUCLID MỞ RỘNG (Tìm d = {a}^(-1) mod {m}):")
    print(f"    {'Bước':<7} | {'q':<6} | {'r':<10} | {'s':<10} | {'t':<10} | {'Phương trình chia'}")
    print("    " + "-" * 72)
    r_prev, r_curr = m, a
    s_prev, s_curr = 1, 0
    t_prev, t_curr = 0, 1
    print(f"    {'init':<7} | {'-':<6} | {r_prev:<10} | {s_prev:<10} | {t_prev:<10} | r0 = {r_prev}")
    print(f"    {'init':<7} | {'-':<6} | {r_curr:<10} | {s_curr:<10} | {t_curr:<10} | r1 = {r_curr}")
    step = 1
    while r_curr != 0:
        q = r_prev // r_curr
        r_next = r_prev - q * r_curr
        s_next = s_prev - q * s_curr
        t_next = t_prev - q * t_curr
        eq = f"{r_prev} = {q} * {r_curr} + {r_next}"
        print(f"    Bước {step:<2} | {q:<6} | {r_next:<10} | {s_next:<10} | {t_next:<10} | {eq}")
        r_prev, r_curr = r_curr, r_next
        s_prev, s_curr = s_curr, s_next
        t_prev, t_curr = t_curr, t_next
        step += 1
    gcd_val = r_prev
    s_val = s_prev
    t_val = t_prev
    d_inv = t_val % m
    print("    " + "-" * 72)
    print(f"    [=>] gcd({m}, {a}) = {gcd_val}")
    print(f"    [=>] Hệ thức Bézout: ({m}) * ({s_val}) + ({a}) * ({t_val}) = {gcd_val}")
    print(f"    [=>] Lấy modulo {m}: ({a}) * ({t_val}) = 1 (mod {m})")
    print(f"    [=>] Khóa riêng d = {t_val} mod {m} = {d_inv}")
    return d_inv

def solve_rsa_keygen():
    p = 139
    q = 227
    candidates = [122, 123, 124, 125]
    
    print("=" * 75)
    print("USTH FINAL EXAM 2025-2026 - EXERCISE 2.1: RSA KEY GENERATION (LỜI GIẢI TỰ LUẬN)")
    print("=" * 75)
    
    # Bước 1
    N = p * q
    print(f"[BƯỚC 1] Tính Modulus N:")
    print(f"    N = p * q = {p} * {q} = {N}")
    
    # Bước 2
    phi = (p - 1) * (q - 1)
    print(f"\n[BƯỚC 2] Tính Hàm Phi Euler phi(N):")
    print(f"    phi(N) = (p - 1) * (q - 1) = {p - 1} * {q - 1} = {phi}")
    
    # Bước 3
    phi_factors = factorize(phi)
    print(f"\n[BƯỚC 3] Phân tích thừa số nguyên tố của phi(N):")
    print(f"    phi(N) = {phi} = {' * '.join(map(str, phi_factors))}")
    print(f"    Tập các ước nguyên tố của phi(N): P = {sorted(list(set(phi_factors)))}")
    
    # Bước 4
    print(f"\n[BƯỚC 4] Kiểm tra điều kiện số mũ công khai gcd(e, phi(N)) == 1 trong tập {candidates}:")
    selected_e = None
    for e in candidates:
        g = math.gcd(e, phi)
        is_coprime = (g == 1)
        if e % 2 == 0:
            reason = f"Số chẵn => chia hết cho 2 (gcd = {g} != 1) => LOẠI"
        elif e % 3 == 0:
            reason = f"Chia hết cho 3 (gcd = {g} != 1) => LOẠI"
        elif is_coprime:
            reason = f"Nguyên tố cùng nhau với {phi} (gcd = 1) => CHẤP NHẬN"
        else:
            reason = f"gcd({e}, {phi}) = {g} != 1 => LOẠI"
        print(f"    - e = {e:3d}: {reason}")
        if is_coprime and selected_e is None:
            selected_e = e
            
    print(f"    ===> CHỌN SỐ MŨ CÔNG KHAI: e_A = {selected_e}")
    
    # Bước 5
    print(f"\n[BƯỚC 5] Tính khóa bí mật d_A = e^(-1) mod phi(N) bằng thuật toán Euclid mở rộng:")
    print(f"    Giải phương trình đồng dư: {selected_e} * d_A = 1 (mod {phi})")
    d = print_eea_table(phi, selected_e)
    
    # Bước 6
    verification = (selected_e * d) % phi
    print(f"\n[BƯỚC 6] Kiểm tra lại phương trình đồng dư (Verification):")
    print(f"    ({selected_e} * {d}) mod {phi} = {selected_e * d} mod {phi} = {verification} (Chính xác 100%!)")
    
    # Bước 7
    print(f"\n[BƯỚC 7] Kết luận cặp khóa cho người dùng A:")
    print(f"    * Khóa công khai (Public Key) : k_pubA = (N = {N}, e = {selected_e})")
    print(f"    * Khóa bí mật (Private Key)   : k_priA = (d = {d})")
    print("=" * 75)

    # Session 6 Slide 10: Textbook RSA Example
    print("\nSESSION 6 SLIDE 10: TEXTBOOK RSA EXAMPLE")
    print("-" * 75)
    p_tb, q_tb, e_tb = 11, 3, 3
    n_tb = p_tb * q_tb
    phi_tb = (p_tb - 1) * (q_tb - 1)
    d_tb = mod_inv(e_tb, phi_tb)
    print(f"  Given primes:                 p = {p_tb}, q = {q_tb}")
    print(f"  Modulus N = p * q:            {n_tb}")
    print(f"  Totient phi(N) = (p-1)*(q-1): {phi_tb}")
    print(f"  Public Exponent e:            {e_tb} (gcd({e_tb}, {phi_tb}) = {math.gcd(e_tb, phi_tb)})")
    print(f"  Private Key d = e^-1 mod phi: {e_tb}^-1 mod {phi_tb} = {d_tb}")
    print(f"  Public Key: (N = {n_tb}, e = {e_tb}), Private Key: (d = {d_tb})")
    
    m_tb = 15
    c_tb = pow(m_tb, e_tb, n_tb)
    dec_tb = pow(c_tb, d_tb, n_tb)
    print(f"  Encryption of M = {m_tb}:     C = {m_tb}^{e_tb} mod {n_tb} = {c_tb}")
    print(f"  Decryption of C = {c_tb}:      M = {c_tb}^{d_tb} mod {n_tb} = {dec_tb} (Match: {dec_tb == m_tb})")
    print("=" * 75)

    return {
        "p": p,
        "q": q,
        "N": N,
        "phi": phi,
        "e": selected_e,
        "d": d
    }

def custom_rsa_keygen(p: int, q: int, candidates=None):
    N = p * q
    phi = (p - 1) * (q - 1)
    phi_factors = factorize(phi)
    
    print("\n" + "=" * 75)
    print(f"CUSTOM RSA KEY GENERATION - LỜI GIẢI TỰ LUẬN (p = {p}, q = {q})")
    print("=" * 75)
    print(f"[BƯỚC 1] Tính Modulus N:")
    print(f"    N = p * q = {p} * {q} = {N}")
    
    print(f"\n[BƯỚC 2] Tính Hàm Phi Euler phi(N):")
    print(f"    phi(N) = (p - 1) * (q - 1) = {p - 1} * {q - 1} = {phi}")
    
    print(f"\n[BƯỚC 3] Phân tích thừa số nguyên tố của phi(N):")
    print(f"    phi(N) = {phi} = {' * '.join(map(str, phi_factors))}")
    print(f"    Ước nguyên tố: {sorted(list(set(phi_factors)))}")
    
    if candidates is None:
        candidates = [65537, 3, 17, 125]
    elif isinstance(candidates, int):
        candidates = [candidates]

    print(f"\n[BƯỚC 4] Đánh giá các số mũ công khai e trong tập {candidates}:")
    selected_e = None
    for e in candidates:
        g = math.gcd(e, phi)
        is_coprime = (g == 1)
        status = "CHẤP NHẬN (gcd = 1, hợp lệ)" if is_coprime else f"LOẠI (gcd = {g} != 1)"
        print(f"    - e = {e:5d}: gcd({e}, {phi}) = {g:2d} -> {status}")
        if is_coprime and selected_e is None:
            selected_e = e

    if selected_e is None:
        print("[-] Không có số mũ công khai nào thỏa mãn nguyên tố cùng nhau với phi(N).")
        return None

    print(f"    ===> CHỌN: e = {selected_e}")

    print(f"\n[BƯỚC 5] Bảng tính thuật toán Euclid mở rộng tìm khóa riêng d = {selected_e}^(-1) mod {phi}:")
    d = print_eea_table(phi, selected_e)
    verification = (selected_e * d) % phi

    print(f"\n[BƯỚC 6] Kiểm tra lại phương trình đồng dư:")
    print(f"    ({selected_e} * {d}) mod {phi} = {verification} (Hợp lệ!)")
    
    print(f"\n[BƯỚC 7] Kết luận cặp khóa:")
    print(f"    * Khóa công khai : k_pub = (N = {N}, e = {selected_e})")
    print(f"    * Khóa bí mật   : k_pri = (N = {N}, d = {d})")
    print("=" * 75)
    return {"p": p, "q": q, "N": N, "phi": phi, "e": selected_e, "d": d}



def custom_input():
    print("\n" + "=" * 65)
    print("CUSTOM EXAM INPUT: RSA KEY GENERATION")
    print("=" * 65)
    try:
        val_p = input("Enter prime p [e.g. 139]: ").strip()
        p = int(val_p, 0) if val_p else 139
        val_q = input("Enter prime q [e.g. 227]: ").strip()
        q = int(val_q, 0) if val_q else 227
        val_e = input("Enter candidate e or comma-separated list [e.g. 122, 123, 124, 125]: ").strip()
        if val_e:
            cands = [int(x.strip(), 0) for x in val_e.split(",") if x.strip()]
        else:
            cands = [122, 123, 124, 125]
        custom_rsa_keygen(p, q, cands)
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}")


if __name__ == "__main__":
    import sys

    # Support CLI arguments: python rsa_key_generation.py 139 227 125
    if len(sys.argv) > 2 and sys.argv[1] not in ("-i", "--interactive", "--custom"):
        try:
            p_arg = int(sys.argv[1], 0)
            q_arg = int(sys.argv[2], 0)
            e_arg = [int(sys.argv[3], 0)] if len(sys.argv) > 3 else [65537, 3, 17, 125]
            custom_rsa_keygen(p_arg, q_arg, e_arg)
            sys.exit(0)
        except Exception:
            pass

    # Direct interactive flag: python rsa_key_generation.py -i
    if len(sys.argv) > 1 and sys.argv[1] in ("-i", "--interactive", "--custom"):
        custom_input()
        sys.exit(0)

    solve_rsa_keygen()

    # Interactive prompt if user runs directly in terminal
    if sys.stdin.isatty():
        print("-" * 65)
        c = input("[?] Enter custom p, q, e for your exam? [y/N]: ").strip().lower()
        if c in ("y", "yes"):
            custom_input()

