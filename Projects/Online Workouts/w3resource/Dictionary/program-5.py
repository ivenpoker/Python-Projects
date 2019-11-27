#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Iterate over a dictionary                                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 27, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def generate_dict(low: int, high: int, size: int) -> dict:
    if size < 0:
        raise ValueError(f'Invalid size [{size}] for dictionary')
    key_items = [random.randint(low, high) for _ in range(size)]
    value_items = [random.randint(low, high) for _ in range(size)]

    return {k: v for (k, v) in zip(key_items, value_items)}

def iterate_over(some_dict: dict):
    for (k, v) in zip(some_dict.keys(), some_dict.values()):
        print(f'key [{k}] --> value [{v}]')

if __name__ == "__main__":
    new_dict = generate_dict(low=0, high=10, size=10)
    print(f'Generated dictionary: {new_dict}')

    # iterate over dictionary, printing key-value pairs
    iterate_over(some_dict=new_dict)