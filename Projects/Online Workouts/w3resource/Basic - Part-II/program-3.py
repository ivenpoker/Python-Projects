#!/usr/bin/env  python3

###########################################################################################
#                                                                                         #
#       Program purpose: Generate a list, remove and print every third number from a list #
#                        of numbers until the list becomes empty                          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                            #
#       Creation Date  : September 4, 2019                                                #
#                                                                                         #
###########################################################################################

import random

def random_integer_list(list_size=10):
    dataList = []
    for x in range(list_size):
        dataList.append(random.choice(range(list_size)))
    return dataList


def remove_every_3_number(int_list=None):
    # list starts with 0 index
    if int_list is None:
        int_list = []
    new_list = []
    position = 3 - 1
    idx = 0
    len_list = (len(int_list))
    while len_list > 0:
        idx = (position + idx) % len_list
        new_list.append(int_list.pop(idx))
        len_list -= 1

    return new_list

if __name__ == "__main__":

    random_list = random_integer_list(list_size=15)
    print(f"Random list: {random_list}")
    list_data = remove_every_3_number(int_list=random_list)

    print(f"Removed items: {list_data}")
