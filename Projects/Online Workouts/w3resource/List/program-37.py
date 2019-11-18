#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Finds common item in two lists.                                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_int_list(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

def find_common_list_item(listA: list, listB: list) -> list:
    return list(set(listA) & set(listB))

if __name__ == "__main__":

    list_A = random_int_list(low=6, high=20, size=15)
    list_B = random_int_list(low=2, high=16, size=10)

    print(f'List A: {list_A}')
    print(f'List B: {list_B}')
    print(f'Common list items: {find_common_list_item(listA=list_A, listB=list_B)}')
