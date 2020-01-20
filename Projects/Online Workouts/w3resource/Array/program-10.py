#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Inserts a new item before the second element in an existing array #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 20, 2019                                                  #
#                                                                                          #
############################################################################################

import array as arr
from random import randint

def random_integer_array(low: int, high: int, size: int) -> arr:
    if size < 0:
        raise ValueError(f"Invalid specified size '{size}' for new array")
    new_array = arr.array('i', [randint(low, high) for _ in range(size)])
    return new_array

if __name__ == "__main__":
    new_data = random_integer_array(low=0, high=10, size=8)
    print(f'Original array data: {new_data}')

    some_int = -10
    print(f"Inserting the string '{some_int}' into array ...")

    new_data.insert(1, some_int)
    print(f'After inserting before 2nd element: {new_data}')

