#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Creates a list with infinite elements.                            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

import itertools

if __name__ == "__main__":

    temp = itertools.count()
    while True:
        print(next(temp))
