#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Checks whether two lists are circularly identical.                #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 11, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_int_list(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

def compare_list(list1: list, list2: list) -> bool:
    return ' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2))

if __name__ == "__main__":

    list_A = random_int_list(low=0, high=5, size=5)
    list_B = random_int_list(low=0, high=5, size=5)

    print(f'List1: {list_A}')
    print(f'List2: {list_B}')

    print(f'Comparing List1 and List2: {compare_list(list1=list_A, list2=list_B)}')
    print(f'Comparing List2 and List1: {compare_list(list1=list_B, list2=list_A)}')



