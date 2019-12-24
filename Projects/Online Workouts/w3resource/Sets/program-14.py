#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Find the length of a set.                                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 24, 2019                                                 #
#                                                                                          #
############################################################################################

from random import randint

def random_set_data(low: int, high: int, size: int) -> set:
    if size < 0:
        raise ValueError(f"Invalid size ({size}). Must be > 0")
    return set([randint(low, high) for _ in range(size)])

if __name__ == "__main__":
    new_set = random_set_data(low=0, high=10, size=15)
    print(f'New set dat: {new_set}')
    print(f'Length of new set: {len(new_set)}')