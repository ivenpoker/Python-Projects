#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Sums all the numbers in a list.                                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 01, 2020                                                 #
#                                                                                          #
############################################################################################

from random import randint
from functools import reduce

def create_random_list(low: int, high: int, size: int) -> list:
    if size < 0:
        raise ValueError(f"Invalid size '{size}'. Must be > 0")
    return [randint(low, high) for _ in range(size)]

def find_sum_1(some_list: list) -> int:
    return reduce(lambda acc, x: acc + x, some_list)

def find_sum_2(some_list: list) -> int:
    temp_sum = 0
    for x in some_list:
        temp_sum += x
    return temp_sum

if __name__ == "__main__":
    new_list = create_random_list(low=0, high=100, size=15)
    print(f'New list: {new_list}')

    print(f'-' * 25)

    print(f'Sum built-in: {sum(new_list)}')
    print(f'List sum (func 1): {find_sum_1(some_list=new_list)}')
    print(f'List sum (func 2): {find_sum_2(some_list=new_list)}')