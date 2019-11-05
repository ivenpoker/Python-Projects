#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Count number of non-empty substrings of a given string.           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 5, 2019                                                  #
#                                                                                          #
############################################################################################

def obtain_user_input(input_mess: str) -> str:
    is_valid, user_data = False, ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Oops! Data is needed')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def number_of_substrings(some_str: str) -> int:
    str_len = len(some_str)
    return int(str_len * (str_len + 1) / 2)

if __name__ == "__main__":
    user_input = obtain_user_input(input_mess='Enter some string: ')
    print(f'Number of substrings: {number_of_substrings(some_str=user_input)}')


