#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Inserts a given string at the beginning of all items in a list.   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 23, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def obtain_user_string_data(input_mess: str) -> str:
    is_valid, user_data = False, ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Oops, data needed')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def rand_int_list(low: int, high: int, size: int) -> list:
    if size < 0:
        raise ValueError('Invalid size of list')
    return [random.randint(low, high) for _ in range(size)]

def do_processing(main_list: list, append_str: str) -> list:
    temp_list = []
    for temp in main_list:
        temp_list.append(append_str + str(temp))
    return temp_list


if __name__ == "__main__":

    rand_list = rand_int_list(low=0, high=20, size=5)
    print(f'Generate list: {rand_list}')
    user_str_data = obtain_user_string_data(input_mess='Enter some string data to append: ')
    new_list_data = do_processing(main_list=rand_list, append_str=user_str_data)
    print(f'New list data: {new_list_data}')
