#!/usr/bin/env  python3

#############################################################################
#                                                                           #
#       Program purpose: Checks and compute a sum based on some property    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>              #
#       Creation Date  : July 14, 2019                                      #
#                                                                           #
#############################################################################

# URL: https://www.w3resource.com/python-exercises/python-basic-exercises.php


def is_vowel(some_lett):
    return some_lett[:1] in "aeiou"


if __name__ == "__main__":
    user_lett = input("Enter a letter to check if vowel: ")
    if is_vowel(user_lett):
        print(f"Letter {user_lett} is a vowel")
    else:
        print(f"Letter {user_lett} is NOT a vowel")
