#!/usr/bin/env   python3

"""
    Program purpose: Swaps the case of alphabetic characters in a string.
    Program author : Happi Yvan
    Program email  : ivensteinpoker@gmail.com
"""

def swap_case(some_str):
    cnt = 0
    str_swap = ""
    for ind in range(len(some_str)):
        if str.islower(some_str[ind]):
            str_swap += str.upper(some_str[ind])
        else:
            str_swap += str.lower(some_str[ind])
    return str_swap


def main():
    user_str = input("\tEnter a string: ")
    print("\tCases swapped : %s\n" % swap_case(user_str))


if __name__ == "__main__":
    print("\n\t==============[ PROGRAM: Swap character cases ]=============\n")
    main()
