#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Removes duplicate items for list of integer data.                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 8, 2019                                                  #
#                                                                                          #
############################################################################################

import random

def obtain_random_int_list(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

def remove_duplicates(data_list: list) -> list:
    return list(set(data_list))

if __name__ == "__main__":

    list_data = obtain_random_int_list(low=0, high=20, size=25)
    print(f'         Random list data: {list_data}')
    print(f'After removing duplicates: {remove_duplicates(data_list=list_data)}')