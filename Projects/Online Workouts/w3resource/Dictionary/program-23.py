#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Combines values in python list of dictionaries.                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 10, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def get_random_dict(low: int, high: int, size: int) -> dict:
    if size < 0:
        raise ValueError('Invalid specified size for dictionary. Must be > 0')
    rand_key = [random.randint(low, high) for _ in range(size)]
    rand_values = [random.randint(low, high) for _ in range(size)]

    return {k: v for (k, v) in zip(rand_key, rand_values)}

def combine_values(list_dicts: list) -> dict:
    if len(list_dicts) == 0:
        return dict()
    new_dict = dict()
    for sub_dict in list_dicts:
        for (k, v) in zip(sub_dict.keys(), sub_dict.values()):
            if k in new_dict.keys():
                new_dict[k] += v
            else:
                new_dict[k] = v
    return new_dict


if __name__ == "__main__":
    new_dict_A = get_random_dict(low=0, high=10, size=8)
    new_dict_B = get_random_dict(low=0, high=10, size=8)

    main_list = [new_dict_A, new_dict_B]

    print(f'New random dict: {new_dict_A}')
    print(f'New random dict: {new_dict_B}')
    print(f'Combined dictionaries: {combine_values(list_dicts=main_list)}')
