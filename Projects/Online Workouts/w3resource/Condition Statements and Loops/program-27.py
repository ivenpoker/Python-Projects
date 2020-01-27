#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Prints letter 'T' to the console.                                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 27, 2019                                                  #
#                                                                                          #
############################################################################################

def print_letter_T():
    for x in range(10):
        print('*', end='')
    print()
    for x in range(10):
        print('*'.center(10, ' '))

if __name__ == '__main__':
    print_letter_T()
