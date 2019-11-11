#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Print a specified list after removing the 0th, 4th and 5th        #
#                        elements.                                                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 11, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_int_list(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

def remove_indices(main_data: list, rem_ind: list) -> list:
    return [x for (i, x) in enumerate(main_data) if i not in rem_ind]

if __name__ == "__main__":

    rand_list = random_int_list(low=1, high=10, size=10)

    del_ind = [0, 4, 5]
    new_data = remove_indices(main_data=rand_list, rem_ind=del_ind)
    print(f'Generated list: {rand_list}')
    print(f'After removing the 0th, 4th and 5th indices: {new_data}')

