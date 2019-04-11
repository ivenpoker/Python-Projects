#!/usr/bin/env python3

#: Program purpose:
#               Read two integers from STDIN and print three lines where:
#:              The first line contains the sum of the two numbers.
#:              The second line contains the difference of the two numbers (first - second).
#:              The third line contains the product of the two numbers.
#:
#: Program Author: Happi Yvan <ivensteinpoker@gmail.com>
#: Program Date  : 11/04/2019 (mm/dd/yyyy)

def process(int1, int2):
    print(int1 + int2)
    print(int1 - int2)
    print(int1 * int2)

def main():
    int1 = int(input())
    int2 = int(input())
    process(int1, int2)

if __name__ == '__main__':
    main()