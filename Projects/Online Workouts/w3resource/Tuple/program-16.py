#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Converts a tuple to a dictionary.                                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 19, 2019                                                 #
#                                                                                          #
############################################################################################

from random import randint

def random_tuples(low: int, high: int, size: int, init_str: str) -> tuple:
    if size < 0:
        raise ValueError(f'Invalid size ({size}) for tuple(s)')
    cnt, temp = 0, []
    for _ in range(size):
        new_tup = (f'{init_str}{cnt}', randint(low, high))
        temp.append(new_tup)
        cnt += 1
    return tuple(temp)

def tuples_to_dict(main_tuple: tuple) -> dict:
    return {k: v for (k, v) in main_tuple}

if __name__ == "__main__":

    new_tuple_data = random_tuples(low=0, high=10, size=15, init_str='key')
    print(f'Tuple data: {new_tuple_data}')
    print(f'Dict equivalent: {tuples_to_dict(main_tuple=new_tuple_data)}')
