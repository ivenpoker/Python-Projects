#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Converts a list of multiple integers to a single integer.         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_int_list(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

def convert_list_to_single_integer(main_list: list) -> int:
    main_list = [str(x) for x in main_list]
    temp_data = ''.join(main_list)
    return int(temp_data)

if __name__ == "__main__":
    random_list = random_int_list(low=0, high=15, size=10)
    print(f'            Random data: {random_list}')
    print(f'Single combined integer: {convert_list_to_single_integer(main_list=random_list)}')