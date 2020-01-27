#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Prints letter 'U' to the console.                                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 27, 2019                                                  #
#                                                                                          #
############################################################################################

def print_letter_U():
    for x in range(6):
        print('*', ' ' * 3, '*')
    print(('*' * 5).center(7, ' '))


if __name__ == '__main__':
    print_letter_U()
