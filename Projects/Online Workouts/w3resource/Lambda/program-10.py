#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Creates Fibonacci series up to 'n' using lambda.                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 05, 2020                                                 #
#                                                                                          #
############################################################################################

from typing import Callable
from functools import reduce

def fibonacci_func() -> Callable:
    return lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0, 1])

if __name__ == "__main__":

    fib_func = fibonacci_func()

    print(f'Fibonacci series up to 2: {fib_func(2)}')
    print(f'Fibonacci series up to 5: {fib_func(5)}')
    print(f'Fibonacci series up to 6: {fib_func(6)}')
    print(f'Fibonacci series up to 9: {fib_func(9)}')