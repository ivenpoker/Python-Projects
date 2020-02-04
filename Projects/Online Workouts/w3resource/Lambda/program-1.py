#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Creates a lambda function that adds 15 to a given number passed   #
#                        in as an argument, also creates a lambda function that multiplies #
#                        argument x with argument y and print the result.                  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 04, 2020                                                 #
#                                                                                          #
############################################################################################

from typing import Callable

def lambda_add(num: int) -> Callable:
    return lambda: num + 15

def lambda_mult(x_val, y_val) -> Callable:
    return lambda: x_val * y_val

if __name__ == "__main__":
    add_lambda = lambda_add(12)
    mult_lambda = lambda_mult(12, 12)

    print(f'Adding with lambda: {add_lambda()}')
    print(f'Multiplying with lambda: {mult_lambda()}')
