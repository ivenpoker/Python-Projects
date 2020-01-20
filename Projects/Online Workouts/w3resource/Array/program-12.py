#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Removes the first occurrence of a specified element from an array #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 20, 2019                                                  #
#                                                                                          #
############################################################################################

import array as arr
from random import randint

def random_integer_array(low: int, high: int, size: int) -> arr:
    if size < 0:
        raise ValueError(f"Invalid array size '{size}'")
    new_data = arr.array('i', [randint(low, high) for _ in range(size)])
    return new_data

if __name__ == "__main__":

    new_array = random_integer_array(low=0, high=20, size=10)
    print(f'Original array: {new_array}')

    temp, passed = randint(0, 20), False
    while not passed:
        try:
            new_array.remove(temp)
            passed = True
        except ValueError as ve:
            temp = randint(0, 20)
            print(f"[ERROR]: Remove failure for '{temp}' ...")

    print(f"After removing '{temp}': {new_array}")