#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Unpacks a tuple in several variables.                             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 15, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def rand_tuple(low: int, high: int, size: int) -> tuple:
    if size < 0:
        raise ValueError("Invalid size for tuple. Must be > 0")
    data = [random.randint(low, high) for _ in range(size)]
    return tuple(data)

if __name__ == "__main__":
    new_data = rand_tuple(low=0, high=10, size=3)
    print(f'Original data: {new_data}')

    (x, y, z) = new_data
    print(f'Extracted data: ({x}, {y}, {z})')
