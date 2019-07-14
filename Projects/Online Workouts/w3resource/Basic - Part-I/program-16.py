#!/usr/bin/env    python3

#############################################################################
#                                                                           #
#       Program purpose: Computes difference based on some property         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>              #
#       Creation Date  : July 14, 2019                                      #
#                                                                           #
#############################################################################

# URL: https://www.w3resource.com/python-exercises/python-basic-exercises.php

def compute_diff(someNum):
    if abs(someNum - 17) > 17:
        return 2 * abs(someNum - 17)
    return 17 - someNum

if __name__ == "__main__":
    userNum = int(input("Enter a number: "))
    diff = compute_diff(userNum)
    print("Difference is: {}".format(diff))
