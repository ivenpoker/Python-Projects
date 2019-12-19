#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Computes the length of a tuple.                                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 19, 2019                                                 #
#                                                                                          #
############################################################################################

from random import randint

def random_tuple(low: int, high: int, size: int) -> tuple:
    if size < 0:
        raise ValueError(f"Invalid size ({size}) for the new tuple(s)")
    return tuple([randint(low, high) for _ in range(size)])

if __name__ == "__main__":
    new_tuples = random_tuple(low=0, high=10, size=15)
    print(f'New generated tuples: {new_tuples}')
    print(f'Length of tuple is: {len(new_tuples)}')
