#!/usr/bin/env python3

#######################################################################################
#                                                                                     #
#       Program purpose: Given an array of integers, finds the one that appears an    #
#                        odd number of times.                                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 10, 2020                                           #
#                                                                                     #
#######################################################################################

def fint_uniq(num_list: list) -> int:
    cnt_dict = dict()
    for x in num_list:
        if x not in cnt_dict.keys():
            cnt_dict[x] = num_list.count(x)
    return list(filter(lambda key: cnt_dict[key] == 1, cnt_dict.keys()))[0]


if __name__ == "__main__":
    print(fint_uniq(num_list=[1, 1, 1, 2, 1, 1]))
