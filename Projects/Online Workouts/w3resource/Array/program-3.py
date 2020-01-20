#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Reverses the contents of an array.                                #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 20, 2019                                                  #
#                                                                                          #
############################################################################################

import array as arr
from random import randint

def random_integer_array(low: int, high: int, size: int) -> arr:
    if size < 0:
        raise ValueError(f"Invalid size '{size}' for new array")
    new_array = arr.array('i', [randint(low, high) for _ in range(size)])
    return new_array

if __name__ == "__main__":

    # Generate new random data
    new_data = random_integer_array(low=0, high=20, size=8)

    print(f'New data: {new_data}')

    new_data.reverse()
    print(f'After reversing: {new_data}')

