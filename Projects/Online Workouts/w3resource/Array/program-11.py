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
    print(f'New data: {new_data}')

    # removing item at index 5
    ind = 5

    new_data.pop(5)
    print(f'After removing the 5th item from array: {new_data}')