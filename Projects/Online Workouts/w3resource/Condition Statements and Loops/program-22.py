#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Prints letter 'M' to the console.                                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 27, 2019                                                  #
#                                                                                          #
############################################################################################

def print_letter_M():
    result_str = "";
    for row in range(0, 7):
        for column in range(0, 7):
            if (column == 1 or column == 5 or (row == 2 and (column == 2 or column == 4)) or (
                    row == 3 and column == 3)):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)

if __name__ == '__main__':
    print_letter_M()
