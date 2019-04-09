#!/usr/bin/env python3

"""
    Program Purpose: Displays a nice :) welcome message.
    Program Author : Happi Yvan
    Author  email  : ivensteinpoker@gmail.com
"""

def print_door_mat(_n, _m):
    _dot_x = 1
    _dash = "-"

    for _x in range(int(_n / 2)+1):
        if not _x == 0:
            print((".|." * _dot_x).center(_m, _dash))
            _dot_x += 2

    print("WELCOME".center(_m, _dash))
    _dot_x -= 2

    for _x in range(int(_n / 2)):
        if not _x == _n-1:
            print((".|." * _dot_x).center(_m, _dash))
            _dot_x -= 2

if __name__ == "__main__":
    print("\n==============[ PROGRAM: Prints a Welcome door mat ]=============")
    length = int(input("\nEnter length: "))
    width  = int(input("Enter width : "))
    print()
    print_door_mat(length, width)