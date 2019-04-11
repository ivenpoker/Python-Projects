#!/usr/bin/env  python3

#: Program Purpose:
#:              Given an integer, we perform the following conditional actions:
#:              If  is odd, print Weird
#:              If  is even and in the inclusive range of  to , print Not Weird
#:              If  is even and in the inclusive range of  to , print Weird
#:              If  is even and greater than , print Not Weird
#:
#: Program Author: Happi Yvan <ivensteinpoker@gmail.com>
#: Written Date:   11/04/2019


def process(val):
    if int(val) % 2 != 0:
        return "Weird"
    elif int(val) % 2 == 0 and (2 <= val <= 5):
        return "Not Weird"
    elif int(val) % 2 == 0 and (6 <= val <= 20):
        return "Weird"
    elif int(val) % 2 == 0 and val > 20:
        return "Not Weird"


def main():
    val = int(input("Enter an integer: "))
    resp = process(val)
    print(resp)

if __name__ == '__main__':
    main()