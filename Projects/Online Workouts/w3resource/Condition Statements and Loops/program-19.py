#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Prints letter 'E' to the console.                                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 27, 2019                                                  #
#                                                                                          #
############################################################################################

def print_letter():
    for x in range(7):
        if x % 3 == 0:
            print('*' * 5)
        else:
            print('*')

if __name__ == '__main__':
    print_letter()