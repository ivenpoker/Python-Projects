#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Create an intersection of sets.                                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 24, 2019                                                 #
#                                                                                          #
############################################################################################

from random import randint

def random_set_data(low: int, high: int, size: int) -> set:
    if size < 0:
        raise ValueError(f'Invalid size ({size}) for new set')
    return set([randint(low, high) for _ in range(size)])

if __name__ == "__main__":
    set_A = random_set_data(low=0, high=10, size=15)
    set_B = random_set_data(low=0, high=10, size=15)

    print(f'Set A: {set_A}')
    print(f'Set B: {set_B}')
    print(f'Intersection of sets: {set_A & set_B}')