# !/usr/bin/env  python3

###################################################################################
#                                                                                 #
#       Program purpose: Program to do some profiling on Python program.          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                    #
#       Creation Date  : August 9, 2019                                           #
#                                                                                 #
###################################################################################

import cProfile

if __name__ == "__main__":

    def sum():
        print(1 + 2)

    cProfile.run('sum()')
