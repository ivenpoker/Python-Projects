#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Sorts a list alphabetically in a dictionary.                      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 10, 2019                                                 #
#                                                                                          #
############################################################################################

import random

main_prefix = "list"

def random_list(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

def random_dict(low: int, high: int, size: int) -> dict:
    if size < 0:
        raise ValueError('Invalid specified size. Must be > 0')
    rand_keys = [f'{main_prefix}{i}' for i in range(size)]
    rand_values = [random_list(low=low, high=high, size=int(size/2)) for _ in range(size)]

    return {k: v for (k, v) in zip(rand_keys, rand_values)}

def sorts_list_in_dict(some_dict: dict) -> dict:
    return {k: sorted(v, reverse=False) for (k, v) in zip(some_dict.keys(), some_dict.values())}

if __name__ == "__main__":
    new_dict = random_dict(low=0, high=10, size=10)
    print(f'   New dictionary: {new_dict}')
    print(f'Sorted dictionary: {sorts_list_in_dict(some_dict=new_dict)}')
