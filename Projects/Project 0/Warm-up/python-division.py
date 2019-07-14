#!/usr/bin/env      python3

#: Program Purpose:
#:              Read two integers 'a' and 'b' print two lines.
#:              The first line should contain integer division, a // b.
#:              The second line should contain float division,  a / b .
#:
#: Program Author: Happi Yvan <ivensteinpoker@gmail.com>
#: Program Date  : 11/04/2019  (mm/dd/yyyy)


def process(int1, int2):
    print(int1 // int2)
    print(int1 / int2)

def main():
    int1 = int(input())
    int2 = int(input())

    process(int1, int2)

if __name__ == '__main__':
    main()
