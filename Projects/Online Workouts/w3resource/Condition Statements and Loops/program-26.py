#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Prints letter 'S' to the console.                                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 27, 2019                                                  #
#                                                                                          #
############################################################################################

def print_letter_S():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (((row == 0 or row == 3 or row == 6) and 1 < column < 5) or (
                    column == 1 and (row == 1 or row == 2 or row == 6)) or (
                    column == 5 and (row == 0 or row == 4 or row == 5))):
                result_str = result_str + "*"
            else:
                result_str = result_str + " "
        result_str = result_str + "\n"
    print(result_str)

    row = 15
    col = 18
    result_str = ""
    for i in range(1, row + 1):
        if (i <= 3) or (7 <= i <= 9) or (13 <= i <= 15):
            for j in range(1, col):
                result_str = result_str + "o"
            result_str = result_str + "\n"
        elif 4 <= i <= 6:
            for j in range(1, 5):
                result_str = result_str + "o"
            result_str = result_str + "\n"
        else:
            for j in range(1, 14):
                result_str = result_str + " "
            for j in range(1, 5):
                result_str = result_str + "o"
            result_str = result_str + "\n"
    print(result_str)

if __name__ == '__main__':
    print_letter_S()
