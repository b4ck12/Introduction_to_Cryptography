import os
"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Algorithm: Birthday Attack & Collision Probability Analysis
Reference: Session 7 (Hash Functions, Slides 29-32)
Student ID: 23BA14056 (x = 56)
=============================================================================
Theory:
  Given an m-bit hash function with output space size n = 2^m:
  1. The probability that k random inputs yield AT LEAST ONE collision:
         p = 1 - PROD_{i=1}^{k-1} (1 - i / n)
  2. Taylor Series / Exponential Approximation:
         p ~ 1 - exp(-k^2 / (2 * n))
  3. Number of hashes required for probability p:
         k ~ sqrt(2 * n * ln(1 / (1 - p)))
  4. For 50% chance of collision (p = 0.5):
         k ~ sqrt(2 * ln(2)) * 2^(m/2) ~ 1.1774 * 2^(m/2)
  ==> An m-bit hash function offers only m/2 bits of collision resistance!
=============================================================================
"""

import math
import random
from typing import Dict, Tuple

def collision_prob_exact(k: int, n: int) -> float:
    """Computes exact collision probability for k items in space n."""
    if k > n:
        return 1.0
    prob_no_collision = 1.0
    for i in range(1, k):
        prob_no_collision *= (1.0 - i / n)
    return 1.0 - prob_no_collision


def collision_prob_approx(k: int, n: int) -> float:
    """Computes collision probability using exponential approximation."""
    exponent = -(k * k) / (2.0 * n)
    return 1.0 - math.exp(exponent)


def required_samples(m_bits: int, p: float = 0.5) -> float:
    """Computes number of samples k needed to achieve collision probability p."""
    n = 2 ** m_bits
    return math.sqrt(2 * n * math.log(1 / (1 - p)))


def simulate_birthday_collision(bits: int) -> int:
    """Simulates random hashing until a collision occurs in a (bits)-bit space."""
    seen = set()
    mask = (1 << bits) - 1
    count = 0
    while True:
        count += 1
        val = random.getrandbits(bits)
        if val in seen:
            return count
        seen.add(val)


def run_demo():
    print("=" * 70)
    print("DEMO: BIRTHDAY ATTACK & HASH COLLISION ANALYSIS")
    print("=" * 70)

    # 1. Standard Course Hash Comparison Table
    print("\n1. Hash Collision Security Levels (50% Collision Bound):")
    print(f"{'Hash Algorithm':<15} | {'Digest Size (m)':<15} | {'Preimage Resistance':<20} | {'Collision Bound (k ~ 2^(m/2))'}")
    print("-" * 80)
    hash_specs = [
        ("MD5", 128),
        ("SHA-1", 160),
        ("SHA-224", 224),
        ("SHA-256", 256),
        ("SHA-384", 384),
        ("SHA-512", 512),
    ]
    for name, bits in hash_specs:
        sec = f"2^{bits} operations"
        col = f"2^{bits//2} operations (~{1.1774 * (2**(bits//2)):.2e})"
        print(f"{name:<15} | {bits:<15} | {sec:<20} | {col}")

    # 2. Classic Birthday Paradox: 365 Days
    print("\n2. Classic Birthday Paradox (Days in Year n = 365):")
    print(f"{'People (k)':<12} | {'Exact Collision Prob':<22} | {'Approx Collision Prob'}")
    print("-" * 60)
    for k in [5, 10, 15, 20, 23, 30, 40, 50, 57]:
        p_ex = collision_prob_exact(k, 365)
        p_ap = collision_prob_approx(k, 365)
        marker = " <== (50% threshold reached at k=23!)" if k == 23 else ""
        print(f"k = {k:<8} | {p_ex * 100:>18.4f}% | {p_ap * 100:>19.4f}%{marker}")

    # 3. Monte Carlo Simulation on 16-bit hash (n = 65,536)
    sim_bits = 16
    expected_k = 1.1774 * (2 ** (sim_bits / 2))
    print(f"\n3. Monte Carlo Simulation on {sim_bits}-bit hash (n = 2^{sim_bits} = {2**sim_bits:,}):")
    print(f"   Theoretical 50% collision count k ~ {expected_k:.1f} trials")
    trials = 5
    print(f"   Running {trials} independent empirical trials:")
    results = []
    for t in range(trials):
        c = simulate_birthday_collision(sim_bits)
        results.append(c)
        print(f"     Trial {t+1}: Collision found at attempt {c}")
    avg_c = sum(results) / len(results)
    print(f"   Average trials to collision: {avg_c:.1f} (Close to theoretical {expected_k:.1f})")


def custom_input():
    import os, sys
    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
        return
    print("\n" + "=" * 65)
    print("CUSTOM EXAM INPUT: BIRTHDAY ATTACK & COLLISION BOUND")
    print("=" * 65)
    try:
        val_m = input("Enter hash output length in bits m [e.g. 64]: ").strip()
        m = int(val_m, 0) if val_m else 64
        val_lambda = input("Enter target collision probability lambda [0.0 - 1.0, default 0.5]: ").strip()
        prob = float(val_lambda) if val_lambda else 0.5
        
        # k ~ sqrt(2 * ln(1/(1-lambda))) * 2^(m/2)
        coeff = math.sqrt(2 * math.log(1 / (1 - prob)))
        k_bound = coeff * (2 ** (m / 2))
        print(f"\n[+] Hash bit length m = {m} bits (Total output space n = 2^{m})")
        print(f"[+] Target probability lambda = {prob * 100}%")
        print(f"[+] Birthday Bound Formula: k ~ sqrt(2 * ln(1/(1 - lambda))) * 2^(m/2)")
        print(f"    Coefficient: {coeff:.4f}")
        print(f"[=>] Number of messages needed k ~ {coeff:.4f} * 2^{m//2} ~ {k_bound:.3e} messages")
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}. Using default.")
        try:
            run_demo()
        except Exception:
            pass


def solve_birthday_detailed(m: int, prob: float = 0.5):
    print("=" * 75)
    print("TẤN CÔNG SINH NHẬT & GIỚI HẠN VA CHẠM HÀM BĂM (BIRTHDAY ATTACK)")
    print("=" * 75)
    print(f"[BƯỚC 1] Thiết lập bài toán & Công thức xấp xỉ Birthday Paradox:")
    print(f"    Công thức: k ≈ √(2 · ln(1 / (1 - λ))) · 2^(m/2)")
    print(f"    Độ phức tạp kháng va chạm: C_hash = 2^(m/2) phép tính băm")
    print(f"    Tham số: Độ dài băm m = {m} bits, Xác suất va chạm mục tiêu λ = {prob}\n")

    coeff = math.sqrt(2 * math.log(1 / (1 - prob))) if prob < 1.0 else 0
    k_bound = coeff * (2 ** (m / 2))
    n_space = 2 ** m

    print(f"[BƯỚC 2] Bảng tính số lượng mẫu thử nghiệm cần thiết (Sample Complexity):")
    print(f"    {'Thông số':<30} | {'Giá trị tính toán'}")
    print("    " + "-" * 60)
    print(f"    {'Không gian đầu ra n = 2^m':<30} | 2^{m} (~ {n_space:.3e})")
    print(f"    {'Hệ số √(2·ln(1/(1-λ)))':<30} | {coeff:.4f}")
    print(f"    {'Độ an toàn hiệu dụng (Bits)':<30} | {m // 2} bits")
    print(f"    {'Số mẫu k cần băm (xấp xỉ)':<30} | {k_bound:.3e} ({int(k_bound):,} bản tin)")
    print("    " + "-" * 60)

    print(f"\n[BƯỚC 3] Kết luận giới hạn bảo mật hàm băm:")
    print(f"    Số lượng bản tin cần thiết để va chạm với xác suất {prob * 100:.1f}% là k ≈ {k_bound:.3e}")
    print(f"    ===> GIỚI HẠN SỐ MẪU CẦN BĂM: k ≈ {k_bound:.3e} (2^{m//2} bits)")
    print("=" * 75)


if __name__ == "__main__":
    import sys
    if "--demo" in sys.argv or (not sys.stdin.isatty() and len(sys.argv) <= 1):
        run_demo()
        sys.exit(0)

    # CLI argument support: python birthday_attack_collision.py 64 0.5
    cli_args = [a for a in sys.argv[1:] if a.strip() and not a.startswith("-")]
    if len(cli_args) >= 1:
        try:
            m_arg = int(cli_args[0], 0)
            p_arg = float(cli_args[1]) if len(cli_args) > 1 else 0.5
            solve_birthday_detailed(m_arg, p_arg)
            sys.exit(0)
        except Exception:
            pass

    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
    else:
        try:
            custom_input()
        except (EOFError, KeyboardInterrupt):
            run_demo()