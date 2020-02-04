#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Creates a function that takes one argument, and that argument     #
#                        will be multiplied with an unknown given number.                  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 04, 2020                                                 #
#                                                                                          #
############################################################################################

from typing import Callable

def create_func(main_arg) -> Callable:
    return lambda new_arg: main_arg * new_arg

if __name__ == "__main__":

    demo_func = create_func(12)

    print(f"Calling 'demo_func(10)': {demo_func(10)}")
    print(f"Calling 'demo_func(12)': {demo_func(12)}")
    print(f"Calling 'demo_func(11)': {demo_func(11)}")

