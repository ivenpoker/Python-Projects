#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Creates and displays all combinations of values, selecting each   #
#                        value from a different key in a dictionary.                       #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 10, 2019                                                 #
#                                                                                          #
############################################################################################

import random
import itertools

main_alpha = 'abcdefghijklmnopqrstuvwxyz'

def random_letter() -> str:
    return main_alpha[random.randint(0, len(main_alpha)-1)]

def get_random_dict(low: int, high: int, size: int) -> dict:
    if size < 0:
        raise ValueError('Invalid specified size for dictionary. Must be > 0')
    rand_keys = [random_letter() for _ in range(size)]
    rand_values = [[random.randint(low, high) for _ in range(int(size/2))] for _ in range(size)]

    return {k: v for (k, v) in zip(rand_keys, rand_values)}

def get_all_combination_of_keys(some_dict: dict) -> list:
    comb_list = []
    for combo in itertools.product(*[some_dict[k] for k in sorted(some_dict.keys())]):
        comb_list.append(combo)
    return comb_list


if __name__ == "__main__":
    new_dict = get_random_dict(low=0, high=10, size=5)
    print(f'New dictionary: {new_dict}')

    key_comb = get_all_combination_of_keys(some_dict=new_dict)
    print(f'Combinations for keys: {key_comb}')
