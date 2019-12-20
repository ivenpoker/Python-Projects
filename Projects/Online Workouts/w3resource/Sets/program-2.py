#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Iterates over sets.                                               #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 20, 2019                                                 #
#                                                                                          #
############################################################################################

from random import randint

def random_set_data(low: int, high: int, size: int) -> set:
    if size < 0:
        raise ValueError(f"Invalid new set size ({size})")
    return set([randint(low, high) for _ in range(size)])

def print_set_data(main_set: set) -> None:
    for (ind, val) in enumerate(main_set):
        print(f'#{ind+1} -> {val}')

if __name__ == "__main__":
    new_set = random_set_data(low=0, high=10, size=15)
    print(f'New set data: {new_set}')
    print('-' * 40)

    print_set_data(main_set=new_set)