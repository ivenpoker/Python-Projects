#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Gets the current memory address and the length in elements of the #
#                        buffer used to hold an array's contents and also find the size of #
#                        the memory buffer in bytes.                                       #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 20, 2019                                                  #
#                                                                                          #
############################################################################################

import array as arr
from random import randint

def random_array_data(low: int, high: int, size: int) -> arr:
    if size < 0:
        raise ValueError(f"Invalid specified size '{size}' for new array")
    new_data = arr.array('i', [randint(low, high) for _ in range(size)])
    return new_data

if __name__ == "__main__":

    new_array = random_array_data(low=0, high=10, size=8)
    print(f'Original array: {new_array}')

    print(f'Current memory address and the length in elements of the buffer: {new_array.buffer_info()}')
    print(f'The size of the memory buffer in bytes: {new_array.buffer_info()[1] * new_array.itemsize}')
