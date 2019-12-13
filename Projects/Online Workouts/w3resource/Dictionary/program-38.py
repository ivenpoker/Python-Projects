#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Matches the key and values in two dictionaries.                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 13, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_dict(low: int, high: int, size: int, init_str: str) -> dict:
    if low < 0:
        raise ValueError("Invalid 'low' argument")
    if high < 0:
        raise ValueError("Invalid 'high' argument")
    if size < 0:
        raise ValueError("Invalid 'size' argument")
    new_dict, init_int = {}, random.randint(low, high)
    rand_keys, rand_values = [], [random.randint(low, high) for _ in range(size)]
    for _ in range(size):
        rand_keys.append(f'{init_str}{init_int}')
        init_int = random.randint(low, high)

    return {k: v for (k, v) in zip(rand_keys, rand_values)}

def match_key_values_in_dict(some_dict_A: dict, some_dict_B: dict) -> dict:
    match = {}
    if len(some_dict_A) < len(some_dict_B):
        for (k, v) in zip(some_dict_A.keys(), some_dict_A.values()):
            if (k in some_dict_B.keys()) and (some_dict_A[k] == some_dict_B[k]):
                match[k] = v
    else:
        for (k, v) in zip(some_dict_B.keys(), some_dict_B.values()):
            if (k in some_dict_A.keys()) and (some_dict_B[k] == some_dict_A[k]):
                match[k] = v
    return match


if __name__ == "__main__":

    dict_A = random_dict(low=0, high=10, size=4, init_str='key')
    dict_B = random_dict(low=0, high=10, size=4, init_str='key')

    print(f'Generated dictionary A: {dict_A}')
    print(f'Generated dictionary B: {dict_B}')

    matched_items = match_key_values_in_dict(some_dict_A=dict_A, some_dict_B=dict_B)

    print(f'Generated matched items in dictionaries: {matched_items}')
    print('-' * 70)

    dict_A = {'key1': 1, 'key2': 3, 'key3': 2}
    dict_B = {'key1': 1, 'key2': 2}

    print(f'Hard coded dictionary A: {dict_A}')
    print(f'Hard coded dictionary B: {dict_B}')

    matched_items = match_key_values_in_dict(some_dict_A=dict_A, some_dict_B=dict_B)
    print(f'Generated matched items in dictionaries: {matched_items}')
