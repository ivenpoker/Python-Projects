#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Gets the number of occurrences of a specified element in an array #
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

def obtain_user_int(input_mess: str) -> int:
    user_int, valid = int(-1), False
    while not valid:
        try:
            user_int = int(input(input_mess))
            valid = True
        except ValueError as ve:
            print(f"[ERROR]: {ve}")
    return user_int

def item_count(main_data: arr, item: int) -> int:
    return main_data.count(item)

if __name__ == "__main__":
    new_data = random_integer_array(low=0, high=10, size=8)
    print(f'New array data: {new_data}')

    user_val = obtain_user_int(input_mess="Enter index to count data [-ve num to stop]: ")
    while user_val >= 0:
        print(f'{user_val} occurs {item_count(main_data=new_data, item=user_val)} time(s)')
        user_val = obtain_user_int(input_mess="Enter index to count data [-ve num to stop]: ")





