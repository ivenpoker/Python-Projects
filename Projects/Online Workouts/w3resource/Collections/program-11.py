#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Make a copy of a deque object and verifies the shallow copying    #
#                        process.                                                          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 27, 2019                                                 #
#                                                                                          #
############################################################################################

from collections import deque
from random import randint

def create_new_deque(low: int, high: int, size: int) -> deque:
    if size < 0:
        raise ValueError(f'Invalid size [{size}] for new deque data')
    return deque([randint(low, high) for _ in range(size)])

if __name__ == "__main__":
    new_deque_data = create_new_deque(low=0, high=20, size=10)
    print(f'New deque data: {new_deque_data}')

    new_deque_copy = new_deque_data.copy()
    print(f'New deque copy: {new_deque_copy}')

    print('-' * 60)
    new_deque_copy.append('[new data]')
    print(f'Original deque data: {new_deque_data}')
    print(f' Modified copy data: {new_deque_copy}')

    print('-' * 60)
    print(f'Original ID: {id(new_deque_data)}')
    print(f'    Copy ID: {id(new_deque_copy)}')

    print('-' * 60)
    print(f'Checking the first element of deque and that of copy, are shallow copies:')
    print(f'{id(new_deque_data[0])}')
    print(f'{id(new_deque_copy[0])}')
