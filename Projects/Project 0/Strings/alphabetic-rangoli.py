#!/usr/bin/env python3


import string

def print_rangoli(_n):
    _alpha = string.ascii_lowercase
    _list = []

    for i in range(_n):
        _str = "-".join(_alpha[i:_n])
        _list.append(_str[::-1] + _str[1:])

    _new_width = len(_list[0])

    for i in range(_n-1, 0, -1):
        print(_list[i].center(_new_width, "-"))
    for i in range(_n):
        print(_list[i].center(_new_width, "-"))

def main():
    print_rangoli(int(input("Enter maximum length: ")))

if __name__ == '__main__':
    print("===========[ PROGRAM: Prints an Alphabetic Rangoli ]============")
    main()