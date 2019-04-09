#!/usr/bin/env      python3

"""
    Program purpose: Splits a string on ' ' and join same string with '-'
    Program author : Happi Yvan
    Author email   :
"""

def split_and_join(some_str):
    _list = some_str.split(' ')
    return '-'.join(_list)

def main():
    data = input("\n\tEnter a string: ")
    data_joined = split_and_join(data)
    print("\tJoined data   : %s" % data_joined)

if __name__ == "__main__":
    print("\n\t=========[ PROGRAM: Split a string on ' ' and join on '-']======")
    main()
