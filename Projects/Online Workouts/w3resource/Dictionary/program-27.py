#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Converts a list into a nested dictionary keys.                    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 10, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def rand_list(low: int, high: int, size: int) -> list:
    if size < 0:
        raise ValueError('Invalid size for new list. Must be > 0')
    return [random.randint(low, high) for _ in range(size)]

def list_to_nested_dict(some_list: list) -> dict:
    new_dict = current_dict = {}
    for val in some_list:
        current_dict[val] = {}
        current_dict = current_dict[val]
    return new_dict

if __name__ == "__main__":
    new_list = rand_list(low=0, high=15, size=10)
    print(f'New random list: {new_list}')
    print(f' Generated dict: {list_to_nested_dict(some_list=new_list)}')