#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Reverses a tuple.                                                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 19, 2019                                                 #
#                                                                                          #
############################################################################################

from random import randint

def random_tuple(low: int, high: int, size: int) -> tuple:
    if size < 0:
        raise ValueError(f"Invalid list size ({size})")
    return tuple([randint(low, high) for _ in range(size)])

def reverse_tuple(main_tuple: tuple) -> tuple:
    temp = list(main_tuple)
    temp.reverse()
    return tuple(temp)

if __name__ == '__main__':
    new_tuples = random_tuple(low=0, high=10, size=15)
    print(f'Newly generated data: {new_tuples}')

    reversed_data = reverse_tuple(main_tuple=new_tuples)
    print(f'Reversed tuple data: {reversed_data}')