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
    
    print("=" * 60)
    print("USTH FINAL EXAM 2025-2026 - EXERCISE 1: DES S1-BOX LOOKUP")
    print("=" * 60)
    print(f"Student ID:                 {student_id_str}")
    print(f"Last 3 digits:              {last_3:03d}")
    print(f"Input integer x:            {last_3} mod 64 = {x}")
    print(f"6-bit Binary:               {bin_6bit} (b1={bin_6bit[0]}, b2={bin_6bit[1]}, b3={bin_6bit[2]}, b4={bin_6bit[3]}, b5={bin_6bit[4]}, b6={bin_6bit[5]})")
    print(f"Row r (b1, b6):             '{row_bin}' -> Row {row}")
    print(f"Column c (b2..b5):          '{col_bin}' -> Column {col}")
    print(f"S1-Box Output (decimal):    {val}")
    print(f"S1-Box Output (4-bit bin):  {val_bin_4bit}")
    print("=" * 60)
    return {
        "x": x,
        "bin_6bit": bin_6bit,
        "row": row,
        "col": col,
        "val_dec": val,
        "val_bin": val_bin_4bit
    }

if __name__ == "__main__":
    sid = sys.argv[1] if len(sys.argv) > 1 else "23BA14056"
    solve_des_s1(sid)
