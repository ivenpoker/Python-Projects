#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Adds two given list using map and lambda.                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 05, 2020                                                 #
#                                                                                          #
############################################################################################

from typing import Callable
from random import randint

def random_list(low: int, high: int, size: int) -> list:
    return [randint(low, high) for _ in range(size)]

def FUNC_add_list(list_A: list, list_B: list) -> Callable:
    return lambda: [x + y for (x, y) in zip(list_A, list_B)]

if __name__ == "__main__":

    data_A = random_list(low=0, high=25, size=15)
    data_B = random_list(low=0, high=25, size=15)

    print(f'List A: {data_A}')
    print(f'List B: {data_B}')

    sum_func = FUNC_add_list(list_A=data_A, list_B=data_B)
    print(f'   Sum: {sum_func()}')
