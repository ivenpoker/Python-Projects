#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Merges two dictionaries.                                          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 28, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_dictionary(low: int, high: int, size: int) -> dict:
    if size < 0:
        raise ValueError(f'Invalid size [{size}] for dictionary')
    rand_keys = [random.randint(low, high) for _ in range(size)]
    rand_values = [random.randint(low, high) for _ in range(size)]

    return {k: v for (k, v) in zip(rand_keys, rand_values)}

def merge_dicts(dict_A: dict, dict_B: dict) -> dict:
    new_dict = dict_A.copy()
    new_dict.update(dict_B)
    return new_dict

if __name__ == "__main__":

    rand_dict_A = random_dictionary(low=0, high=10, size=6)
    rand_dict_B = random_dictionary(low=5, high=15, size=6)

    print(f'Random dictionary A: {rand_dict_A}')
    print(f'Random dictionary B: {rand_dict_B}')
    print(f'After merging dicts: {merge_dicts(dict_A=rand_dict_A, dict_B=rand_dict_B)}')

