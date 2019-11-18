#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Finds missing an additional values in two lists.                  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_int_list(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

if __name__ == "__main__":

    list_A = random_int_list(low=0, high=10, size=10)
    list_B = random_int_list(low=1, high=10, size=10)

    print(f'List A: {list_A}')
    print(f'List B: {list_B}')

    print(f"Missing values in second list: {list(set(list_A).difference(list_B))}")
    print(f"Additional values in second list: {list(set(list_B).difference(list_A))}")
