# !/usr/bin/env  python3

###################################################################################
#                                                                                 #
#       Program purpose: Program to access some environmental variables.          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                    #
#       Creation Date  : August 10, 2019                                          #
#                                                                                 #
###################################################################################

import os


if __name__ == "__main__":

    print("*------------------------------------------*")
    print(os.environ)
    print("*------------------------------------------*")
    print(os.environ['HOME'])
    print("*------------------------------------------*")
    print(os.environ['PATH'])
    print("*------------------------------------------*")
