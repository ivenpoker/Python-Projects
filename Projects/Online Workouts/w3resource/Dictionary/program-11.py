#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Multiply all values in a dictionary.                              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 28, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_dictionary(low: int, high: int, size: int) -> dict:
    if size < 0:
        raise ValueError(f'Invalid size [{size}] for dictionary')
    key_list = [random.randint(low, high) for _ in range(size)]
    value_list = [random.randint(low, high) for _ in range(size)]

    return {k: v for (k, v) in zip(key_list, value_list)}

def multi_all_values(some_dict: dict) -> int:
    temp = 1
    for key in some_dict.keys():
        temp *= some_dict[key]
    return temp

if __name__ == "__main__":
    new_dict = random_dictionary(low=0, high=20, size=10)
    print(f'  Generated dictionary data: {new_dict}')
    print(f'After multiplying all items: {multi_all_values(some_dict=new_dict)}')
