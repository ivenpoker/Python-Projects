#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Find and display the frequency of items in a list.                #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 12, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_int_list(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

def list_frequency(main_data: list) -> dict:

    data_info = {}
    for x in main_data:
        if x not in data_info.keys():
            data_info[x] = main_data.count(x)
    return data_info

if __name__ == "__main__":

    list_data = random_int_list(low=0, high=10, size=15)
    print(f'Generated integer list: {list_data}')
    print(f'Frequency info: {list_frequency(main_data=list_data)}')
