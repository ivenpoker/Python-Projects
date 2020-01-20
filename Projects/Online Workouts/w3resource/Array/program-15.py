#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Finds the first duplicate element in a given array of integers.   #
#                        returns -1 if there are no such elements.                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 20, 2019                                                  #
#                                                                                          #
############################################################################################

import array as arr
from random import randint

def random_int_array(low: int, high: int, size: int) -> arr:
    if size < 0:
        raise ValueError(f"Invalid size '{size}' for new array")
    new_array = arr.array('i', [randint(low, high) for _ in range(size)])
    return new_array

def find_first_duplicate(nums: arr) -> int:
    num_set = set()
    no_duplicate = -1

    for i in range(len(nums)):
        if nums[i] in num_set:
            return nums[i]
        else:
            num_set.add(nums[i])

    return no_duplicate

if __name__ == "__main__":

    print(find_first_duplicate(arr.array('i', [1, 2, 3, 4, 4, 5])))
    print(find_first_duplicate(arr.array('i', [1, 2, 3, 4])))
    print(find_first_duplicate(arr.array('i', [1, 1, 2, 3, 3, 4, 2, 2])))