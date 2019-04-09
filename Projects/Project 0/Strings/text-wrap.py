#!/usr/bin/env python3

"""
    Program Purpose: Gets a string from console, wraps it based on user
                     specific width.
    Program Author : Happi Yvan
    Author email   : ivensteinpoker@gmail.com
"""


def text_wrap(_some_str, _width):
    for ind in range(len(_some_str)):
        if ind % _width == 0:
            print("\n\t%s" % (_some_str[ind]), end="")
        else:
            print(_some_str[ind], end="")

def main():
    user_str = input("\n\tEnter a string: ")
    width = int(input("\tEnter wrap width: "))
    text_wrap(user_str, width)


if __name__ == "__main__":
    print("\n\t=========[ PROGRAM: Wraps a user defined string, based on with ]=======")
    main()
    print()