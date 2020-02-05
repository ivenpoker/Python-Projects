#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Finds the intersection of two given arrays using lambda.          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 05, 2020                                                 #
#                                                                                          #
############################################################################################

from typing import Callable

def FUNC_find_intersection(arr1: list, arr2: list) -> Callable:
    return lambda: [x for x in arr1 if x in arr2]

if __name__ == "__main__":

    array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
    array_nums2 = [1, 2, 4, 8, 9]

    filter_func = FUNC_find_intersection(arr1=array_nums1, arr2=array_nums2)

    print(f'Results: {filter_func()}')
