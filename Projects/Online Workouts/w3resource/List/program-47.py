#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Insert an element before each element of a list.                  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def obtain_user_pre_input(input_mess: str) -> str:
    user_data, is_valid = '', False
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Oops, input needed!')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def random_int_list(low: int, high: int, list_size: int) -> list:
    if list_size < 0:
        raise ValueError('Invalid list size')
    return [random.randint(low, high) for _ in range(list_size)]

def do_insertion(some_list: list, pre_data: str) -> list:
    new_list_data = []
    for (i, val) in enumerate(some_list):
        new_list_data.append(pre_data)
        new_list_data.append(val)
    return new_list_data

if __name__ == "__main__":

    new_list = random_int_list(low=0, high=10, list_size=15)
    print(f'Generated list: {new_list}')

    pre_ind_data = obtain_user_pre_input(input_mess='Enter some data to insert within: ')
    new_data = do_insertion(some_list=new_list, pre_data=pre_ind_data)

    print(f'New list data: {new_data}')