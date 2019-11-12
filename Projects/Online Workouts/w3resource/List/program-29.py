#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Gets all unique item in a list.                                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 12, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_int_list(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

def get_unique_values(main_data: list) -> list:
    unique = []
    for x in main_data:
        if x not in unique:
            unique.append(x)
    return sorted(unique)

if __name__ == "__main__":
    rand_list = random_int_list(low=0, high=15, size=15)
    print(f' Randomly generated list: {rand_list}')
    new_data = get_unique_values(main_data=rand_list)
    print(f'Unique items in the list: {new_data} [expected: '
          f'{new_data == list(set(rand_list))}]')
    print(f'Using the standard set: {list(set(rand_list))}')