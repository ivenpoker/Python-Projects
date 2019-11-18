#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Concatenates element of a list.                                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_int_list(low: int, high: int, list_size: int) -> list:
    return [str(random.randint(low, high)) for _ in range(list_size)]

if __name__ == "__main__":

    list_data = random_int_list(low=0, high=20, list_size=15)
    print(f'Generated data: {list_data}')

    list_data_concat = '-'.join(list_data)
    print(f'After joining list data: {list_data_concat}')