#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Computes the difference between two lists.                        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_int_list(low: int, high: int, list_size: int) -> list:
    return [random.randint(low, high) for _ in range(list_size)]

def compute_similarity(list1: list, list2: list) -> list:
    return list(set(list1).difference(set(list2)))

if __name__ == "__main__":
    list_A = random_int_list(low=0, high=10, list_size=15)
    list_B = random_int_list(low=0, high=10, list_size=10)

    print(f'List A: {list_A}')
    print(f'List B: {list_B}')

    print(f'Difference between A and B: {compute_similarity(list1=list_A, list2=list_B)}')
    print(f'Difference between B and A: {compute_similarity(list1=list_B, list2=list_A)}')