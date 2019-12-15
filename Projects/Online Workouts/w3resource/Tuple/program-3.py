#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Creates a random tuple and prints one item within it.             #
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
    new_data = rand_tuple(low=0, high=10, size=10)
    print(f'New tuple data: {new_data}')
    print(f'One item from tuple: {new_data[random.randint(0, len(new_data))]}')
