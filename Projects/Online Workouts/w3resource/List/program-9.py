#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Clones a list with data.                                          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 8, 2019                                                  #
#                                                                                          #
############################################################################################

import random

def generate_random_int_list(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

def clone_list(list_data: list) -> list:
    return list(list_data)

if __name__ == "__main__":
    new_data = generate_random_int_list(low=1, high=25, size=20)
    print(f'Generated data: {new_data}')
    print(f'New clone data: {clone_list(list_data=new_data)}')