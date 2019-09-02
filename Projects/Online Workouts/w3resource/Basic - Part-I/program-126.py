# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Get actual module object for a given object.                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 2, 2019                                            #
#                                                                                     #
#######################################################################################

from inspect import getmodule
import os

if __name__ == "__main__":
    print(getmodule(os.path))
