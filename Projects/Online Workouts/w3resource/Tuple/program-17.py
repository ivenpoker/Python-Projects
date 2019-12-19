#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Unzip a list of tuples into individual lists.                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 19, 2019                                                 #
#                                                                                          #
############################################################################################

from random import randint

def rand_tuples_list(low: int, high: int, size: int) -> list:
    if size < 0:
        raise ValueError(f"Invalid specified size ({size})")
    return [(randint(low, high), randint(low, high)) for _ in range(size)]

if __name__ == "__main__":
    new_list = rand_tuples_list(low=0, high=10, size=15)
    print(f'Newly generated data: {new_list}')
    print(f'Unzipped version: {list(zip(*new_list))}')
