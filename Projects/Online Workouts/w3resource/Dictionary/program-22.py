#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Finds and returns the highest 3 values in a dictionary.           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 10, 2019                                                 #
#                                                                                          #
############################################################################################

import random
import operator

def get_user_num(input_mess: str, max_int: int) -> int:
    is_valid, user_data = False, ''
    while is_valid is False:
        try:
            user_data = int(input(input_mess))
            if user_data < 0:
                raise ValueError(f'Oops, number must be in range [0, {max_int}]')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def get_random_dict(low: int, high: int, size: int) -> dict:
    if size < 0:
        raise ValueError('Invalid size of dictionary. Must be > 0')
    rand_keys = [random.randint(low, high) for _ in range(size)]
    rand_values = [random.randint(low, high) for _ in range(size)]

    return {k: v for (k, v) in zip(rand_keys, rand_values)}

def sort_dict(main_dict: dict, ascending=True) -> dict:
    return dict(sorted(main_dict.items(), key=operator.itemgetter(0))) if ascending else\
        dict(sorted(main_dict.items(), key=operator.itemgetter(0), reverse=True))

def get_n_highest_values_in_dict(some_dict: dict, n_highs: int) -> list:


    if n_highs < 0 or n_highs > len(some_dict.keys()):
        raise ValueError(f'Invalid number of highs. Must be in range [0, {len(some_dict.keys())}]')

    # new_sorted_dict = sort_dict(main_dict=some_dict, ascending=False)
    # first_n_high = list(new_sorted_dict.values())[0:n_highs]
    # print(f'Sorted list: {new_sorted_dict}')

    dict_values = list(some_dict.values())
    sorted_values = sorted(dict_values, reverse=True)
    return sorted_values[0:n_highs]


if __name__ == "__main__":

    new_dict = get_random_dict(low=0, high=10, size=8)
    print(f'New dictionary: {new_dict}')

    # get user number
    user_num = get_user_num(input_mess='Enter number of highs: ', max_int=len(new_dict.keys()))
    list_n_highs = get_n_highest_values_in_dict(some_dict=new_dict, n_highs=user_num)

    print(f'Highs are: {list_n_highs}')

