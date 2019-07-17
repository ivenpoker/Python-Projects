# !/usr/bin/env  python3

################################################################################
#                                                                              #
#       Program purpose: Find sum based on some properties.                    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                 #
#       Creation Date  : July 17, 2019                                         #
#                                                                              #
################################################################################

# URL: https://www.w3resource.com/python-exercises/python-basic-exercises.php


def is_equal(valA, valB):
    if valA == valB:
        return True
    if abs(valA - valB) == 5 or valA + valB == 5: return True

if __name__ == "__main__":
    intA = int(input("Enter first integer: "))
    intB = int(input("Enter second integer: "))

    if is_equal(intA, intB):
        print(f"Integer {intA} and {intB} passed test!")
    else:
        print(f"Integer {intA} and {intB} failed test!")
