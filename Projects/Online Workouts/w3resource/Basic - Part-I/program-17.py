#!/usr/bin/env  python3

#############################################################################
#                                                                           #
#       Program purpose: Test whether a number is within 100 of 1000 or     #
#                        2000.                                              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>              #
#       Creation Date  : July 14, 2019                                      #
#                                                                           #
#############################################################################

# URL: https://www.w3resource.com/python-exercises/python-basic-exercises.phps

def check_num(some_num):
    return (abs(1000 - some_num) <= 100) or (abs(2000 - some_num) <= 100)

if __name__ == "__main__":
    user_int = int(input("Enter a number near a {}: ".format(1000)))
    if check_num(user_int):
        print("TRUE")
    else:
        print("False")
