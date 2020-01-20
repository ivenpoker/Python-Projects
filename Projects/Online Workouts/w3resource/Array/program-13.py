#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Converts an array to an ordinary list with the same items.        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 20, 2019                                                  #
#                                                                                          #
############################################################################################

import array as arr
from random import randint

def random_int_array(low: int, high: int, size: int) -> arr:
    if size < 0:
        raise ValueError(f"Invalid size '{size}' for new array")
    new_array = arr.array('i', [randint(low, high) for _ in range(size)])
    return new_array

if __name__ == "__main__":

    new_data = random_int_array(low=0, high=20, size=8)
    print(f"New array data: {new_data}")

    new_list = new_data.tolist()
    print(f"List from data: {new_list}")