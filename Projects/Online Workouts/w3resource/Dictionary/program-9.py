#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Iterates over dictionary items.                                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 28, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_dict(low: int, high: int, size: int) -> dict:
    if size < 0:
        raise ValueError(f'Invalid size [{size}] for dictionary')
    rand_keys = [random.randint(low, high) for _ in range(size)]
    rand_values = [random.randint(low, high) for _ in range(size)]

    return {k: v for (k, v) in zip(rand_keys, rand_values)}

def display_dict(some_dict: dict) -> None:
    for (k, v) in some_dict.items():
        print(f'Key-[{k}] | Value-[{v}]')

if __name__ == "__main__":
    main_dict = random_dict(low=0, high=20, size=25)
    print(f'Generated dictionary: {main_dict}')

    display_dict(some_dict=main_dict)
