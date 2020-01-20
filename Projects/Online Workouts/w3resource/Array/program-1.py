#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Creates an array of 5 integers and display the array items.       #
#                        Access individual element through indexes.                        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 20, 2019                                                  #
#                                                                                          #
############################################################################################

import array as arr
from random import randint


def random_array_data(low: int, high: int, size: int) -> arr:
    if size < 0:
        raise ValueError(f"Invalid '{size}' size for new array.")
    new_array = arr.array('i', [randint(low, high) for _ in range(size)])
    return new_array

def display_array_data(main_data: arr) -> None:
    print(f'Array items: ', end='')
    for item in main_data:
        print(f'{item} ', end='')
    print()

def display_via_indices(main_data: arr) -> None:
    print(f'Array items [index access]: ')
    for (i, item) in enumerate(main_data):
        print(f'data[{i}] = {main_data[i]}')

if __name__ == "__main__":

    # Create random integer array of specific size.
    new_data = random_array_data(low=0, high=20, size=5)
    print(f'New array data: {new_data}')

    # display data array data
    display_array_data(main_data=new_data)

    print('-' * 45)

    # display array data via indices
    display_via_indices(main_data=new_data)
