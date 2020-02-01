#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Multiplies all the numbers in a list.                             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 01, 2020                                                 #
#                                                                                          #
############################################################################################

from random import randint
from functools import reduce

def make_random_list(low: int, high: int, size: int) -> list:
    if size < 0:
        raise ValueError(f"Invalid size '{size}' for new list")
    return [randint(low, high) for _ in range(size)]

def multiply_list_A(some_list: list) -> int:
    if some_list and len(some_list) == 0:
        return 0
    temp_mult = 1
    for x in some_list:
        temp_mult *= x
    return temp_mult

def multiply_list_B(some_list: list) -> int:
    return reduce(lambda x, y: x * y, some_list, 1)

if __name__ == "__main__":
    new_list = make_random_list(low=0, high=20, size=15)
    print(f'Generated list: {new_list}')

    print('-' * 25)

    print(f'Multiplication with func A: {multiply_list_A(some_list=new_list)}')
    print(f'Multiplication with func B: {multiply_list_B(some_list=new_list)}')
