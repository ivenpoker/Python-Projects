#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Converts a list into a tuple.                                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 19, 2019                                                 #
#                                                                                          #
############################################################################################

from random import randint

def random_tuple_list(low: int=0, high: int=10, size: int=10) -> list:
    if size < 0:
        raise ValueError(f"Invalid list size f'{size}'.")
    return [(randint(low, high), randint(low, high)) for _ in range(size)]

def list_to_tuples(main_list: list) -> tuple:
    return tuple(main_list)

if __name__ == "__main__":
    new_tuple = random_tuple_list(low=0, high=10, size=10)
    print(f'New tuple: {new_tuple}')
    print(f'Converting list to tuples: {list_to_tuples(main_list=new_tuple)}')