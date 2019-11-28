#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Finds the max and min values in a dictionary.                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 28, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_dict(low: int, high: int, size: int) -> dict:
    if size < 0:
        raise ValueError(f'Invalid size ({size}) for dictionary')
    rand_keys = [random.randint(low, high) for _ in range(size)]
    rand_values = [random.randint(low, high) for _ in range(size)]

    return {k: v for (k, v) in zip(rand_keys, rand_values)}

def max_min_dict_values(main_dict: dict) -> dict:
    return {'max': max(main_dict.values()), 'min': min(main_dict.values())}

if __name__ == "__main__":
    new_dict = random_dict(low=0, high=30, size=10)
    print(f'New dictionary: {new_dict}')

    max_min = max_min_dict_values(main_dict=new_dict)
    print(f"Max value: {max_min['max']}")
    print(f"Min value: {max_min['min']}")