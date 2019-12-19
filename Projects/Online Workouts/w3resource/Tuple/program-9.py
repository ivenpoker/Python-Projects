#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Finds duplicate tuples in a list of tuples.                       #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 19, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def rand_tuples(low: int = 0, high: int = 10, size: int = 10):
    if size < 0:
        raise ValueError("Invalid size for new list. Must be > 0")
    return [(random.randint(low, high), random.randint(low, high))
            for _ in range(size)]

def find_repeated(tuple_list: list) -> list:
    dups = []
    for (a, b) in tuple_list:
        if tuple_list.count((a, b)) >= 2 and (a, b) not in dups:
            dups.append((a, b))
    return dups

if __name__ == "__main__":
    new_tuples = rand_tuples(low=0, high=5, size=10)
    print(f'Random tuples: {new_tuples}')
    print(f'Repeated tuples: {find_repeated(tuple_list=new_tuples)}')

