#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Print the numbers of a specified list after removing even numbers #
#                        from it.                                                          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 11, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def generate_list_data(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

def process_data(main_data: list) -> list:
    return [x for x in main_data if x % 2 != 0]

if __name__ == "__main__":
    new_data = generate_list_data(low=1, high=10, size=15)
    print(f'     New data is: {new_data}')
    print(f'After processing: {process_data(main_data=new_data)}')