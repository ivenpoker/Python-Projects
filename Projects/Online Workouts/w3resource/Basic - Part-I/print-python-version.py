#!/usr/bin/env python3

#############################################################################
#                                                                           #
#       Program purpose: Prints current python version in the system        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>              #
#       Creation Date  : 19/04/2019                                         #
#                                                                           #
#############################################################################


def print_version():
    import sys
    print("Current python version: \n\n{}".format(sys.version))

def main():
    print_version()

if __name__ == "__main__":
    main()