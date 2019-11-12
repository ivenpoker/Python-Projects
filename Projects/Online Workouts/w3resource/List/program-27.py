#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Finds and prints the second smallest element in list.             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 12, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_int_list(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

def obtain_2nd_smallest(main_data: list) -> int:
    if len(main_data) < 2:
        return main_data[0]

    # sort the list in ascending order, use `set` to remove duplicates, use `list` to obtain a list
    # since `sets` don't support indexing, finally return the 2nd element.

    return list(set(sorted(main_data)))[1]

if __name__ == "__main__":
    list_data = random_int_list(low=0, high=15, size=15)
    print(f'Generated list: {list_data}')
    print(f'Second smallest element in list: {obtain_2nd_smallest(main_data=list_data)}')
