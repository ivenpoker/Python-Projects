#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Prints a list of space-separated elements.                        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 23, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_int_list(low: int, high: int, size: int) -> list:
    if size < 0:
        raise ValueError('Invalid size for new list')
    return [random.randint(low, high) for _ in range(size)]

if __name__ == "__main__":
    rand_list = random_int_list(low=0, high=10, size=15)
    print(f'Generated list is: {rand_list}')
    print(f'Space-separated: ', end='')
    print(*rand_list)