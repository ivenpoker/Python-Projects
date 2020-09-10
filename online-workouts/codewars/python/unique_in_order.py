#!/usr/bin/env python3

#######################################################################################
#                                                                                     #
#       Program purpose: Parse iterable contents in a specific order.                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 10, 2020                                           #
#                                                                                     #
#######################################################################################

from typing import List


def unique_in_order(iterable) -> List[int]:
    uniques, prev = [], None

    for val in iterable:
        if val != prev:
            uniques.append(val)
            prev = val
    return uniques


if __name__ == '__main__':
    print(unique_in_order('AAAABBBCCDAABBB'))
    print(unique_in_order('ABBCcAD'))
    print(unique_in_order([1, 2, 2, 3, 3]))
