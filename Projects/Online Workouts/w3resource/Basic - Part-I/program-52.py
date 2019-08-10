# !/usr/bin/env  python3

###################################################################################
#                                                                                 #
#       Program purpose: Prints to standard error stream                          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                    #
#       Creation Date  : August 9, 2019                                           #
#                                                                                 #
###################################################################################

from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

if __name__ == "__main__":
    eprint("abc", "efg", "xyz", sep="--")


