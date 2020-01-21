#!/usr/bin/env  python3

#################################################################################
#                                                                               #
#       Program purpose: Program that performs a search on data store using the #
#                        high perfomance binary search algorithm.               #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                  #
#       Creation Date  : January 21, 2020                                       #
#                                                                               #
#################################################################################

from random import randint
import math

def random_int_list(low: int, high: int, size: int) -> list:
    if size < 0:
        raise ValueError(f"Invaliid size '{size}' for new list")
    return [randint(low, high) for _ in range(size)]

def BNS_algo(source: list, key: int) -> int:
    low = 0
    high = len(source)
    while low < high:
        ind = int((low + high) / 2)
        if source[ind] < key:
            low = ind + 1
        elif source[ind] > key:
            high = ind - 1
        else:
            return ind  # key found, we return it's index in iterable
    return -1           # key not found, we return -1 (negative index)

def begin_simmulation():
    new_source_data = random_int_list(low=0, high=200, size=20)
    sorted_data = sorted(new_source_data)

    # begin interaction with user

    found = False  # keep track if user data is found
    max_repeat = 30

    print(f'=' * (max_repeat * 3 + 1))
    print(f'{sorted_data}')
    print(f'=' * (max_repeat * 3 + 1))

    while not found:
        try:
            print('-' * max_repeat)
            user_guess = int(input('Enter your seach key: '))
            results = BNS_algo(sorted_data, user_guess)

            if results >= 0:         # key found in source data
                found = True
            else:
                print('-' * max_repeat)
                print(f"Oops! '{user_guess}' not found!")

        except ValueError as ve:
            print(f'[ERROR]: {ve}')

    print()
    print(f'=' * 10, 'FOUND .. BYE!', '=' * 10)

if __name__ == "__main__":
    begin_simmulation()

