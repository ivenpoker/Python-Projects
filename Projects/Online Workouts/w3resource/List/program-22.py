#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Find the index of a specified element in list.                    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 11, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def obtain_user_search_key(input_mess: str, low: int, high: int) -> int:
    is_valid, user_data = False, int(-1)
    while is_valid is False:
        try:
            user_data = int(input(input_mess))
            if user_data not in range(low, high):
                raise ValueError(f'Invalid input. Must be in range [{low}, {high})')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def generate_int_list(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

if __name__ == "__main__":

    new_list_data = generate_int_list(low=1, high=10, size=15)
    print(f'Generated data: {new_list_data}')

    int_key = obtain_user_search_key(input_mess='Enter integer to find index (first): ', low=1, high=11)
    if new_list_data.index(int_key) >= 0:
        print(f'Data at index {int_key} is: {new_list_data[int_key]}')
    else:
        print(f'Invalid index!')

