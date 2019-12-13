#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Creates a dictionary from two lists without losing duplicate      #
#                        values                                                            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 13, 2019                                                 #
#                                                                                          #
############################################################################################

from collections import defaultdict

def create_dict_from_list(list_A: list, list_B: list) -> dict:
    temp = defaultdict(set)
    for c, i in zip(list_A, list_B):
        temp[c].add(i)
    return temp

if __name__ == "__main__":
    sample_list_A = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VII']
    sample_list_B = [1, 2, 2, 3]

    print(f'List A: {sample_list_A}')
    print(f'List B: {sample_list_B}')
    print(f'Create dictionary: {create_dict_from_list(list_A=sample_list_A, list_B=sample_list_B)}')