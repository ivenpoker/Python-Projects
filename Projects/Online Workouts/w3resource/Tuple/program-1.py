#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Creates a tuple.                                                  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 13, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def create_tuple() -> tuple:
    return random.randint(0, 10), random.randint(0, 10)

if __name__ == "__main__":

    temp_A = ()        # Create an empty tuple
    temp_B = tuple()   # Create tuple with built-in

    print(f'Tuple A: {temp_A}\nTuple B: {temp_B}')
    print(f'Random tuple: {create_tuple()}')