#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Flattens a shallow list.                                          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 11, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def create_int_list(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

def flatten_lists(main_list: list) -> list:
    flat_list = []
    for sub_list in main_list:
        for x in sub_list:
            flat_list.append(x)
    return flat_list


if __name__ == "__main__":

    list_A = create_int_list(low=1, high=5, size=5)
    list_B = create_int_list(low=2, high=8, size=6)
    list_C = create_int_list(low=1, high=10, size=4)

    print(f'List A: {list_A}')
    print(f'List B: {list_B}')
    print(f'List C: {list_C}')
    print(f'After flattening list: {flatten_lists(main_list=[list_A, list_B, list_C])}')
