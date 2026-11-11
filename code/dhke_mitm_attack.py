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
        print(f"\n[+] Public Domain Parameters: Prime p = {p}, Generator alpha = {alpha}")
        print("-" * 65)

    # Step 1: Alice generates private key 'a' and public key A
    A = pow(alpha, a, p)
    if verbose:
        print(f"[1] Alice generates private a = {a}")
        print(f"    Alice calculates public key A = alpha^a mod p = {alpha}^{a} mod {p} = {A}")
        print(f"    --> Alice attempts to send A = {A} to Bob...")

    # Step 2: Eve intercepts A and sends E_1 to Bob
    E1 = pow(alpha, e1, p)
    if verbose:
        print(f"[2] Eve intercepts A = {A}!")
        print(f"    Eve chooses private e1 = {e1}, computes public E1 = {alpha}^{e1} mod {p} = {E1}")
        print(f"    --> Eve forwards E1 = {E1} to Bob (Bob thinks it comes from Alice).")

    # Step 3: Bob receives E_1, generates private 'b' and public key B
    B = pow(alpha, b, p)
    if verbose:
        print(f"[3] Bob receives E1 = {E1}")
        print(f"    Bob chooses private b = {b}")
        print(f"    Bob calculates public key B = alpha^b mod p = {alpha}^{b} mod {p} = {B}")
        print(f"    --> Bob attempts to send B = {B} to Alice...")

    # Step 4: Eve intercepts B and sends E_2 to Alice
    E2 = pow(alpha, e2, p)
    if verbose:
        print(f"[4] Eve intercepts B = {B}!")
        print(f"    Eve chooses private e2 = {e2}, computes public E2 = {alpha}^{e2} mod {p} = {E2}")
        print(f"    --> Eve forwards E2 = {E2} to Alice (Alice thinks it comes from Bob).")

    # Step 5: Key Computation
    K_Alice = pow(E2, a, p)
    K_Eve_Alice = pow(A, e2, p)

    K_Bob = pow(E1, b, p)
    K_Eve_Bob = pow(B, e1, p)

    if verbose:
        print("-" * 65)
        print("[5] Shared Key Derivations:")
        print(f"    Alice calculates key: K_AE = (E2)^a mod p = {E2}^{a} mod {p} = {K_Alice}")
        print(f"    Eve calculates key  : K_AE = A^(e2) mod p = {A}^{e2} mod {p} = {K_Eve_Alice}")
        print(f"    --> Eve and Alice share session key: {K_Alice} (Match: {K_Alice == K_Eve_Alice})")
        print()
        print(f"    Bob calculates key  : K_EB = (E1)^b mod p = {E1}^{b} mod {p} = {K_Bob}")
        print(f"    Eve calculates key  : K_EB = B^(e1) mod p = {B}^{e1} mod {p} = {K_Eve_Bob}")
        print(f"    --> Eve and Bob share session key  : {K_Bob} (Match: {K_Bob == K_Eve_Bob})")
        print("-" * 65)
        print(f"[=>] Notice: Alice thinks she is talking to Bob using key {K_Alice},")
        print(f"     while Bob thinks he is talking to Alice using key {K_Bob}.")
        print(f"     Eve holds BOTH keys, completely compromising confidentiality and integrity!\n")

    return K_Alice, K_Bob


def custom_input():
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
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}")


if __name__ == "__main__":
    import sys

    # Direct interactive flag: python dhke_mitm_attack.py -i
    if len(sys.argv) > 1 and sys.argv[1] in ("-i", "--interactive", "--custom"):
        custom_input()
        sys.exit(0)

    print("=" * 65)
    print("DEMO: MAN-IN-THE-MIDDLE ATTACK ON DIFFIE-HELLMAN KEY EXCHANGE")
    print("=" * 65)

    # Parameters from Exam 2025-2026:
    print("1. Exam 2025-2026 Diffie-Hellman MitM Simulation:")
    p = 27361
    alpha = 7
    # Student ID: 56
    a_alice = 56
    b_bob = 140
    e1_eve = 33
    e2_eve = 77

    simulate_dhke_mitm(p, alpha, a_alice, b_bob, e1_eve, e2_eve, verbose=True)

    # Session 8 Slide 18: Oscar Active MitM Attack
    print("=" * 65)
    print("2. Session 8 Slide 18: Oscar Active MitM Attack:")
    print("   Parameters: p = 467, alpha = 2, a = 228, b = 57, o = 16")
    print("=" * 65)
    p_s8 = 467
    alpha_s8 = 2
    a_s8 = 228
    b_s8 = 57
    o_s8 = 16
    simulate_dhke_mitm(p_s8, alpha_s8, a_s8, b_s8, o_s8, o_s8, verbose=True)

    # Interactive prompt if user runs directly in terminal
    if sys.stdin.isatty():
        print("-" * 65)
        c = input("[?] Enter custom parameters for your exam? [y/N]: ").strip().lower()
        if c in ("y", "yes"):
            custom_input()

