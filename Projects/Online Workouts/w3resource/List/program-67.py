#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Checks if all values in list are greater than a certain value.    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 23, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_int_list(low: int, high: int, size: int) -> list:
    if size < 0:
        raise ValueError('Invalid requested size of list')
    return [random.randint(low, high) for _ in range(size)]

if __name__ == "__main__":

    rand_list = random_int_list(low=0, high=50, size=10)
    print(f'Random list: {rand_list}')
    rand_val = random.randint(0, 10)

    # check if all values in list are greater than
    # rand_val

    print(f'All values > than {rand_val}: '
          f'{"YES" if all(x > rand_val for x in rand_list) else "NO"}')
