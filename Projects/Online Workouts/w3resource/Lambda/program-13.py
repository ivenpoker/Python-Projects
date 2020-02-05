#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Counts the even and odd numbers in a given array of integers      #
#                        using lambda.                                                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 05, 2020                                                 #
#                                                                                          #
############################################################################################

from random import randint

def random_list_data(low: int, high: int, size: int) -> list:
    if size < 0:
        raise ValueError(f"Invalid size '{size}' for new list")
    return list(randint(low, high) for _ in range(size))

def FUNC_filter_evens(some_data: list) -> int:
    temp_func = lambda: [x for x in some_data if x % 2 == 0]
    return len(temp_func())

def FUNC_filter_odds(some_data: list) -> int:
    temp_func = lambda: [x for x in some_data if x % 2 != 0]
    return len(temp_func())

if __name__ == "__main__":

    new_list_data = random_list_data(low=0, high=25, size=15)

    even_cnt = FUNC_filter_evens(some_data=new_list_data[:])
    odd_cnt = FUNC_filter_odds(some_data=new_list_data[:])

    print(f'New data: {new_list_data}')
    print(f' # Evens: {even_cnt}')
    print(f'  # Odds: {odd_cnt}')
