#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Prints letter 'L' to the console.                                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 27, 2019                                                  #
#                                                                                          #
############################################################################################

def print_letter_P():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (column == 1 or ((row == 0 or row == 3) and 0 < column < 5) or (
                    (column == 5 or column == 1) and (row == 1 or row == 2))):
                result_str = result_str + "*"
            else:
                result_str = result_str + " "
        result_str = result_str + "\n"
    print(result_str)

if __name__ == '__main__':
    print_letter_P()
