#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Append items from iterable to the end of the array.               #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 20, 2019                                                  #
#                                                                                          #
############################################################################################

import array as arr
from random import randint

def random_integer_array(low: int, high: int, size: int) -> arr:
    if size < 0:
        raise ValueError(f"Invalid size {size} for new array.")
    new_array = arr.array('i', [randint(low, high) for _ in range(size)])
    return new_array

if __name__ == "__main__":
    new_data = random_integer_array(low=0, high=15, size=8)
    print(f'New array data: {new_data}')

    temp = [1, 2, 3, 4]
    new_data.extend(temp)

    print(f'After extending: {new_data}')
