#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Checks if the n-th element exists in a given list.                #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 23, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_list_data(low: int, high: int, size: int) -> list:
    if size < 0:
        raise ValueError('Invalid size for list')
    return [random.randint(low, high) for _ in range(size)]

def ith_exists(list_data: list, ith_val: int) -> bool:
    if 0 <= ith_val < len(list_data):
        return list_data[ith_val] is not None
    return False

if __name__ == "__main__":

    rand_list = random_list_data(low=0, high=100, size=10)
    print(f'Generated list is: {rand_list}')
    temp = random.randint(0, len(rand_list)+10)
    print(f"Is the '{temp}'-th value present: {ith_exists(rand_list, temp)}")
