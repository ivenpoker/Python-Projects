#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Counts the number of times a specific element is present in a     #
#                        deque object.                                                     #
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

def display_occurrences(source_deque: deque) -> None:

    for i in range(len(source_deque)):
        temp = source_deque[i]
        count = source_deque.count(temp)
        print(f"{temp} occurs {count} time{'s' if count > 1 else ''} in deque")

if __name__ == "__main__":

    new_deque_data = create_new_deque(low=0, high=10, size=20)
    print(f'New deque data: {new_deque_data}')

    # display the number of times elements occur in deque
    display_occurrences(source_deque=new_deque_data)
