#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Find a tuple, the smallest second index value from a list of      #
#                        tuples.                                                           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 23, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_tuple_list(low: int, high: int, size: int) -> list:
    if size < 0:
        raise ValueError('Invalid size for new array')
    return [(random.randint(low, high), random.randint(low, high)) for _ in range(size)]

def get_2nd_smallest(tuple_list: list) -> tuple:
    if len(tuple_list) == 0:
        return ()
    sorted_tuple_list = sorted(tuple_list, key=lambda x: x[1])
    return sorted_tuple_list[1] if len(sorted_tuple_list) > 1 else sorted_tuple_list[0]


if __name__ == "__main__":

    rand_list = random_tuple_list(low=-3, high=15, size=10)
    print(f'Generate list: {rand_list}')
    print(f'Second smallest value from list of tuples: '
          f'{get_2nd_smallest(tuple_list=rand_list)}')