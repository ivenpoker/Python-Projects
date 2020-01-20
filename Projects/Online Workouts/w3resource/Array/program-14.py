#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Finds if a given array of integers contains any duplicate element #
#                        Returns true if any value appears at least twice in the said      #
#                        array and return false if every element is distinct.              #
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

def test_duplicate(main_data: arr) -> bool:
    temp_set = set(main_data)
    return len(temp_set) != len(main_data)

if __name__ == "__main__":
    new_data = random_int_array(low=0, high=30, size=8)
    print(f'Main data: {new_data}')
    print(f'Duplicate present: {test_duplicate(main_data=new_data)}')