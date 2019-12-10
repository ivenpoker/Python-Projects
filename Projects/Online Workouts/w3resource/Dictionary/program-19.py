#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Merges two dictionaries. If both dictionaries have the same key,  #
#                        their values are added.                                           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 10, 2019                                                 #
#                                                                                          #
############################################################################################

import random
import operator

main_alpha = 'abcdefghijklmnopqrstuvwxyz'

def random_letter() -> str:
    return main_alpha[random.randint(0, len(main_alpha)-1)]

def random_dict(low: int, high: int, size: int) -> dict:
    if size < 0:
        raise ValueError('Invalid size for dictionary. Must be > 0')
    rand_keys = [random_letter() for _ in range(size)]
    rand_values = [random.randint(low, high) for _ in range(size)]

    return {k: v for (k, v) in zip(rand_keys, rand_values)}

def is_dict_empty(some_dict: dict) -> bool:
    return len(some_dict.keys()) == 0

def merge_dict(dict_A: dict, dict_B: dict) -> dict:

    if is_dict_empty(some_dict=dict_A): return dict_B
    if is_dict_empty(some_dict=dict_B): return dict_A

    new_dict = dict()
    for (k, v) in zip(dict_A.keys(), dict_A.values()):
        new_dict[k] = v

    for (k, v) in zip(dict_B.keys(), dict_B.values()):
        if k in new_dict.keys():
            new_dict[k] += v
        else:
            new_dict[k] = v

    return new_dict

def sort_dict(main_dict: dict, ascending=True) -> dict:
    return dict(sorted(main_dict.items(), key=operator.itemgetter(0))) if ascending else\
        dict(sorted(main_dict.items(), key=operator.itemgetter(0), reverse=True))

if __name__ == "__main__":

    new_dict_A = random_dict(low=0, high=100, size=15)
    new_dict_B = random_dict(low=0, high=100, size=15)

    print(f'New dict A -> {sort_dict(main_dict=new_dict_A)}')
    print(f'New dict B -> {sort_dict(main_dict=new_dict_B)}')

    merged_dict = merge_dict(dict_A=new_dict_A, dict_B=new_dict_B)
    print(f'Merge dict -> {sort_dict(main_dict=merged_dict)}')
