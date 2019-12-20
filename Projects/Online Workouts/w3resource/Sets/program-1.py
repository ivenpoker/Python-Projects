#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Creates a new empty set and another with data.                    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 20, 2019                                                 #
#                                                                                          #
############################################################################################

from random import randint

def random_set(low: int, high: int, size: int) -> set:
    if size < 0:
        raise ValueError(f"Invalid size ({size}) for array")
    return set([randint(low, high) for _ in range(size)])

if __name__ == "__main__":
    new_set = random_set(low=0, high=10, size=15)
    print(f'   Empty set: {set()}')
    print(f'New set data: {new_set}')
