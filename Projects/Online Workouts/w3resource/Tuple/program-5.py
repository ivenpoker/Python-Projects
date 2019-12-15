#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Adds an item in a tuple.                                          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 15, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def rand_tuple(low: int, high: int, size: int) -> tuple:
    if size < 0:
        raise ValueError("Invalid size for tuple. Must be > 0")
    data = [random.randint(low, high) for _ in range(size)]
    return tuple(data)

def add_item_in_tuple(data: tuple, ind: int, ind_data) -> tuple:
    return data[:ind-1] + tuple(ind_data) +  data[ind+1:]

if __name__ == "__main__":
    new_data = rand_tuple(low=0, high=10, size=5)
    print(f'New tuple data: {new_data}')

    rand_ind = random.randint(0, len(new_data))
    new_ind_data = 'N'

    new_data = add_item_in_tuple(data=new_data, ind=rand_ind, ind_data=new_ind_data)
    print(f'New data: {new_data} [random-index: {rand_ind}]')