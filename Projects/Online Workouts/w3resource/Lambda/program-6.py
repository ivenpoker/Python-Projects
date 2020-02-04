#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Squares and cubes every number in a given list of integers using  #
#                        Lambdas.                                                          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 04, 2020                                                 #
#                                                                                          #
############################################################################################

from typing import Callable
from random import randint

def random_int_list(low: int, high: int, size: int) -> list:
    if size < 0:
        raise ValueError(f"Invalid list size '{size}'. Must be > 0")
    return [randint(low, high) for _ in range(size)]

def process_list(list_data: list, func: Callable) -> list:
    return [func(item) for item in list_data]

if __name__ == "__main__":

    main_data = random_int_list(low=0, high=20, size=15)
    print(f"Main data: {main_data}")

    sqaured_list = process_list(list_data=main_data[:], func=lambda x: pow(x, 2))
    cubed_list = process_list(list_data=main_data[:], func=lambda x: pow(x, 3))

    print('-' * 75)
    print(f'Squared List: {sqaured_list}')
    print(f'  Cubed List: {cubed_list}')
    print('-' * 75)

    print(f'Original list: {main_data}')
