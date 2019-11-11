#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Generates all permutations of a list in Python.                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 11, 2019                                                 #
#                                                                                          #
############################################################################################

import itertools
import random

def random_int_list(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

def get_all_permutations(list_data: list) -> list:
    return list(itertools.permutations(list_data))

if __name__ == "__main__":
    new_data = random_int_list(low=1, high=10, size=5)
    print(f'Generated data: {new_data}')
    print(f'All permutations: {get_all_permutations(list_data=new_data)}')
