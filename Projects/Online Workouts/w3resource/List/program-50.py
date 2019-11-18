#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Sorts a list of nested dictionaries.                              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def generate_dict_of_dict(low: int, high: int, max_sub_dict: int) -> list:
    if max_sub_dict < 0:
        raise ValueError('Invalid sub dictionaries count')
    main_list = []
    for x in range(max_sub_dict):
        main_list.append({'key': {'subkey': random.randint(low, high)}})
    return main_list

def sort_list_of_dicts(dicts_list: list) -> list:
    return sorted(dicts_list, key=lambda val: val['key']['subkey'])

if __name__ == "__main__":

    list_of_dicts = generate_dict_of_dict(low=0, high=20, max_sub_dict=10)
    print(f'\nGenerated list of dictionaries:\n{list_of_dicts}')

    sorted_data = sort_list_of_dicts(dicts_list=list_of_dicts)
    print(f'\nSorted list dat:\n{sorted_data}')