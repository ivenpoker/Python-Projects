#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Creates a dictionary from two lists.                              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 28, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_list(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

def create_dict(listA: list, listB: list) -> dict:
    new_dict = dict()
    for (k, v) in zip(listA, listB):
        new_dict[k] = v
    return new_dict


if __name__ == "__main__":

    list_A = random_list(low=0, high=10, size=5)
    list_B = random_list(low=0, high=10, size=5)

    print(f'List A: {list_A}')
    print(f'List B: {list_B}')

    print(f'New dictionary: {create_dict(listA=list_A, listB=list_B)}')
