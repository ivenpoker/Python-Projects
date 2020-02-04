#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Filters a list of integers using a lambda function.               #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 04, 2020                                                 #
#                                                                                          #
############################################################################################

from random import randint
from typing import Callable

def random_int_list(low: int, high: int, size: int) -> list:
    if size < 0:
        raise ValueError(f"Invalid size '{size}' for new list")
    return [randint(low, high) for _ in range(size)]

def func_based_filter(list_data: list, func: Callable) -> list:
    return list(filter(func, list_data))

if __name__ == "__main__":

    new_list_data = random_int_list(low=0, high=50, size=15)
    print(f"Random list data: {new_list_data}")

    all_odd_ints = func_based_filter(list_data=new_list_data, func=lambda x: x % 2 != 0)
    all_even_ints = func_based_filter(list_data=new_list_data, func=lambda x: x % 2 == 0)

    print(f' All odds from list: {all_odd_ints}')
    print(f'All evens from list: {all_even_ints}')
