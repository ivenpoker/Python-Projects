#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Removes item(s) from set if present.                              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 24, 2019                                                 #
#                                                                                          #
############################################################################################

from random import randint

def random_set_data(low: int, high: int, size: int) -> set:
    if size < 0:
        raise ValueError(f'Invalid size ({size}). Must be > 0')
    return set([randint(low, high) for _ in range(size)])

def do_some_processing(main_set: set) -> None:
    while len(main_set) > 0:
        print(f'Main set data: {main_set}')
        print('-' * 40)
        try:
            user_val = int(input('Enter item to remove from set: '))
            if remove_if_present(main_set=main_set, item=user_val):
                print(f'Data item {user_val} has been removed')
            else:
                print(f'Data item {user_val} has NOT been removed')
        except TypeError as ve:
            print(f'[ERROR]: {ve}')


def remove_if_present(main_set: set, item: int) -> bool:
    if item in main_set:
        main_set.discard(item)
        return True
    return False

if __name__ == "__main__":
    new_set = random_set_data(low=0, high=20, size=10)
    do_some_processing(main_set=new_set)