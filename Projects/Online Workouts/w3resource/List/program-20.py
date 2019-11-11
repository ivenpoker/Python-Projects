#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Access index of a list.                                           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 11, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def rand_int_list(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

def print_data(some_data: list) -> None:
    for (i, x) in enumerate(some_data):
        print(f'Index: {i:02} ---> Data: {x}')

if __name__ == "__main__":
    new_data = rand_int_list(low=1, high=10, size=20)
    print(f'Generated data: {new_data}')
    print_data(some_data=new_data)