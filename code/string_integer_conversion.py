import os
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
        print("=" * 75)
        print("CHUYỂN ĐỔI XÂU KÝ TỰ SANG SỐ NGUYÊN (STRING TO INTEGER BIG-ENDIAN)")
        print("=" * 75)
        print(f"[BƯỚC 1] Thiết lập cơ số Big-Endian base-256 & Bảng mã ASCII:")
        print(f"    Công thức: M = ∑_{{i=0}}^{{k-1}} ord(s[i]) · 256^{{k - 1 - i}}")
        print(f"    Tham số: Chuỗi ký tự = '{text}', Độ dài k = {k} ký tự\n")
        print(f"[BƯỚC 2] Bảng vết phân rã trọng số từng byte (Conversion Trace Table):")
        print(f"    {'Idx':<4} | {'Ký tự':<6} | {'Mã ASCII':<10} | {'Mã Hex':<8} | {'Trọng số 256^pow':<20} | {'Đóng góp vào M'}")
        print("    " + "-" * 75)

    for i, (char, val) in enumerate(zip(text, byte_vals)):
        pwr = k - 1 - i
        weight = 256 ** pwr
        term = val * weight
        result += term
        if verbose:
            print(f"    {i:<4} | {char:<6} | {val:<10} | 0x{val:02X}{'':<4} | 256^{pwr:<2} ({weight:<12}) | {term}")

    if verbose:
        print("    " + "-" * 75)
        print(f"\n[BƯỚC 3] Kết luận số nguyên Big-Endian thu được:")
        print(f"    Số nguyên hệ thập phân (Decimal) : {result}")
        print(f"    Số nguyên hệ thập lục phân (Hex) : 0x{result:X}")
        print(f"    ===> SỐ NGUYÊN ĐẠI DIỆN: M = {result}")
        print("=" * 75)

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


def custom_input():
    import os, sys
    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
        return
    print("\n" + "=" * 65)
    print("CUSTOM EXAM INPUT: STRING <-> INTEGER CONVERTER")
    print("=" * 65)
    print("Choose conversion direction:")
    print("  [1] String to Big-Endian Integer (M = SUM ord(c_i) * 256^(k-1-i))")
    print("  [2] Integer to String (ASCII characters)")
    try:
        choice = input("Select [1/2, default 1]: ").strip()
        if choice == "2":
            val_int = input("Enter integer M [e.g. 1718382455]: ").strip()
            num = int(val_int, 0) if val_int else 1718382455
            int_to_string(num, verbose=True)
        else:
            txt = input("Enter text string [e.g. flow]: ")
            if not txt:
                txt = "flow"
            string_to_int(txt, verbose=True)
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}. Using default.")
        try:
            run_demo()
        except Exception:
            pass


def run_demo():
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


if __name__ == "__main__":
    import sys

    # Run demo test suite only if explicitly requested or in non-interactive test pipe
    if "--demo" in sys.argv or (not sys.stdin.isatty() and len(sys.argv) <= 1):
        run_demo()
        sys.exit(0)

    # Support CLI arguments: python string_integer_conversion.py "flow"
    if len(sys.argv) > 1 and not sys.argv[1].startswith("-"):
        arg = sys.argv[1]
        if arg.isdigit():
            int_to_string(int(arg), verbose=True)
        else:
            string_to_int(arg, verbose=True)
        sys.exit(0)

    # Default: Open directly into Custom Exam Input prompt
    if os.environ.get("GUI_MODE") == "1" or not sys.stdin.isatty():
        run_demo()
    else:
        try:
            custom_input()
        except (EOFError, KeyboardInterrupt):
            run_demo()