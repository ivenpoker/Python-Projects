#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Obtain (print) unique values from a dictionary.                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 10, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def get_random_dict(low: int, high: int, size: int) -> dict:
    if size < 0:
        raise ValueError('Invalid size for new dictionary. Must be > 0')
    rand_keys = [random.randint(low, high) for _ in range(size)]
    rand_values = [random.randint(low, high) for _ in range(size)]

    return {k: v for (k, v) in zip(rand_keys, rand_values)}

def dict_empty(some_dict: dict) -> bool:
    return len(some_dict.keys()) == 0

def get_unique_values(some_dict: dict) -> list:
    if dict_empty(some_dict=some_dict):
        return []
    unique_values = []
    for val in some_dict.values():
        if val not in unique_values:
            unique_values.append(val)

    return unique_values

def get_unique_values_from_dicts_list(list_of_dicts: list) -> list:
    lists_of_uniques = []
    for sub_dict in list_of_dicts:
        if not dict_empty(some_dict=sub_dict):
            lists_of_uniques.append(get_unique_values(some_dict=sub_dict))
    return lists_of_uniques

if __name__ == "__main__":

    new_dict = get_random_dict(low=0, high=20, size=10)
    print(f'  New dictionary is: {new_dict}')
    print(f'Original values are: {list(new_dict.values())}')
    print(f'  Unique values are: {get_unique_values(some_dict=new_dict)}')

    print()
    print('-' * 15, ' [New Operations] ', '-' * 15)

    dicts_list = [
        get_random_dict(low=0, high=10, size=10),
        get_random_dict(low=0, high=10, size=10),
        get_random_dict(low=0, high=10, size=10),
    ]
    print(f'List of dictionaries: {dicts_list}')
    print(f'List of uniques: {get_unique_values_from_dicts_list(list_of_dicts=dicts_list)}')