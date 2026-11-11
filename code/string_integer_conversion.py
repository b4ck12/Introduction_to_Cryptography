"""
=============================================================================
Course: Introduction to Cryptography (USTH)
Algorithm: String to Integer & Integer to String Big-Endian Conversion
Reference: Session 6 (Public Key), Lab 3 Exercise 1 & Exercise 2
Student ID: 23BA14056 (x = 56)
=============================================================================
Theory:
  Public-key cryptosystems (RSA, ElGamal) operate on elements of Z_n (numbers).
  To encrypt text, strings are mapped to integers using Big-Endian base-256:
      M = SUM_{i=0}^{k-1} ord(s[i]) * 256^{k - 1 - i}
  To decrypt, the integer is decomposed back into ASCII characters:
      c_{k-1-i} = (M // 256^i) % 256
=============================================================================
"""

def string_to_int(text: str, verbose: bool = True) -> int:
    """
    Converts a string to a Big-Endian integer (Lab 3 Exercise 1).
    """
    byte_vals = [ord(c) for c in text]
    k = len(byte_vals)
    result = 0

    if verbose:
        print(f"\n[+] String to Integer Conversion for '{text}':")
        print(f"    String length k = {k} characters")
        print(f"{'Idx':<4} | {'Char':<6} | {'ASCII':<8} | {'Hex':<6} | {'Weight (256^pow)':<18} | {'Contribution':<20}")
        print("-" * 70)

    for i, (char, val) in enumerate(zip(text, byte_vals)):
        pwr = k - 1 - i
        weight = 256 ** pwr
        term = val * weight
        result += term
        if verbose:
            print(f"{i:<4} | {char:<6} | {val:<8} | 0x{val:02X}{'':<2} | 256^{pwr:<2} ({weight:<10}) | {term:<20}")

    if verbose:
        print("-" * 70)
        print(f"[=>] Total Integer M = {result} (Hex: 0x{result:X})\n")

    return result


def int_to_string(number: int, verbose: bool = True) -> str:
    """
    Converts a Big-Endian integer back to an ASCII string (Lab 3 Exercise 2).
    """
    if number == 0:
        return "\x00"

    temp = number
    byte_list = []
    while temp > 0:
        byte_list.append(temp % 256)
        temp //= 256
    byte_list.reverse()

    chars = [chr(b) for b in byte_list]
    result_str = "".join(chars)

    if verbose:
        print(f"\n[+] Integer to String Conversion for M = {number} (0x{number:X}):")
        print(f"{'Byte':<6} | {'ASCII Code':<12} | {'Hex':<6} | {'Character':<10}")
        print("-" * 40)
        for idx, b in enumerate(byte_list):
            print(f"Byte {idx:<2} | {b:<12} | 0x{b:02X}{'':<2} | '{chr(b)}'")
        print("-" * 40)
        print(f"[=>] Recovered String: '{result_str}'\n")

    return result_str


if __name__ == "__main__":
    print("=" * 65)
    print("DEMO: STRING <-> INTEGER CONVERSION (LAB 3 EX 1 & EX 2)")
    print("=" * 65)

    # 1. Lab 3 Ex 1: Convert "flow" to integer
    word = "flow"
    m_val = string_to_int(word, verbose=True)
    print(f"Lab 3 Ex 1 Result: '{word}' -> M = {m_val} (Expected: 1718382455, Match: {m_val == 1718382455})")

    # 2. Lab 3 Ex 2: Convert integer back to string
    recovered_word = int_to_string(m_val, verbose=True)
    print(f"Lab 3 Ex 2 Result: M = {m_val} -> '{recovered_word}' (Match: {recovered_word == word})")

    # 3. Student ID Check
    student_msg = "ID056"
    m_id = string_to_int(student_msg, verbose=False)
    rec_id = int_to_string(m_id, verbose=False)
    print(f"\nStudent ID Message: '{student_msg}' -> Int: {m_id} -> Recovered: '{rec_id}' (Match: {rec_id == student_msg})")
