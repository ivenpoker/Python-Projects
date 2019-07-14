#!/usr/bin/env python3

"""
    Program Purpose: Prints the 'Hacker Rank' logo
    Program Author : Happi Yvan
    Author email   : ivensteinpoker@gmail.com
"""

def print_log(_int):
    for i in range(_int):
        print(("H" * i).rjust(_int-1) + "H" + ("H"*i).ljust(_int-1))
    for i in range(_int + 1):
        print(("H" * _int).center(_int*2)+(_int*"H").center(_int*6))
    for i in range((_int+1) // 2):
        print(("H" * _int * 5).center(_int * 6))
    for i in range(_int+1):
        # print(("H"*_int*5).center(_int * 6))
        print(("H" * _int).center(_int * 2) + (_int * "H").center(_int * 6))
    for i in range(_int):
        print((("H" * (_int-i-1)).rjust(_int) + "H" + ("H" * (_int-i-1)).ljust(_int)).rjust(_int * 6))

if __name__ == "__main__":
    _int = int(input())
    print_log(_int)
