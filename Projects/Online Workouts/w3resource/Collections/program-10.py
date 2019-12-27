#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Removes all the elements of a given deque object.                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 27, 2019                                                 #
#                                                                                          #
############################################################################################

from random import randint
from collections import deque

def create_new_deque(low: int, high: int, size: int) -> deque:
    if size < 0:
        raise ValueError(f'Invalid size ({size}) for new deque')
    return deque([randint(low, high) for _ in range(size)])


if __name__ == "__main__":
    new_deque = create_new_deque(low=0, high=20, size=10)
    print(f'New deque data: {new_deque}')

    new_deque.clear() # remove all elements from deque
    print(f'Deque after clearing all data: {new_deque} | length: {len(new_deque)}')
