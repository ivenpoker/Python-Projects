#!/usr/bin/env  python3

#############################################################################
#                                                                           #
#       Program purpose: Checks and compute a sum based on some property    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>              #
#       Creation Date  : July 14, 2019                                      #
#                                                                           #
#############################################################################

# URL: https://www.w3resource.com/python-exercises/python-basic-exercises.php


def get_n_copies(some_str, n):
    if len(some_str) <= 2:
        return some_str * n
    return some_str[0:2] * n


if __name__ == "__main__":
    user_str = input("Enter some string: ")
    n_val = int(input("Enter number of copies of first two: "))
    print(f"New data: {get_n_copies(user_str, n_val)}")
