#!/usr/bin/env  python3

################################################################################
#                                                                              #
#       Program purpose: Validates string on some condition and returns string #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                 #
#       Creation Date  : July 14, 2019                                         #
#                                                                              #
################################################################################

# URL: https://www.w3resource.com/python-exercises/python-basic-exercises.php

def new_string(_str):
    if len(_str) >= 2 and _str[:2] == "Is":
        return _str
    return "Is" + _str

if __name__ == "__main__":
    user_str = input("Enter some string: ")
    print("New string is: {}".format(new_string(user_str)))

