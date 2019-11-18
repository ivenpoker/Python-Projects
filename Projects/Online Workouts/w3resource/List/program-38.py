#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Change the position of every n-th value with the (n+1)th in a     #
#                        list.                                                             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_int_list(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

def perform_change(main_list: list) -> list:
    for i in range(len(main_list)):
        if i % 2 == 0 and i + 1 < len(main_list):
            temp = main_list[i]
            main_list[i] = main_list[i+1]
            main_list[i+1] = temp
    return main_list

if __name__ == "__main__":
    random_list = random_int_list(low=0, high=10, size=16)
    print(f' Random list: {random_list}')
    print(f'After change: {perform_change(main_list=random_list)}')