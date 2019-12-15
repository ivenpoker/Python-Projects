#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Converts a tuple to a string.                                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 15, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def rand_tuple(low: int, high: int, size: int) -> tuple:
    if size < 0:
        raise ValueError("Invalid size for tuple. Must be > 0")
    data = [f'{random.randint(low, high)}' for _ in range(size)]
    return tuple(data)

def tuple_to_string(tuple_data: tuple) -> str:
    return ' '.join(tuple_data)

if __name__ == "__main__":
    new_data = rand_tuple(low=0, high=10, size=10)
    print(f'Newly generated data: {new_data}')

    str_equiv = tuple_to_string(tuple_data=new_data)
    print(f'String equivalent: {str_equiv}')