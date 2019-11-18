#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Converts a pair of values into a sorted unique array                           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def generate_list_tuples(low: int, high: int, list_size: int) -> list:
    if list_size < 0:
        raise ValueError('Invalid size for list')
    return [(random.randint(low, high), random.randint(low, high)) for _ in range(list_size)]

def convert_value_pairs(tuple_list: list) -> list:

    main_list = []
    for (x, v) in tuple_list:
        if x not in main_list:
            main_list.append(x)
        if v not in main_list:
            main_list.append(v)
    return sorted(main_list)

if __name__ == "__main__":

    list_tuple = generate_list_tuples(low=0, high=20, list_size=10)
    print(f'Generated pairs: {list_tuple}')
    convert_value_pairs(tuple_list=list_tuple)
    print(f'Sorted list: {convert_value_pairs(tuple_list=list_tuple)}')