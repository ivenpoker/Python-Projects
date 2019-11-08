#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Multiplies all the contents of a list (int data)                  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 8, 2019                                                  #
#                                                                                          #
############################################################################################

import random

def obtain_random_int_list(low: int, high: int, size: int) -> list:
    new_list = []
    for x in range(size):
        new_list.append(random.randint(low, high))
    return new_list

def multiply_list_data(some_list: list) -> int:
    mult = 1
    for x in some_list:
        mult *= x
    return mult

if __name__ == "__main__":

    data = obtain_random_int_list(low=1, high=10, size=20)
    print(f'Random data: {data}')
    print(f'After multiplying all data: {multiply_list_data(some_list=data)}')
