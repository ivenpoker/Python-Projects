# !/usr/bin/env  python3

#############################################################################
#                                                                           #
#       Program purpose: Displays a histogram from list data                #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>              #
#       Creation Date  : July 14, 2019                                      #
#                                                                           #
#############################################################################

# URL: https://www.w3resource.com/python-exercises/python-basic-exercises.php

def histogram(someList, char):
    for x in someList:
        while x > 0:
            print(f"{char}", end='')
            x = x-1
        print(f"\n")


if __name__ == "__main__":
    randList = [3, 7, 4, 2, 6]
    histogram(randList, '*')
