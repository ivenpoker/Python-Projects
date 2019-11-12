#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Prints random item from a list.                                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 12, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_int_list(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

def print_random_items(main_data: list, max_rand: int) -> None:
    if max_rand < 0:
        raise ValueError('Invalid maximum random prints. Must be > 0')
    for x in range(max_rand):
        print(f'Random item #{x:02}: {main_data[random.randint(0, len(main_data))]}')

if __name__ == "__main__":

    main_list = random_int_list(low=0, high=15, size=10)
    print(f'Random list: {main_list}')
    print_random_items(main_data=main_list, max_rand=10)