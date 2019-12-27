#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Finds the maximum and minimum value in a set.                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 27, 2019                                                 #
#                                                                                          #
############################################################################################

from random import randint

def random_set(low: int, high: int, size: int) -> set:
    if size < 0:
        raise ValueError(f'Invalid size ({size}) for new set')
    return set([randint(low, high) for _ in range(size)])

if __name__ == "__main__":
    new_set_data = random_set(low=0, high=10, size=15)
    print(f'New set data: {new_set_data}')
    print(f'Max data in set: {max(new_set_data)}')
    print(f'Min data in set: {min(new_set_data)}')