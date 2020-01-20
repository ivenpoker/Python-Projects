#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Converts an array to an array of machine values and return the    #
#                        bytes representation.                                             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 20, 2019                                                  #
#                                                                                          #
############################################################################################

import array as arr
from random import randint

def random_integer_array(low: int, high: int, size: int) -> arr:
    if size < 0:
        raise ValueError(f"Invalid size '{size}' for new array data")
    new_data = arr.array('b', [randint(low, high) for _ in range(size)])
    return new_data

if __name__ == "__main__":
    new_array = random_integer_array(low=0, high=100, size=8)
    print(f'Bytes of first string: {new_array.tobytes()}')

    temp = arr.array('b', [119, 51, 114, 101, 115, 111, 117, 114, 99, 101])
    print(f'New array: {temp.tobytes()}')