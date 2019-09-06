#!/usr/bin/env  python3

########################################################################
#                                                                      #
#       Program purpose: Finds the median of 'n' numbers.              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>         #
#       Creation Date  : September 6, 2019                             #
#                                                                      #
########################################################################

import random

def random_list(list_size=10):
    data = []
    for x in range(list_size):
        data.append(random.choice(seq=range(list_size)))
    return data

def find_median(some_list=[]):
    if some_list is None:
        return None
    some_list = sorted(some_list)

    if len(some_list) % 2 != 0:
        return some_list[int(len(some_list) / 2)]
    else:
        temp = int((len(some_list)-1) / 2)
        return int((some_list[temp] + some_list[temp+1]) / 2)

if __name__ == "__main__":
    random_data = random_list(list_size=15)
    print(f"Generated list: {random_data}")
    print(f"Sorted list   : {sorted(random_data)} ")
    print(f"Median is: {find_median(random_data)}")
