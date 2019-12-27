#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Performs Counter arithmetic and set operations for aggregating    #
#                        results.                                                          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 27, 2019                                                 #
#                                                                                          #
############################################################################################

from collections import Counter
from random import randint

def create_new_list_data(low: int, high: int, size: int) -> list:
    if size < 0:
        raise ValueError(f'Invalid specified list size ({size}). Must be > 0')
    return [randint(low, high) for _ in range(size)]

def do_processing(list_A:  list, list_B: list) -> None:
    cA = Counter(list_A)
    cB = Counter(list_B)
    print(f'Combined counts: {cA + cB}\n')
    print(f'Subtraction: {cA - cB}\n')
    print(f'Intersection (taking +ve minimums): {cA & cB}\n')
    print(f'Union (taking maximums): {cA | cB}\n')

if __name__ == "__main__":

    data_A = create_new_list_data(low=0, high=20, size=10)
    data_B = create_new_list_data(low=0, high=20, size=10)

    print(f'List A: {data_A}')
    print(f'List B: {data_B}\n')

    do_processing(list_A=data_A, list_B=data_B)
