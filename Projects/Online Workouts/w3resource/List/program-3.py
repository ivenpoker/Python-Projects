#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Finds the largest data item in a list of integer data.            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 8, 2019                                                  #
#                                                                                          #
############################################################################################

import random

def obtain_random_list_data(low: int, high: int, size: int) -> list:
    new_data = []
    for x in range(size):
        new_data.append(random.randint(low, high))
    return new_data

def find_largest_in_list(list_data: list) -> int:
    big = list_data[0]
    for x in list_data:
        if x > big:
            big = x
    return big

if __name__ == "__main__":

    data = obtain_random_list_data(low=1, high=50, size=10)
    print(f'Generated data: {data}')
    print(f'  Largest data: {find_largest_in_list(list_data=data)}')
