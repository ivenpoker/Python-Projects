#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Select the odd items of a list.                                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_int_list(low: int, high: int, list_size: int) -> list:
    if list_size < 0:
        raise ValueError('Invalid list size')
    return [random.randint(low, high) for _ in range(list_size)]

def get_odd_items(some_list: list) -> list:
    return some_list[::2]

if __name__ == "__main__":
    new_list_data = random_int_list(low=0, high=15, list_size=10)
    print(f'Generated list data: {new_list_data}')
    print(f'  Odd items in list: {get_odd_items(some_list=new_list_data)}')