# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Print current call stack.                                    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 29, 2019                                              #
#                                                                                     #
#######################################################################################

import traceback

def f1():
    return abc()

def abc():
    traceback.print_stack()

if __name__ == "__main__":
    f1()