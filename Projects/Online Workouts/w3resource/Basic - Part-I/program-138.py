#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Program to convert true to 1 and false to 0.                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 3, 2019                                            #
#                                                                                     #
#######################################################################################

if __name__ == '__main__':
    x = 'true'
    x = int(x == 'true')
    print(f"Value of x: {x}")
    x = 'abcd'
    x = int(x == 'true')
    print(f"Value of x: {x}")
