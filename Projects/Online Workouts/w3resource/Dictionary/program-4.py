#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Determines if a certain key is found in dictionary.               #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 28, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def generate_dict(low: int, high: int, size: int) -> dict:
    if size < 0:
        raise ValueError(f'Invalid size [{size}] of array')
    key_items = [random.randint(low, high) for _ in range(size)]
    value_items = [random.randint(low, high) for _ in range(size)]

    return {k: v for (k, v) in zip(key_items, value_items)}

def random_list(low: int, high: int, size: int) -> list:
    if size < 0:
        raise ValueError(f'Invalid size [{size}] of array')
    return [random.randint(low, high) for _ in range(size)]


def key_in_dict(some_key: int, main_dict: dict) -> bool:
    return some_key in main_dict.keys()

if __name__ == "__main__":
    new_dict = generate_dict(low=0, high=20, size=10)
    print(f'Generated dictionary: {new_dict}')

    # search for 5 random key values.
    search_keys = random_list(low=0, high=20, size=5)

    for temp_key in search_keys:
        print(f"Is '{temp_key}' found in list: "
              f"{key_in_dict(some_key=temp_key, main_dict=new_dict)}")

