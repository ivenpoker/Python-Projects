#!/usr/bin/env python3

"""
    Program Purpose: Change the character at a particular index
    Program Author : Happi Yvan
    Author Email   : ivensteinpoker@gmail.com
"""

def mutate(some_str, ind, char):
    return some_str[:ind] + char + some_str[ind+1:]

def main():
    user_str = input("\n\tEnter a string: ")
    ind = input("\tEnter index to mutate: ")
    char = input("\tEnter new character: ")
    print("\n\tMutated string: %s" % (mutate(user_str, int(ind), char)))


if __name__ == "__main__":
    print("\n\t=======[ PROGRAM: Mutates an index in string ]========")
    main()