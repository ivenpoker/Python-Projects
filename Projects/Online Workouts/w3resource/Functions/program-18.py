#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Accesses a function inside a function.                            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 01, 2020                                                 #
#                                                                                          #
############################################################################################

import typing

def do_test(valA) -> typing.Callable:
    def add(valB):
        nonlocal valA
        valA += 1
        return valA + valB
    return add

if __name__ == '__main__':
    func = do_test(4)
    print(func(4))
