#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Appends item from a list to an array.                             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 20, 2019                                                  #
#                                                                                          #
############################################################################################

import array as arr
from random import randint

def random_list(low: int, high: int, size: int) -> list:
    if size < 0:
        raise ValueError(f"Invalid size '{size}' for new array")
    return [randint(low, high) for _ in range(size)]

if __name__ == "__main__":
    rand_list = random_list(low=0, high=100, size=8)
    print(f"Random list: {rand_list}")

    array_nm = arr.array('i', [])

    print(f'Array before inclusion: {array_nm}')
    array_nm.fromlist(rand_list)

    print(f'Array after inserting list: {array_nm}')
