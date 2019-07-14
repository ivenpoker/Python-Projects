#!/usr/bin/env  python3

"""
    Program purpose: Validates characters in the string.
    Program Author : Happi Yvan
    Author email   : ivensteinpoker@gmail.com
"""

def process(_str):

        print("\n\tIs there any alphanumeric character: ", end="")
        if any(c.isalnum() for c in _str):
            print("True")
        else:
            print("False")

        print("\tIs there any alphabetic character: ", end="")
        if any(c.isalpha() for c in _str):
            print("True")
        else:
            print("False")

        print("\tIs there any digit: ", end="")
        if any(c.isdigit() for c in _str):
            print("True")
        else:
            print("False")

        print("\tIs there is any lower character: ", end="")
        if any(c.islower() for c in _str):
            print("True")
        else:
            print("False")

        print("\tIs there any upper character: ", end="")
        if any(c.isupper() for c in _str):
            print("True")
        else:
            print("False")

        # print(any(c.isalnum() for c in _str))
        # print(any(c.isalpha() for c in _str))
        # print(any(c.isdigit() for c in _str))
        # print(any(c.islower() for c in _str))
        # print(any(c.isupper() for c in _str))

def main():
    user_str = input("\n\tEnter a string: ")
    process(user_str)

if __name__ == "__main__":
    print("\n\t==========[ PROGRAM: Validate string ]========")
    main()