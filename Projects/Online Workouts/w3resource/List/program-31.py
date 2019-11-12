#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Finds the number of items that falls within a certain range.      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 12, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_int_list(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

def count_items_in_range(main_data: list, low: int, high: int) -> int:
    cnt = int(0)
    for x in main_data:
        if low <= x <= high:
            cnt += 1
    return cnt

if __name__ == "__main__":
    list_data = random_int_list(low=0, high=20, size=15)
    print(f'Generated list data: {list_data}')
    print(f'Number of items in range  2 and 10: {count_items_in_range(main_data=list_data, low=2, high=10)}')
