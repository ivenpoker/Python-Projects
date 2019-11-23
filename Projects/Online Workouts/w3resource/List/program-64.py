#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Iterates over two lists simultaneously.                           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 23, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_int_list(low: int, high: int, size: int) -> list:
    if size < 0:
        raise ValueError('Invalid size of new list')
    return [random.randint(low, high) for _ in range(size)]

def display_both_lists(listA: list, listB: list) -> None:
    for valA, valB in zip(listA, listB):
        print(f'--> {valA} {valB}')

if __name__ == "__main__":

    list_A = random_int_list(low=0, high=15, size=10)
    list_B = random_int_list(low=0, high=15, size=10)
    print(f'Generate list data [A]: {list_A}')
    print(f'Generate list data [B]: {list_B}')

    display_both_lists(listA=list_A, listB=list_B)

