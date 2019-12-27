#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Adds more number of elements to a deque object from an iterable   #
#                        object.                                                           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 27, 2019                                                 #
#                                                                                          #
############################################################################################

from random import randint
from collections import deque

def create_random_deque(low: int, high: int, size: int) -> deque:
    if size < 0:
        raise ValueError(f'Invalid size ({size}) for new deque')
    return deque([randint(low, high) for _ in range(size)])

def add_nums_to_deque(source_deque: deque, max_ext: int) -> None:
    if max_ext < 0:
        raise ValueError(f'Invalid max size ({max_ext}) for deque')
    return source_deque.extend([randint(0, max_ext) for _ in range(max_ext)])

if __name__ == "__main__":

    new_deque = create_random_deque(low=0, high=20, size=5)
    print(f'New deque: {new_deque}')

    # Extend deque with 5 random data.
    add_nums_to_deque(source_deque=new_deque, max_ext=5)

    print(f'Extended deque: {new_deque}')
