#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Determines if 2 list have a common member.                        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 8, 2019                                                  #
#                                                                                          #
############################################################################################

import random

def random_int_list(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

def found_common(listA: list, listB: list) -> bool:
    if len(listA) > len(listB):
        for x in listA:
            if x in listA:
                return True
    else:
        for x in listA:
            if x in listB:
                return True
    return False

if __name__ == "__main__":

    list_A = random_int_list(low=0, high=5, size=5)
    list_B = random_int_list(low=3, high=15, size=5)

    print(f'List A: {list_A}')
    print(f'List B: {list_B}')
    print(f'Does both list have common member: '
          f'{"YES" if found_common(listA=list_A, listB=list_B) else "NO"}')
