#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Rearranges positive and negative numbers in a given array using   #
#                        lambda.                                                           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 05, 2020                                                 #
#                                                                                          #
############################################################################################

from typing import Callable

def FUNC_rearrange_ints_A(some_data: list) -> Callable:
    return lambda: sorted(some_data)

def FUNC_rearrange_ints_B(some_data: list) -> Callable:
    return lambda: [x for x in some_data if x < 0] + [x for x in some_data if x >= 0]

if __name__ == "__main__":

    array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]

    rearrange_func_A = FUNC_rearrange_ints_A(some_data=array_nums[:])
    rearrange_func_B = FUNC_rearrange_ints_B(some_data=array_nums[:])

    print(f'Orginal array: {array_nums}')
    print(f'Re-arranged data A: {rearrange_func_A()}')
    print(f'Re-arranged data B: {rearrange_func_B()}')
