#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Creates a shallow copy of sets.                                   #
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
    set_A = random_set_data(low=0, high=10, size=15)
    print(f'      Set A: {set_A}')
    print(f'Copy of Set: {set_A.copy()}')
