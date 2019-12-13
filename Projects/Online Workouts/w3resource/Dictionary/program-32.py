#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Prints a dictionary line by line.                                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 13, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_dict(low: int, high: int, size: int) -> dict:

    if low < 0: raise ValueError("Invalid value for low")
    if high < 0: raise ValueError("Invalid value for high")
    if size < 0: raise ValueError("Invalid value for the size")

    rand_keys = [random.randint(low, high) for _ in range(size)]
    rand_values = [random.randint(low, high) for _ in range(size)]

    return {k: v for (k, v) in zip(rand_keys, rand_values)}

def print_dict_line_by_line(main_dict: dict) -> None:
    for count, (key, value) in enumerate(main_dict.items(), 1):
        print(f'Line #{count} -> {key}: {value}')

if __name__ == "__main__":
    new_dict = random_dict(low=0, high=20, size=15)
    print_dict_line_by_line(main_dict=new_dict)