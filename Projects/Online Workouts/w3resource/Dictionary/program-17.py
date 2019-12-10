#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Remove duplicates from a dictionary.                              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 10, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_dict(low: int, high: int, key_size: int) -> dict:
    if key_size < 0:
        raise ValueError(f'Invalid key size for new dict. Must be > 0')
    rand_keys = [random.randint(low, high) for _ in range(key_size)]
    rand_values = [random.randint(low, high) for _ in range(key_size)]

    return {k: v for (k, v) in zip(rand_keys, rand_values)}

def remove_dict_duplicate(main_dict: dict) -> dict:
    unique_values = set(list(main_dict.values()))
    unique_dict = dict()

    for value in unique_values:
        for (k, v) in zip(main_dict.keys(), main_dict.values()):
            if v == value:
                unique_dict[k] = value
                break

    return unique_dict

if __name__ == "__main__":

    new_dict = random_dict(low=0, high=2, key_size=10)
    print(f'Generated dict -> {new_dict} | {new_dict.values()} | size -> {len(new_dict)}')

    filtered_dict = remove_dict_duplicate(main_dict=new_dict)
    print(f' Filtered dict -> {filtered_dict} | {filtered_dict.values()} | size -> {len(new_dict)}')
