#!/usr/bin/env  python3

#############################################################################
#                                                                           #
#       Program purpose: Checks and compute a sum based on some property    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>              #
#       Creation Date  : July 14, 2019                                      #
#                                                                           #
#############################################################################

# URL: https://www.w3resource.com/python-exercises/python-basic-exercises.php

def sum_thrice(valA, valB, valC):
    if valA == valB and valB == valC:
        return 3 * (valA + valB + valC)
    else:
        return valA + valB + valC

if __name__ == "__main__":
    intA = int(input("Enter first integer : "))
    intB = int(input("Enter second integer: "))
    intC = int(input("Enter third integer : "))

    print("Their sum is: {}".format(sum_thrice(intA, intB, intC)))


