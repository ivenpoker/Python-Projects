# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Gets the detail of the math module.                          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 19, 2019                                              #
#                                                                                     #
#######################################################################################

import math

def get_details(module):
    return dir(module)

if __name__ == "__main__":
    print(f"\nDetails of math module: \n\n{get_details(module=math)}")
