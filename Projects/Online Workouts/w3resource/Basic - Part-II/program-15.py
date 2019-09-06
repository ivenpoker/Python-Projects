#!/usr/bin/env  python3

########################################################################
#                                                                      #
#       Program purpose: Program to check the priority of the four     #
#                        operators (+, -, *, /)                        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>         #
#       Creation Date  : September 6, 2019                             #
#                                                                      #
########################################################################

__operators__ = "+-/*"
__parenthesis__ = "()"
__priority__ = {
        '+': 0,
        '-': 0,
        '*': 1,
        '/': 1
}

def test_higher_priority(operatorA, operatorB):
    return __priority__[operatorA] >= __priority__[operatorB]

if __name__ == "__main__":

    print(test_higher_priority('*', '-'))
    print(test_higher_priority('+', '-'))
    print(test_higher_priority('+', '*'))
    print(test_higher_priority('+', '/'))
    print(test_higher_priority('*', '/'))
