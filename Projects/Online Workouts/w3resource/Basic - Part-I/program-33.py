# !/usr/bin/env  python3

################################################################################
#                                                                              #
#       Program purpose: Find the sum of three numbers based on some factor.   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                 #
#       Creation Date  : July 17, 2019                                         #
#                                                                              #
################################################################################

# URL: https://www.w3resource.com/python-exercises/python-basic-exercises.php

def find_sum(valA, valB, valC):
    if valA == valB or valB == valC or valA == valC:
        return 0
    return valA + valB + valC


if __name__ == "__main__":
    intA = int(input("Enter int A: "))
    intB = int(input("Enter int B: "))
    intC = int(input("Enter int C: "))

    print(f"Sum of {intA}, {intB} and {intC}: {find_sum(intA, int)}")

