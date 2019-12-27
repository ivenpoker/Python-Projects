#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Rotates (positive direction) a deque object a specified number    #
#                        of times.                                                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 27, 2019                                                 #
#                                                                                          #
############################################################################################

from collections import deque
from random import randint
from copy import deepcopy

def obtain_user_data(input_mess: str) -> int:
    user_data, valid = int(-1), False
    while not valid:
        try:
            user_data = int(input(input_mess))
            if user_data < 0:
                raise ValueError(f'Invalid number of rotations. Must be > 0')
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def create_new_deque(low: int, high: int, size: int) -> deque:
    if size < 0:
        raise ValueError(f'Invalid size ({size}) for new deque data')
    return deque([randint(low, high) for _ in range(size)])

def do_rotations_A(source_deque: deque, rot_cnt: int) -> None:
    print('-' * 60)
    tmp_cnt = 1
    while rot_cnt > 0:
        print(f'Rotation-A #{tmp_cnt}: ', end='')
        temp = source_deque.pop()
        source_deque.appendleft(temp)
        print(f'{source_deque}')
        rot_cnt -= 1
        tmp_cnt += 1

def do_rotations_B(source_deque: deque, rot_cnt: int) -> None:
    print('-' * 60)
    tmp_cnt = 1
    while rot_cnt > 0:
        source_deque.rotate()
        print(f'Rotation-B #{tmp_cnt}: {source_deque}')
        tmp_cnt += 1
        rot_cnt -= 1

if __name__ == "__main__":

    # generate random deque
    new_deque_data = create_new_deque(low=0, high=20, size=10)
    print(f'Generated deque data: {new_deque_data}')

    # obtain number of rotations from user
    num_rotations = obtain_user_data(input_mess='Enter number of rotations: ')

    # make copy for new deque
    temp_deque_copy = deepcopy(new_deque_data)

    # do the rotations and display it to user
    do_rotations_A(source_deque=new_deque_data, rot_cnt=num_rotations)
    do_rotations_B(source_deque=temp_deque_copy, rot_cnt=num_rotations)

