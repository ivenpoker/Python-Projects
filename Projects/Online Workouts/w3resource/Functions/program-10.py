#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Prints all the even numbers from a given (generated) list.        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 01, 2020                                                 #
#                                                                                          #
############################################################################################

from random import randint

def make_random_list(low: int, high: int, size: int) -> list:
    if size < 0:
        raise ValueError(f"Invalid specified size '{size}'")
    return [randint(low, high) for _ in range(size)]

def get_all_evens(some_list: list) -> list:
    return sorted([x for x in some_list if x % 2 == 0])

if __name__ == "__main__":

    main_list = make_random_list(low=0, high=20, size=15)
    print(f'Generated list: {main_list}')
    print(f'All evens in list: {get_all_evens(some_list=main_list)}')
