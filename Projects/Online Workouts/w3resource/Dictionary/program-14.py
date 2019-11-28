#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Sorts dictionary by keys.                                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 28, 2019                                                 #
#                                                                                          #
############################################################################################

import random
import operator

def random_dict(low: int, high: int, size: int) -> dict:
    if size < 0:
        raise ValueError(f'Invalid size ({size}) for dictionary')
    rand_keys = [random.randint(low, high) for _ in range(size)]
    rand_values = [random.randint(low, high) for _ in range(size)]

    return {k: v for (k, v) in zip(rand_keys, rand_values)}

def sort_dict_by_key(some_dict: dict) -> dict:
    return dict(sorted(some_dict.items(), key=operator.itemgetter(0), reverse=False))

if __name__ == "__main__":
    main_dict = random_dict(low=0, high=20, size=10)
    print(f'Generated dictionary: {main_dict}')
    print(f'   Sorted dictionary: {sort_dict_by_key(some_dict=main_dict)}')



