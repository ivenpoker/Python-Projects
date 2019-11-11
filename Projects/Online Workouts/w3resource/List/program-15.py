#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Shuffles and prints a specified list.                             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 11, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def generate_int_list(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

if __name__ == "__main__":

    new_list_data = generate_int_list(low=1, high=10, size=15)
    print(f'  New list data: {new_list_data}')

    random.shuffle(new_list_data)
    print(f'After shuffling: {new_list_data}')