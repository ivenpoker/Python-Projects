#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Replaces the last element in a list with another list.            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_int_list(low: int, high: int, list_size: int) -> list:
    if list_size < 0:
        raise ValueError('Invalid size of list')
    return [random.randint(low, high) for _ in range(list_size)]


def do_the_replacement(main_list: list, sub_list: list) -> list:
    main_list[-1:] = sub_list
    return main_list


if __name__ == "__main__":
    list_A = random_int_list(low=0, high=30, list_size=6)
    list_B = random_int_list(low=0, high=30, list_size=5)

    print(f'List A: {list_A}')
    print(f'List B: {list_B}')

    from_replacement = do_the_replacement(main_list=list_A, sub_list=list_B)

    print(f'New list after replacement:\n{from_replacement}')
