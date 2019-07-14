#!/usr/bin/env  python3

##############################################################################
#                                                                            #
#       Program purpose: Given a string, returns sames string with a defined #
#                        number of repetitions.                              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>               #
#       Creation Date  : July 14, 2019                                       #
#                                                                            #
##############################################################################

# URL: https://www.w3resource.com/python-exercises/python-basic-exercises.php

def larger_string(_str, n):
    result = ""
    for i in range(n):
        result = result + _str
    return result


if __name__ == "__main__":
    user_str = input("Enter a string: ")
    str_rep = int(input("Enter number of repetitions: "))
    print("New string is: {}".format(larger_string(user_str, str_rep)))