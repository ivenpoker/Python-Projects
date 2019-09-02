# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Compute the time runs of a program.                          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 2, 2019                                            #
#                                                                                     #
#######################################################################################

import timeit

def timer(n):
    start = timeit.default_timer()

    # some code here

    for row in range(0, n):
        print(row)

    print(timeit.default_timer() - start)


if __name__ == "__main__":
    timer(5)
    timer(15)
