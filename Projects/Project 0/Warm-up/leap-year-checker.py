#!/usr/bin/env python3

#: Program Purpose:
#:          Given a year, program checks if the year is a leap year or not.
#:
#: Program Authror: Happi Yvan <ivensteinpoker@gmail.com>
#: Program Date   : 11/04/2019


def process(year):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return "True"
    else:
        return "False"

def main():
    year = int(input())
    print(process(year))


if __name__ == '__main__':
    main()
