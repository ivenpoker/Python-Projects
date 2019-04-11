#!/usr/bin/env python3

#: Prorgam Purpose:
#:          Given a comma seperated list of integers, program generates
#:          a list and a tuple out of them and print them.
#:
#: Program Author: Happi Yvan <ivensteinpoker@gmail.com>
#: Program Date  : 11/04/2019


def main():
    data = input("Enter comma separated integers: ").strip().split(", ")
    print("List : ", list(data))
    print("Tuple: ", tuple(data))

if __name__ == '__main__':
    main()