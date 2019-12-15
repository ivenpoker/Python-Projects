#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Create a colon of a tuple.                                        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 15, 2019                                                 #
#                                                                                          #
############################################################################################

from copy import deepcopy

if __name__ == "__main__":
    tuplex = ("HELLO", 5, [], True)
    print(tuplex)
    tuplex_colon = deepcopy(tuplex)
    tuplex_colon[2].append(50)
    print(tuplex_colon)
    print(tuplex)