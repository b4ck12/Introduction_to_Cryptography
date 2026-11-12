# -*- coding: utf-8 -*-
"""
Script: solve_des_sbox.py
Description: Solves Exercise 1 (DES S1-Box Lookup) for any Student ID.
Default ID: 23BA14056 (Last 3 digits: 056 -> x = 56).
"""
import sys

# Standard DES S-Box S1 Table (4 rows x 16 columns)
S1_BOX = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]

def solve_des_s1(student_id_str="23BA14056"):
    digits = "".join(filter(str.isdigit, student_id_str))
    last_3 = int(digits[-3:]) if len(digits) >= 3 else int(digits)
    x = last_3 % 64
    bin_6bit = f"{x:06b}"
    
    # Outer bits: b1 (MSB) and b6 (LSB) define Row r
    row_bin = bin_6bit[0] + bin_6bit[5]
    row = int(row_bin, 2)
    
    # Inner 4 bits: b2, b3, b4, b5 define Column c
    col_bin = bin_6bit[1:5]
    col = int(col_bin, 2)
    
    # Lookup in S1
    val = S1_BOX[row][col]
    val_bin_4bit = f"{val:04b}"
    
    print("=" * 75)
    print("USTH FINAL EXAM 2025-2026 - EXERCISE 1: DES S1-BOX LOOKUP (LỜI GIẢI TỰ LUẬN)")
    print("=" * 75)
    print(f"[BƯỚC 1] Xác định số nguyên x từ 3 chữ số cuối mã sinh viên:")
    print(f"    * Mã sinh viên       : {student_id_str}")
    print(f"    * 3 chữ số cuối      : {last_3:03d}")
    print(f"    * Số nguyên đầu vào x: x = {last_3} mod 64 = {x}")
    
    print(f"\n[BƯỚC 2] Biểu diễn số nguyên x dưới dạng nhị phân 6 bit:")
    print(f"    {x}_10 = ({bin_6bit})_2 = (b1 b2 b3 b4 b5 b6)")
    print(f"    Chi tiết từng bit: b1={bin_6bit[0]}, b2={bin_6bit[1]}, b3={bin_6bit[2]}, b4={bin_6bit[3]}, b5={bin_6bit[4]}, b6={bin_6bit[5]}")

    print(f"\n[BƯỚC 3] Xác định chỉ số Hàng r và Cột c trong bảng S1:")
    print(f"    * Hàng r (ghép bit ngoài cùng b1 b6):")
    print(f"        r = (b1 b6)_2 = ({row_bin})_2 = {int(row_bin[0])*2} + {int(row_bin[1])} = {row}  ===> HÀNG {row}")
    print(f"    * Cột c (ghép 4 bit ở giữa b2 b3 b4 b5):")
    print(f"        c = (b2 b3 b4 b5)_2 = ({col_bin})_2 = {int(col_bin[0])*8} + {int(col_bin[1])*4} + {int(col_bin[2])*2} + {int(col_bin[3])} = {col} ===> CỘT {col}")

    print(f"\n[BƯỚC 4] Tra cứu giá trị trong bảng S1-Box tại tọa độ (Hàng {row}, Cột {col}):")
    print(f"    S1[{row}][{col}] = {val} (Thập phân)")

    print(f"\n[BƯỚC 5] Đổi giá trị đầu ra sang hệ nhị phân 4 bit:")
    print(f"    {val}_10 = ({val_bin_4bit})_2")
    print(f"    ===> ĐÁP SỐ BÀI 1: Đầu ra của hộp S1 là {val} (Nhị phân: {val_bin_4bit}_2)")
    print("=" * 75)
    return {
        "x": x,
        "bin_6bit": bin_6bit,
        "row": row,
        "col": col,
        "val_dec": val,
        "val_bin": val_bin_4bit
    }

def custom_input():
    print("\n" + "=" * 60)
    print("CUSTOM EXAM INPUT: DES S1-BOX LOOKUP")
    print("=" * 60)
    try:
        user_in = input("Enter Student ID (e.g. 23BA14056) or integer (0-63) or 6-bit binary [default: 23BA14056]: ").strip()
        if not user_in:
            user_in = "23BA14056"
        solve_des_s1(user_in)
    except (ValueError, KeyboardInterrupt, EOFError) as err:
        print(f"[-] Input error or cancelled: {err}")


def run_demo():
    solve_des_s1("23BA14056")


if __name__ == "__main__":
    import sys

    # Run demo test suite only if explicitly requested or in non-interactive test pipe
    if "--demo" in sys.argv or (not sys.stdin.isatty() and len(sys.argv) <= 1):
        solve_des_s1("23BA14056")
        sys.exit(0)

    # If CLI arg provided: python des_sbox_lookup.py 23BA14099
    if len(sys.argv) > 1 and not sys.argv[1].startswith("-"):
        solve_des_s1(sys.argv[1])
        sys.exit(0)

    # Default: Open directly into Custom Exam Input prompt
    if sys.stdin.isatty():
        custom_input()
    else:
        run_demo()