#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Appends two list.                                                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 12, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def create_int_list(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

def append_lists(list_A: list, list_B: list) -> list:
    return list_A + list_B

if __name__ == "__main__":
    list_1 = create_int_list(low=1, high=10, size=5)
    list_2 = create_int_list(low=2, high=15, size=6)

    print(f'List A: {list_1}')
    print(f'List B: {list_2}')

    print(f'After appending list: {append_lists(list_A=list_1, list_B=list_2)}')
