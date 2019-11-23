#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Finds the list in a list of lists whose sum of elements is the    #
#                        highest.                                                          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 23, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_int_list(low: int, high: int, size: int) -> list:
    if size < 0:
        raise ValueError('Invalid size for new list')
    return [random.randint(low, high) for _ in range(size)]

def do_computation(core_lists: list) -> list:
    temp_sum = 0
    track = None
    for temp_list in core_lists:
        if sum(temp_list) > temp_sum:
            track = list(temp_list)
            temp_sum = sum(temp_list)
    return track


if __name__ == "__main__":
    main_list = []
    for _ in range(10):
        main_list.append(random_int_list(low=0, high=10, size=5))
    print(f'Main list is: {main_list}')
    print(f'Sub-list with largest sum: {do_computation(core_lists=main_list)}')

