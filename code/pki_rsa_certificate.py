# -*- coding: utf-8 -*-
"""
Script: solve_exam_2024.py
Description: Solves all calculation problems for USTH Final Exam 2024-2025 (Code 01).
  - Exercise 1.1: RSA Key Generation (p = 223, q = 193, candidates: {3525, 5525, 6525}).
  - Exercise 1.2: CA Digital Certificate with RSA (p_CA = 227, q_CA = 149, e_CA = 25537, M = 56).
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

def print_eea_table(m: int, a: int):
    """Prints Extended Euclidean Algorithm table for a^(-1) mod m."""
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
    inv = t_prev % m
    print("    " + "-" * 72)
    print(f"    [=>] gcd({m}, {a}) = {r_prev}")
    print(f"    [=>] Khóa riêng d = {t_prev} mod {m} = {inv}")
    return inv

def solve_exam_2024(student_id=56):
    import sys
    if len(sys.argv) > 1:
        try:
            student_id = int(sys.argv[1])
        except ValueError:
            pass
    print("=" * 75)
    print("USTH FINAL EXAM 2024-2025 - EXERCISE 1.1: RSA KEY GENERATION (LỜI GIẢI TỰ LUẬN)")
    print("=" * 75)
    p = 223
    q = 193
    
    print(f"[BƯỚC 1] Tính Modulus N:")
    N = p * q
    print(f"    N = p * q = {p} * {q} = {N}")
    
    print(f"\n[BƯỚC 2] Tính Hàm Phi Euler phi(N):")
    phi = (p - 1) * (q - 1)
    print(f"    phi(N) = (p - 1) * (q - 1) = {p - 1} * {q - 1} = {phi}")
    
    print(f"\n[BƯỚC 3] Phân tích thừa số nguyên tố phi(N):")
    phi_factors = factorize(phi)
    print(f"    phi(N) = {phi} = {' * '.join(map(str, phi_factors))}")
    print(f"    Tập các ước nguyên tố của phi(N): P = {sorted(list(set(phi_factors)))}")
    
    print(f"\n[BƯỚC 4] Kiểm tra các ứng viên số mũ công khai e trong tập [3525, 5525, 6525]:")
    candidates = [3525, 5525, 6525]
    selected_e = None
    for e in candidates:
        g = math.gcd(e, phi)
        if e % 3 == 0:
            status = f"Chia hết cho 3 (gcd = {g} != 1) => LOẠI"
        elif g == 1:
            status = "Nguyên tố cùng nhau (gcd = 1) => CHẤP NHẬN"
        else:
            status = f"gcd = {g} != 1 => LOẠI"
        print(f"    - e = {e}: {status}")
        if g == 1 and selected_e is None:
            selected_e = e
            
    print(f"    ===> CHỌN SỐ MŨ CÔNG KHAI: e = {selected_e}")
    
    print(f"\n[BƯỚC 5] Bảng thuật toán Euclid mở rộng tìm khóa riêng d = {selected_e}^(-1) mod {phi}:")
    d = print_eea_table(phi, selected_e)
    print(f"    Kiểm tra lại: ({selected_e} * {d}) mod {phi} = {(selected_e * d) % phi} (Hợp lệ!)")
    
    print(f"\n[BƯỚC 6] Kết luận cặp khóa:")
    print(f"    * Khóa công khai : k_pub = (N = {N}, e = {selected_e})")
    print(f"    * Khóa bí mật   : k_pri = (d = {d})")
    
    print("\n" + "=" * 75)
    print("USTH FINAL EXAM 2024-2025 - EXERCISE 1.2: CA RSA DIGITAL CERTIFICATE (LỜI GIẢI TỰ LUẬN)")
    print("=" * 75)
    p_CA = 227
    q_CA = 149
    e_CA = 25537
    M = student_id # Student ID (Default 56)
    
    print(f"[BƯỚC 1] Thiết lập thông số khóa của Cơ quan Chứng thực CA:")
    N_CA = p_CA * q_CA
    phi_CA = (p_CA - 1) * (q_CA - 1)
    print(f"    * CA Modulus N_CA = p_CA * q_CA = {p_CA} * {q_CA} = {N_CA}")
    print(f"    * CA phi(N_CA)    = (p_CA - 1)*(q_CA - 1) = {p_CA - 1} * {q_CA - 1} = {phi_CA}")
    print(f"    * CA Khóa riêng d_CA = {e_CA}^(-1) mod {phi_CA}:")
    d_CA = print_eea_table(phi_CA, e_CA)
    print(f"    * Khóa công khai CA: (N_CA = {N_CA}, e_CA = {e_CA})")
    print(f"    * Khóa bí mật CA   : (d_CA = {d_CA})")
    
    print(f"\n[BƯỚC 2] CA ký số chứng thực định danh của Người dùng A (M = {M}):")
    S_CA = pow(M, d_CA, N_CA)
    print(f"    * Chữ ký số CA: S_CA = M^d_CA mod N_CA = {M}^{d_CA} mod {N_CA} = {S_CA}")
    print(f"    * Chứng chỉ số cấp cho A: Cert_A = (ID = {M}, Signature = {S_CA})")
    
    print(f"\n[BƯỚC 3] Người dùng B xác minh chứng chỉ số bằng khóa công khai của CA:")
    V = pow(S_CA, e_CA, N_CA)
    print(f"    * V = S_CA^e_CA mod N_CA = {S_CA}^{e_CA} mod {N_CA} = {V}")
    print(f"    * So sánh: V == M ({V} == {M}) -> {V == M}")
    print(f"    ===> KẾT LUẬN: Chứng chỉ của Người dùng A là HOÀN TOÀN HỢP LỆ VÀ XÁC THỰC!")
    
    print("\n" + "=" * 75)
    print("USTH FINAL EXAM 2024-2025 - EXERCISE 1.3: QUY TRÌNH TRAO ĐỔI EMAIL BẢO MẬT (PKI)")
    print("=" * 75)
    print("  Bước 1: Người dùng A gửi Email kèm theo Cert_A cho Người dùng B.")
    print("  Bước 2: Người dùng B dùng khóa công khai của CA (e_CA, N_CA) để xác thực Cert_A,")
    print("          thu được khóa công khai đã được CA chứng thực của A: (e_A, N_A).")
    print("  Bước 3: Người dùng B soạn thư hồi đáp, tạo khóa phiên đối xứng k_session,")
    print("          mã hóa nội dung thư bằng k_session, và mã hóa k_session bằng khóa công khai của A (e_A).")
    print("  Bước 4: Người dùng A nhận thư, dùng khóa bí mật của mình d_A để giải mã lấy k_session,")
    print("          sau đó giải mã toàn bộ nội dung thư.")
    print("=" * 75)


def custom_ca_sign(p_CA: int, q_CA: int, e_CA: int, M: int):
    N_CA = p_CA * q_CA
    phi_CA = (p_CA - 1) * (q_CA - 1)
    d_CA = pow(e_CA, -1, phi_CA)
    S_CA = pow(M, d_CA, N_CA)
    V = pow(S_CA, e_CA, N_CA)
    print("\n" + "=" * 70)
    print("CUSTOM CA RSA DIGITAL SIGNATURE / CERTIFICATE")
    print("=" * 70)
    print(f"CA Primes: p_CA = {p_CA}, q_CA = {q_CA}")
    print(f"CA Modulus N_CA = {N_CA}, phi(N_CA) = {phi_CA}")
    print(f"CA Public Exponent e_CA: {e_CA}")
    print(f"CA Private Key d_CA:     {d_CA}")
    print(f"User Message/ID to Sign: M = {M}")
    print(f"CA Digital Signature:    S_CA = M^d_CA mod N_CA = {M}^{d_CA} mod {N_CA} = {S_CA}")
    print(f"Verification:            V = S_CA^e_CA mod N_CA = {V}")
    print(f"Valid Signature:         {V == M}")
    print("=" * 70)


def custom_input():
    print("\n" + "=" * 70)
    print("CUSTOM EXAM INPUT: CA RSA DIGITAL CERTIFICATE")
    print("=" * 70)
    try:
        val_p = input("Enter CA prime p [e.g. 227]: ").strip()
        p = int(val_p, 0) if val_p else 227
        val_q = input("Enter CA prime q [e.g. 149]: ").strip()
        q = int(val_q, 0) if val_q else 149
        val_e = input("Enter CA public exponent e [e.g. 25537]: ").strip()
        e = int(val_e, 0) if val_e else 25537
        val_m = input("Enter message/ID to sign M [e.g. 56]: ").strip()
        m = int(val_m, 0) if val_m else 56
        custom_ca_sign(p, q, e, m)
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}")


run_demo = solve_exam_2024


if __name__ == "__main__":
    import sys

    if "--demo" in sys.argv or (not sys.stdin.isatty() and len(sys.argv) <= 1):
        solve_exam_2024()
        sys.exit(0)

    # Support CLI arguments: python pki_rsa_certificate.py 227 149 25537 56
    if len(sys.argv) > 4 and sys.argv[1] not in ("-i", "--interactive", "--custom"):
        try:
            p_arg = int(sys.argv[1], 0)
            q_arg = int(sys.argv[2], 0)
            e_arg = int(sys.argv[3], 0)
            m_arg = int(sys.argv[4], 0)
            custom_ca_sign(p_arg, q_arg, e_arg, m_arg)
            sys.exit(0)
        except Exception:
            pass

    if sys.stdin.isatty():

        custom_input()

    else:

        run_demo()