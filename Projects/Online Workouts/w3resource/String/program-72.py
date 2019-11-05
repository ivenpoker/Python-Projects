#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Removes all consecutive duplicates from a given string.           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 5, 2019                                                  #
#                                                                                          #
############################################################################################

import itertools

def obtain_data_from_user(input_mess: str) -> str:
    is_valid, user_data = False, ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Please enter some string to work with')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def do_processing(main_str: str) -> str:
    return ''.join(i for i, _ in itertools.groupby(main_str))

if __name__ == "__main__":
    main_data = obtain_data_from_user(input_mess='Enter some string data: ')
    print(f'New string: {do_processing(main_str=main_data)}')
