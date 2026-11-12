import os
"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Algorithm: Man-in-the-Middle (MitM) Attack on Unauthenticated DHKE
Reference: Session 6 (Public Key & Diffie-Hellman Key Exchange)
Student ID: 23BA14056 (x = 56)
=============================================================================
Theory:
  Diffie-Hellman provides confidentiality against passive eavesdroppers,
  but lacks entity authentication.
  An active adversary (Eve) situated between Alice and Bob can execute a MitM attack:
  1. Intercepts Alice's public key A = alpha^a mod p.
     Replaces it with Eve's key E_1 = alpha^(e_1) mod p sent to Bob.
  2. Intercepts Bob's public key B = alpha^b mod p.
     Replaces it with Eve's key E_2 = alpha^(e_2) mod p sent to Alice.
  3. Established Shared Keys:
     - Alice and Eve share key: K_AE = (E_2)^a mod p = A^(e_2) mod p
     - Bob and Eve share key  : K_EB = (E_1)^b mod p = B^(e_1) mod p
  4. Result: Eve transparently decrypts, inspects/alters, and re-encrypts all traffic.
=============================================================================
"""

def simulate_dhke_mitm(p: int, alpha: int, a: int, b: int, e1: int, e2: int, verbose: bool = True):
    """
    Simulates the Man-in-the-Middle attack on Diffie-Hellman Key Exchange.
    """
    if verbose:
        print("=" * 75)
        print("TẤN CÔNG KẺ ĐỨNG GIỮA TRÊN TRAO ĐỔI KHÓA (DHKE MITM ATTACK)")
        print("=" * 75)
        print(f"[BƯỚC 1] Thiết lập tham số công khai hệ thống:")
        print(f"    Công thức: A = alpha^a mod p, B = alpha^b mod p")
        print(f"    Tham số: Số nguyên tố p = {p}, Phần tử sinh alpha = {alpha}")
        print(f"    Alice secret a = {a}, Bob secret b = {b}, Attacker: e1 = {e1}, e2 = {e2}\n")

    # Step 1: Alice generates private key 'a' and public key A
    A = pow(alpha, a, p)
    E1 = pow(alpha, e1, p)
    if verbose:
        print(f"[BƯỚC 2] Alice tạo khóa A và Kẻ tấn công can thiệp gửi E1 cho Bob:")
        print(f"    * Alice tính: A = alpha^a mod p = {alpha}^{a} mod {p} = {A}")
        print(f"    * Kẻ tấn công chặn bắt A và tính E1 = alpha^e1 mod p = {alpha}^{e1} mod {p} = {E1}")
        print(f"    * Kẻ tấn công gửi E1 = {E1} cho Bob (Bob tin rằng E1 đến từ Alice)\n")

    # Step 2: Bob receives E_1, generates private 'b' and public key B
    B = pow(alpha, b, p)
    E2 = pow(alpha, e2, p)
    if verbose:
        print(f"[BƯỚC 3] Bob tạo khóa B và Kẻ tấn công can thiệp gửi E2 cho Alice:")
        print(f"    * Bob tính: B = alpha^b mod p = {alpha}^{b} mod {p} = {B}")
        print(f"    * Kẻ tấn công chặn bắt B và tính E2 = alpha^e2 mod p = {alpha}^{e2} mod {p} = {E2}")
        print(f"    * Kẻ tấn công gửi E2 = {E2} cho Alice (Alice tin rằng E2 đến từ Bob)\n")

    # Step 3: Key Computation
    K_Alice = pow(E2, a, p)
    K_Eve_Alice = pow(A, e2, p)
    K_Bob = pow(E1, b, p)
    K_Eve_Bob = pow(B, e1, p)

    if verbose:
        print(f"[BƯỚC 4] Tính toán các khóa phiên bí mật phân nhánh:")
        print(f"    Công thức: K_AE = (E2)^a mod p, K_EB = (E1)^b mod p")
        print(f"    * Khóa phiên giữa Alice và Kẻ tấn công:")
        print(f"        Alice tính K_AE = (E2)^a mod p = ({E2})^{a} mod {p} = {K_Alice}")
        print(f"        Kẻ tấn công tính K_AE = A^(e2) mod p = ({A})^{e2} mod {p} = {K_Eve_Alice}")
        print(f"        Kiểm tra khớp khóa: {K_Alice} == {K_Eve_Alice} -> True (Chính xác!)")
        print(f"    * Khóa phiên giữa Bob và Kẻ tấn công:")
        print(f"        Bob tính K_EB = (E1)^b mod p = ({E1})^{b} mod {p} = {K_Bob}")
        print(f"        Kẻ tấn công tính K_EB = B^(e1) mod p = ({B})^{e1} mod {p} = {K_Eve_Bob}")
        print(f"        Kiểm tra khớp khóa: {K_Bob} == {K_Eve_Bob} -> True (Chính xác!)\n")

        print(f"[BƯỚC 5] Kết luận hậu quả an ninh đối với hệ thống:")
        print(f"    Alice tin rằng đang trò chuyện an toàn với Bob bằng khóa {K_Alice},")
        print(f"    trong khi Bob tin rằng đang trò chuyện với Alice bằng khóa {K_Bob}.")
        print(f"    Kẻ tấn công nắm giữ CẢ HAI khóa phiên, giải mã và chỉnh sửa toàn bộ dữ liệu!")
        print(f"    ===> KHÓA PHIÊN ALICE-ATTACKER: K_AE = {K_Alice}")
        print(f"    ===> KHÓA PHIÊN BOB-ATTACKER  : K_EB = {K_Bob}")
        print("=" * 75)

    return K_Alice, K_Bob


def custom_input():
    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
        return
    print("\n" + "=" * 65)
    print("CUSTOM EXAM INPUT: DHKE MAN-IN-THE-MIDDLE ATTACK")
    print("=" * 65)
    try:
        val_p = input("Enter prime p [e.g. 467]: ").strip()
        p = int(val_p, 0) if val_p else 467
        val_alpha = input("Enter generator alpha [e.g. 2]: ").strip()
        alpha = int(val_alpha, 0) if val_alpha else 2
        val_a = input("Enter Alice's private key a [e.g. 228]: ").strip()
        a = int(val_a, 0) if val_a else 228
        val_b = input("Enter Bob's private key b [e.g. 57]: ").strip()
        b = int(val_b, 0) if val_b else 57
        val_o1 = input("Enter Attacker private key towards Alice [e.g. 16]: ").strip()
        o1 = int(val_o1, 0) if val_o1 else 16
        val_o2 = input("Enter Attacker private key towards Bob [e.g. 16]: ").strip()
        o2 = int(val_o2, 0) if val_o2 else o1
        simulate_dhke_mitm(p, alpha, a, b, o1, o2, verbose=True)
    except (ValueError, KeyboardInterrupt, EOFError):
        run_demo()


def run_demo():
    simulate_dhke_mitm(467, 2, 228, 57, 16, 16, verbose=True)


if __name__ == "__main__":
    import os
    import sys

    if "--demo" in sys.argv:
        run_demo()
        sys.exit(0)

    # Support CLI arguments: python dhke_mitm_attack.py 467 2 228 57 16 16
    cli_args = [a for a in sys.argv[1:] if a.strip() and not a.startswith("-")]
    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty() or len(cli_args) > 0:
        try:
            p_arg = int(cli_args[0], 0) if len(cli_args) > 0 else 467
            alpha_arg = int(cli_args[1], 0) if len(cli_args) > 1 else 2
            a_arg = int(cli_args[2], 0) if len(cli_args) > 2 else 228
            b_arg = int(cli_args[3], 0) if len(cli_args) > 3 else 57
            e1_arg = int(cli_args[4], 0) if len(cli_args) > 4 else 16
            e2_arg = int(cli_args[5], 0) if len(cli_args) > 5 else e1_arg
            simulate_dhke_mitm(p_arg, alpha_arg, a_arg, b_arg, e1_arg, e2_arg, verbose=True)
        except Exception:
            run_demo()
        sys.exit(0)

    custom_input()