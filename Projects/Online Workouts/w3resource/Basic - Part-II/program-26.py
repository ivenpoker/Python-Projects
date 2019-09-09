#!/usr/bin/env  python3

############################################################################
#                                                                          #
#       Program purpose: Compute the summation of the absolute difference  #
#                        of all distinct pairs in any given array.         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>             #
#       Creation Date  : September 9, 2019                                 #
#                                                                          #
############################################################################

import random

def random_integer_list(list_size=10):
    data = []
    for x in range(list_size):
        data.append(random.choice(seq=range(list_size)))
    return data

def compute_summation_diff(main_list=None):
    if main_list is None:
        main_list = []
    main_sum = 0
    for x in range(len(main_list)):
        for i in range(x+1, len(main_list)):
            main_sum += abs(main_list[x] - main_list[i])
    return main_sum


if __name__ == "__main__":
    random_list = random_integer_list(list_size=15)
    print(f"List is: {random_list}")
    print(f"Summation difference: {compute_summation_diff(main_list=random_list)}")