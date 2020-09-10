#!/usr/bin/env python3

#######################################################################################
#                                                                                     #
#       Program purpose: Determines if a string is a pangram                          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 10, 2020                                           #
#                                                                                     #
#######################################################################################


def is_pangram(main_str: str) -> bool:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return len(list(filter(lambda char: char not in main_str.lower(), alphabet))) == 0


if __name__ == "__main__":
    print(is_pangram("James is the king of the jungle"))
    print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
    print(is_pangram("Cwm fjord bank glyphs vext quiz is a pangram"))
