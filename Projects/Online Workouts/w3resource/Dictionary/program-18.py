#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Determines if a dictionary is empty.                              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 10, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_dict(low: int, high: int, size: int) -> dict:
    if size < 0:
        raise ValueError('Invalid size for dictionary. Must be > 0')
    rand_keys = [random.randint(low, high) for _ in range(size)]
    rand_values = [random.randint(low, high) for _ in range(size)]

    return {k: v for (k, v) in zip(rand_keys, rand_values)}

def is_dict_empty_A(some_dict: dict) -> bool:
    return len(some_dict.keys()) == 0 and len(some_dict.values()) == 0

def is_dict_empty_B(some_dict: dict) -> bool:
    return not bool(some_dict)

if __name__ == "__main__":
    dict_A = {}
    dict_B = random_dict(low=0, high=20, size=10)

    print(f"Dictionary A -> {dict_A} | Is empty: {'YES' if is_dict_empty_A(some_dict=dict_A) else 'NO'}")
    print(f"Dictionary B -> {dict_B} | Is empty: {'YES' if is_dict_empty_A(some_dict=dict_B) else 'NO'}")