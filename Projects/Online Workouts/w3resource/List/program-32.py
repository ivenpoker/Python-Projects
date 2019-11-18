#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Checks if a sublist is found in a main list.                      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_int_data(low: int, high: int, size: int) -> list:
    return [random.randint(low, high) for _ in range(size)]

def check_sublist(main_list: list, sub_list: list) -> bool:
    if len(sub_list) > len(main_list):
        return False
    if len(sub_list) == len(main_list):
        return sorted(sub_list) == sorted(main_list)
    else:
        for (i, val) in enumerate(main_list):
            if i + len(sub_list) <= len(main_list):
                tmpA, tmpB, found = i, 0, True
                while tmpA < i + len(sub_list):
                    if main_list[tmpA] != sub_list[tmpB]:
                        found = False
                        break
                    tmpA += 1
                    tmpB += 1
                if found:
                    return True
    return False

if __name__ == "__main__":

    new_list = random_int_data(low=0, high=3, size=30)
    new_sub_list = random_int_data(low=0, high=3, size=3)

    print(f'Main list data: {new_list}')
    print(f'Checking sub list: {new_sub_list}')
    print(f'Is sublist found in main list: '
          f'{"YES" if check_sublist(main_list=new_list, sub_list=new_sub_list) else "NO"}')
