#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Checks whether a given string is number or not using Lambda.      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 04, 2020                                                 #
#                                                                                          #
############################################################################################

from typing import Callable

def obtain_user_data(input_mess) -> str:
    user_data, valid = '', False
    while not valid:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Oops, data needed')
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def LAMBDA_is_string_int(some_str: str) -> Callable:
    return lambda: some_str.replace('.', '', 1).isdigit()

if __name__ == "__main__":
    main_str = obtain_user_data('Enter some string to check: ')
    test_func = LAMBDA_is_string_int(some_str=main_str)

    print(f"Is string a number: {'YES' if test_func() else 'NO'}")

