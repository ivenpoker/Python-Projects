#!/usr/bin/env  python3

###########################################################################
#                                                                         #
#       Program purpose: Finds the digits which are absent in a given     #
#                        mobile number (or list).                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>            #
#       Creation Date  : September 9, 2019                                #
#                                                                         #
###########################################################################

import random

def absent_digits(num):
    all_nums = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    temp = set([int(i) for i in num])
    temp = temp.symmetric_difference(all_nums)
    temp = sorted(temp)
    return temp

def random_integer_list(list_size=10):
    data = []
    for i in range(list_size):
        data.append(random.choice(seq=range(list_size)))
    return data

if __name__ == "__main__":
    random_list = random_integer_list(list_size=20)
    print(f"Generate list: {random_list}")
    print(f"Absent digits: {absent_digits(random_list)}")
