#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Finds the smallest list item (integer list).                      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 8, 2019                                                  #
#                                                                                          #
############################################################################################

import random

def obtain_random_list_data(low: int, high: int, size: int) -> list:
    new_list_data = []
    for x in range(size):
        new_list_data.append(random.randint(low, high))
    return new_list_data

def find_smallest_list_item(data_list: list) -> int:
    small = data_list[0]
    for x in data_list:
        if x < small:
            small = x
    return small

if __name__ == "__main__":

    list_data = obtain_random_list_data(low=1, high=15, size=15)
    print(f'Generated list data: {list_data}')
    print(f' Smallest list item: {find_smallest_list_item(data_list=list_data)}')
