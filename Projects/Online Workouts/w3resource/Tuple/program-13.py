#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Demonstrates slicing a tuple.                                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 19, 2019                                                 #
#                                                                                          #
############################################################################################

from random import randint

def random_tuple(low: int, high: int, size: int) -> tuple:
    if size < 0:
        raise ValueError(f'Invalid size ({size}) for tuple')
    return tuple([randint(low, high) for _ in range(size)])

if __name__ == "__main__":
    new_tuple = random_tuple(low=0, high=10, size=15)
    print(f'New tuple data: {new_tuple}')
    print(f'Slice [3:6] -> {new_tuple[3:6]}')
    print(f'Slice [0:8:2] -> {new_tuple[0:8:2]}')