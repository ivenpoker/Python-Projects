#!/usr/bin/env python3

def print_formatted(_int):
    _len = len("{:b}".format(_int))+1
    for _x in range(_int):
        _dec = "{:d}".format(_x+1).rjust(_len, " ")
        _oct = _dec + "{:o}".format(_x+1).rjust(_len, " ")
        _hex = _oct + "{:X}".format(_x+1).rjust(_len, " ")
        _bin = _hex + "{:b}".format(_x+1).rjust(_len, " ")
        print(_bin[1:])

def main():
    n = int(input("Enter maximum digits: "))
    print_formatted(n)


if __name__ == '__main__':
    print("\n============[ PROGRAM: Decimal, Octal, Hexadecimal and Binary display ]==========")
    main()