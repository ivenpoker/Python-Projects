#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Get the length in bytes of one array item in the internal         #
#                        representation.                                                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 20, 2019                                                  #
#                                                                                          #
############################################################################################

import array as arr
from random import randint

def random_integer_array(low: int, high: int, size: int) -> arr:
    if size < 0:
        raise ValueError(f"Invalid size '{size}' for new array")
    new_data = arr.array('i', [randint(low, high) for _ in range(size)])
    return new_data

if __name__ == "__main__":

    new_array = random_integer_array(low=0, high=20, size=10)
    print(f'New array data: {new_array}')
    print(f'Length in bytes of one array item: {new_array.itemsize} bytes')
