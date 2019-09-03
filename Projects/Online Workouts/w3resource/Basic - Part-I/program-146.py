#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Find the location of python module resources.                #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 3, 2019                                            #
#                                                                                     #
#######################################################################################

import sys
import os

if __name__ == '__main__':
    print(f"List of directories in sys module:")
    print(f"{sys.path}")
    print(f"List of directories in os module:")
    print(os.path)