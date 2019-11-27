#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Sorts (ascending and descending) a dictionary by key              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 27, 2019                                                 #
#                                                                                          #
############################################################################################

import operator
import random

def random_dictionary(low: int, high: int, size: int) -> dict:
    if size < 0:
        raise ValueError(f'Invalid size [{size}] for dictionary')
    key_list = [random.randint(low, high) for _ in range(size)]
    value_list = [random.randint(low, high) for _ in range(size)]

    return {k: v for (k, v) in zip(key_list, value_list)}

def sort_dict(main_dict: dict, ascending: bool) -> dict:
    return dict(sorted(main_dict.items(), key=operator.itemgetter(0))) if ascending else\
        dict(sorted(main_dict.items(), key=operator.itemgetter(0), reverse=True))

if __name__ == "__main__":

    random_dict = random_dictionary(low=0, high=20, size=20)
    print(f'              Generated dictionary is: {random_dict}')
    print(f' Sorted dictionary in ascending order: {sort_dict(main_dict=random_dict, ascending=True)}')
    print(f'Sorted dictionary in descending order: {sort_dict(main_dict=random_dict, ascending=False)}')
