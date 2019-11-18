#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Get a variable unique identification number or string.            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

if __name__ == "__main__":
    x = 120
    print(format(id(x), 'x'))
    temp = 'Python Programmer'
    print(format(id(temp), 'x'))
