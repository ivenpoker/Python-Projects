#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Adds a key to the dictionary.                                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 27, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_dict(low: int, high: int, size: int) -> dict:
    if size < 0:
        raise ValueError(f'Invalid size [{size}] for dictionary')
    key_data = [random.randint(low, high) for _ in range(size)]
    value_data =  [random.randint(low, high) for _ in range(size)]

    return {k: v for (k, v) in zip(key_data, value_data)}

def add_item(main_dict: dict, key_val: tuple):
    main_dict[key_val[0]] = key_val[1]

if __name__ == "__main__":
    new_dict = random_dict(low=0, high=10, size=5)
    print(f'Generated dictionary is: {new_dict}')
    new_key_val = (0, 3)
    print(f'Adding key -> {new_key_val[0]} and value -> {new_key_val[1]}')

    add_item(main_dict=new_dict, key_val=new_key_val)
    print(f'After adding: {new_dict}')