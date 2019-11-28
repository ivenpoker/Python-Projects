#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Sums all the values in the dictionary.                            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 28, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_dict(low: int, high: int, size: int) -> dict:
    if size < 0:
        raise ValueError(f'Invalid size ({size}) of dictionary')
    rand_keys = [random.randint(low, high) for _ in range(size)]
    rand_values = [random.randint(low, high) for _ in range(size)]

    return {k: v for (k, v) in zip(rand_keys, rand_values)}

def sum_all_items(some_dict: dict) -> int:
    return sum(some_dict.values())

if __name__ == "__main__":

    new_dict = random_dict(low=0, high=20, size=10)
    print(f' Generated dictionary: {new_dict}')
    print(f'Sum of values in dict: {sum_all_items(some_dict=new_dict)}')

