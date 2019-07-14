#!/usr/bin/env  python3

#############################################################################
#                                                                           #
#       Program purpose: Checks is user provided integer is even or odd     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>              #
#       Creation Date  : July 14, 2019                                      #
#                                                                           #
#############################################################################

# URL: https://www.w3resource.com/python-exercises/python-basic-exercises.php


def is_even(val):
    return val % 2 == 0             # If even returns 0, any other number means, 'val' is odd.

if __name__ == "__main__":
    user_val = int(input("Enter an integer: "))
    if is_even(user_val):
        print("Integer value '{}' is: {}".format(user_val, "EVEN"))
    else:
        print("Integer value '{}' is: {}".format(user_val, "ODD"))
