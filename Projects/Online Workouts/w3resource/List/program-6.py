#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Get a list, sorted in increasing order by the last element in     #
#                        each tuple from a given list of non-empty tuples.                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 8, 2019                                                  #
#                                                                                          #
############################################################################################

def last(n):
    return n[-1]

def sort_list_last(tuple_list: list) -> list:
    return sorted(tuple_list, key=last)

if __name__ == "__main__":
    test_data = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(f'Original data: {test_data}')
    print(f'Sorted list data: {sort_list_last(tuple_list=test_data)}')