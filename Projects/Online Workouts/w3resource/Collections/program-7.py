#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Creates a deque and append a few elements to the left and right,  #
#                        then removes some elements from left, right and reverse the deque.#
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 27, 2019                                                 #
#                                                                                          #
############################################################################################

from collections import deque
from random import randint

def get_random_deque(low: int, high: int, size: int) -> deque:
    if size < 0:
        raise ValueError(f'Invalid size ({size}) for deque')
    return deque([randint(low, high) for _ in range(size)])

def deque_append_left(source_deque: deque, max_rand: int) -> None:
    if max_rand < 0:
        raise ValueError(f'Invalid max ({max_rand}) for deque')
    for _ in range(max_rand):
        rand_val = randint(0, max_rand)
        print(f'Appending {rand_val} to left ... ', end='')
        source_deque.appendleft(rand_val)
        print(f'-> {source_deque}')

def deque_append_right(source_deque: deque, max_rand: int) -> None:
    if max_rand < 0:
        raise ValueError(f'Invalid max ({max_rand}) for deque')
    for _ in range(max_rand):
        rand_val = randint(0, max_rand)
        print(f'Appending {rand_val} to right ... ', end='')
        source_deque.append(rand_val)
        print(f'-> {source_deque}')

def remove_from_left(source_deque: deque, max_remove: int) -> None:
    if max_remove < 0:
        raise ValueError(f'Invalid max ({max_remove}) for deque')
    for _ in range(max_remove):
        print(f'Removing {source_deque[0]} from left ... ', end='')
        source_deque.popleft()
        print(f'-> {source_deque}')

def remove_from_right(source_deque: deque, max_remove: int) -> None:
    if max_remove < 0:
        raise ValueError(f'Invalid max ({max_remove}) for deque')
    source_len = len(source_deque)-1
    for _ in range(max_remove):
        print(f'Removing {source_deque[source_len]} ... ', end='')
        source_deque.pop()
        print(f'-> {source_deque}')
        source_len -= 1

def reverse_deque(source_deque: deque) -> None:
    print(f'Reversing {source_deque} ... ', end='')
    source_deque.reverse()
    print(f'-> {source_deque}')

if __name__ == "__main__":
    main_deque = get_random_deque(low=0, high=20, size=5)
    print(f'Main deque: {main_deque}')

    print(f'-' * 80)
    deque_append_left(source_deque=main_deque, max_rand=3)
    print(f'-' * 80)

    deque_append_right(source_deque=main_deque, max_rand=3)
    print(f'-' * 80)

    remove_from_left(source_deque=main_deque, max_remove=3)
    print(f'-' * 80)

    remove_from_right(source_deque=main_deque, max_remove=3)
    print(f'-' * 80)

    reverse_deque(source_deque=main_deque)
    print(f'-' * 80)