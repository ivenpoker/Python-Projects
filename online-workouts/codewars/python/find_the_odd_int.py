#!/usr/bin/env python3

#######################################################################################
#                                                                                     #
#       Program purpose: Given an array of integers, finds the one that appears an    #
#                        odd number of times.                                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 10, 2020                                           #
#                                                                                     #
#######################################################################################


def find_it(ints: list) -> int:
    new_dict = dict()
    for x in ints:
        if x not in new_dict.keys():
            new_dict[x] = ints.count(x)
    odd_key = [x for x in new_dict.keys() if new_dict[x] % 2 == 1]

    return odd_key[0]

if __name__ == "__main__":
    print(find_it(ints=[20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
