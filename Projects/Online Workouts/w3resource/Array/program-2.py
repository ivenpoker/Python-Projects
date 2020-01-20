#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Appends new item to the end of the array.                         #
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

    # Random integer array generated via function call.
    new_data = random_integer_array(low=0, high=10, size=5)

    print(f'New data: {new_data}')

    new_item = 12

    # Append new item to end of array
    new_data.append(12)

    print(f"After appending '12': {new_data}")