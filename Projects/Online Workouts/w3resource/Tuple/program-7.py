#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Gets the 4th element and 4th element from last of a tuple.        #
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
    print(f'New data: {new_data}')

    print(f'4th item in data [from front]: {new_data[3]}')
    print(f'4th item in data [from back] : {new_data[-4]}')