#!/usr/bin/env  python3

#: Program Purpose:
#:          Given user names, prints them back in reverse order
#:
#: Program Author : Happi Yvan <ivensteinpoker@gmail.com>
#: Program Date   : 11/04/2019 (mm/dd/yyyy)


def main():
    data = list(input("Enter first and last name: ").split(" "))
    list.reverse(data)
    print("Reversed name: ", end="")
    print(' '.join(data))

if __name__ == '__main__':
    main()