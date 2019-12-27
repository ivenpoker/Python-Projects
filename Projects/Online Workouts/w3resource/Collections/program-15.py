#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Finds the most common element of a given list (generated list).   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 27, 2019                                                 #
#                                                                                          #
############################################################################################

from collections import Counter
from random import randint

def create_random_list(low: int, high: int, size: int) -> list:
    if size < 0:
        raise ValueError(f'Invalid specified list size ({size})')
    return [randint(low, high) for _ in range(size)]

def find_most_common_in_list(main_list: list) -> int:
    temp_counter = Counter(main_list)
    # print(f'Most common data: {temp_counter.most_common(1)}')
    return temp_counter.most_common(1)[0][0]

if __name__ == "__main__":

    new_list = create_random_list(low=0, high=20, size=10)
    print(f'   Newly generated list data: {new_list}')
    print(f"Most common 'int' in data is: {find_most_common_in_list(main_list=new_list)}")
