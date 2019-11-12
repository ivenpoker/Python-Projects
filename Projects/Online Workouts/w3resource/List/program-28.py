#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Finds and prints the second largest item in a list.               #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 12, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_int_list(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

def obtain_2nd_largest(main_data: list) -> int:
    if len(main_data) < 2:
        return main_data[0]

    # sort the list in ascending order, use `set` to remove duplicates, use `list` to obtain
    # a list since `sets` don't support indexing, finally return the 2nd element.

    new_data = list(set(sorted(main_data, reverse=True)))
    if len(new_data) < 2:
        return new_data[-1]
    return new_data[-2]

if __name__ == "__main__":

    list_data = random_int_list(low=0, high=10, size=10)
    print(f'Generated list: {list_data}')
    print(f'Second largest integer in list: {obtain_2nd_largest(main_data=list_data)}')

