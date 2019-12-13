#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Counts the number of items in a dictionary value that is a list.  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 13, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_dict(low: int, high: int, size: int, init_str: str) -> dict:
    if low < 0:
        raise ValueError('Invalid value for low')
    if high < 0:
        raise ValueError('Invalid value for high')
    if size < 0:
        raise ValueError('Invalid value for size')
    init_int = 0
    rand_keys = []
    for _ in range(size):
        rand_keys.append(f'{init_str}{init_int}')
        init_int += 1
    rand_values = []
    for _ in range(size):
        temp_val = [random.randint(low, high) for _ in range(random.randint(low, high))]
        rand_values.append(temp_val)

    return {k: v for (k, v) in zip(rand_keys, rand_values)}

def count_number_of_items(some_dict: dict) -> int:
    return sum(map(len, some_dict.values()))

if __name__ == "__main__":
    rand_dict = random_dict(low=0, high=10, size=15, init_str='key')
    print(f'Generated dict: {rand_dict}')
    print(f'Number of items in dictionary: {count_number_of_items(some_dict=rand_dict)}')
