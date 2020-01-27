#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Prints letter 'U' to the console.                                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 27, 2019                                                  #
#                                                                                          #
############################################################################################

def print_letter_Z():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if ((row == 0 or row == 6) and 0 <= column <= 6) or row + column == 6:
                result_str = result_str + "*"
            else:
                result_str = result_str + " "
        result_str = result_str + "\n"
    print(result_str)

if __name__ == '__main__':
    print_letter_Z()