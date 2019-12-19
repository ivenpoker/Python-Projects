#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Prints a tuple with string formatting.                            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 19, 2019                                                 #
#                                                                                          #
############################################################################################

from random import randint

def random_tuples(low: int, high: int, size: int) -> tuple:
    if size < 0:
        raise ValueError(f'Invalid size ({size}) for new tuples')
    return tuple([randint(low, high) for _ in range(size)])

if __name__ == "__main__":
    new_data = random_tuples(low=0, high=10, size=15)
    print(f'Newly generated data [formatted]: {new_data}')
