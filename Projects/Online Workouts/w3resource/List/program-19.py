#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Gets the difference between two lists.                            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 11, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_int_list(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

def find_list_diff(list_A: list, list_B: list) -> list:
    diff = []
    if len(list_A) > len(list_B):
        for x in list_B:
            if x not in list_A:
                if x not in diff:
                    diff.append(x)
    else:
        for x in list_A:
            if x not in list_B:
                if x not in diff:
                    diff.append(x)
    return diff

if __name__ == "__main__":

    data_A = random_int_list(low=1, high=10, size=8)
    data_B = random_int_list(low=2, high=12, size=8)

    print(f'Data A: {data_A}')
    print(f'Data B: {data_B}')
    print(f'Difference: {find_list_diff(list_A=data_A, list_B=data_B)}')

