
# !/usr/bin/env  python3

##############################################################################
#                                                                            #
#       Program purpose: Computes the GCD of two numbers.                    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>               #
#       Creation Date  : July 17, 2019                                       #
#                                                                            #
##############################################################################

# URL: https://www.w3resource.com/python-exercises/python-basic-exercises.php

def find_gcd(intA, intB):
    t = 0
    while intA > 0:
        if intA < intB:
            t = intA
            intA = intB
            intB = t
        intA = intA - intB
    return intB


if __name__ == "__main__":
    valA = int(input("Enter first integer: "))
    valB = int(input("Enter second integer: "))

    print(f"GCD of {valA} and {valB} is: {find_gcd(valA, valB)}")