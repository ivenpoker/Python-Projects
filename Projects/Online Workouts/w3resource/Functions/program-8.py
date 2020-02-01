#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Takes a list and returns a new list with unique elements of       #
#                        the first list.                                                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 01, 2020                                                 #
#                                                                                          #
############################################################################################

from random import randint

def make_random_list(low: int, high: int, size: int) -> list:
    if size < 0:
        raise ValueError(f"Invalid size '{size}' for new list")
    return [randint(low, high) for _ in range(size)]

def unique_list_A(some_list: list) -> list:
    unique_list = []
    for x in some_list:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

def unique_list_B(some_list: list) -> list:
    return list(set(some_list))

if __name__ == "__main__":

    new_list = make_random_list(low=0, high=20, size=15)

    print(f'New list: {new_list}')
    print(f'-' * 25)
    print(f'Unique list [func A]: {unique_list_A(some_list=new_list)}')
    print(f'Unique list [func B]: {unique_list_B(some_list=new_list)}')
