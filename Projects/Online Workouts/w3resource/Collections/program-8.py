#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Creates a deque from an existing iterable object.                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 27, 2019                                                 #
#                                                                                          #
############################################################################################

from random import randint

def random_list(low: int, high: int, size: int) -> list:
    if size < 0:
        raise ValueError(f'Invalid size ({size}) for new list data')
    return [randint(low, high) for _ in range(size)]

def random_set(low: int, high: int, size: int) -> set:
    if size < 0:
        raise ValueError(f'Invalid size ({size}) for new set data')
    return set([randint(low, high) for _ in range(size)])

def random_tuple(low: int, high: int, size: int) -> tuple:
    if size < 0:
        raise ValueError(f'Invalid size ({size}) for new tuple data')
    return tuple([randint(low, high) for _ in range(size)])

def random_dict(low: int, high: int, size: int, init_key_str: str) -> dict:
    if size < 0:
        raise ValueError(f'Invalid size ({size}) for new set data')
    random_keys = [f'{init_key_str}{val}' for val in range(size)]
    random_vals = [randint(low, high) for _ in range(size)]

    return {k: v for (k, v) in zip(random_keys, random_vals)}

if __name__ == "__main__":

    new_list = random_list(low=0, high=10, size=5)
    new_set = random_set(low=0, high=10, size=5)
    new_dict = random_dict(low=0, high=10, size=5, init_key_str='key')
    new_tuple = random_tuple(low=0, high=10, size=5)

    print(f' New list: {new_list}')
    print(f'  New set: {new_set}')
    print(f' New dict: {new_dict}')
    print(f'New tuple: {new_tuple}')

