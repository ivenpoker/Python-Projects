#!/usr/bin/env python3

#: Program Purpose:
#:          Read an integer N. For all non-negative integers i < N
#:          print i * i.
#:
#: Program Author: Happi Yvan <ivensteinpoker@gmail.com
#: Program Date  : 11/04/2019 (mm/dd/yyyy)

def process(int_val):
    for x in range(int_val):
        print(x * x)

def main():
    val = int(input())
    process(val)

if __name__ == '__main__':
    main()