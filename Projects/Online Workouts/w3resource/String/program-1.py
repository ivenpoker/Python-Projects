#!/usr/bin/env  python3

######################################################################################
#                                                                                    #
#       Program purpose: Computes the length of a string provided by the user.       #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                       #
#       Creation Date  : October 10, 2019                                            #
#                                                                                    #
######################################################################################

def find_string_length(main_str: str):
    return len(main_str)

if __name__ == "__main__":
    some_str = input('Enter some string to compute length: ')
    print(f"Length of \'{some_str}\' is: {find_string_length(main_str=some_str)} character(s) long.")