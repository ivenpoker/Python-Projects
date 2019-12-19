#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Reveal the index of elements in a tuple.                          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 19, 2019                                                 #
#                                                                                          #
############################################################################################

from random import randint

def random_tuple(low: int, high: int, size: int) -> tuple:
    if size < 0:
        raise ValueError(f'Invalid size ({size}) for tuple')
    return tuple([randint(low, high) for _ in range(size)])

def show_indices(main_tuple: tuple) -> None:
    for (ind, val) in enumerate(main_tuple):
        print(f"Index {ind} -> Value is '{val}'")
    print('-' * 30)
    for val in main_tuple:
        print(f"Index of '{val}' is {main_tuple.index(val)}")

if __name__ == "__main__":
    new_tuple = random_tuple(low=0, high=10, size=15)
    print(f'New tuple data: {new_tuple}')
    show_indices(main_tuple=new_tuple)