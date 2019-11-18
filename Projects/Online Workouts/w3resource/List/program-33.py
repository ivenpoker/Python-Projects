#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Finds all permutations of list data.                              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

import random
import itertools

def random_int_range(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

def find_all_sublist(main_list: list) -> list:
    perms = []
    for i in range(len(main_list)):
        temp = [list(x) for x in itertools.permutations(main_list, i)]
        perms.extend(temp)
    return temp

if __name__ == "__main__":

    list_data = random_int_range(low=0, high=10, size=5)
    print(f'List data: {list_data}')

    list_perm = find_all_sublist(main_list=list_data)
    print(f'All permutations: {list_perm}')