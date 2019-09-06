#!/usr/bin/env  python3

########################################################################
#                                                                      #
#       Program purpose: Add two integers without using '+' operator.  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>         #
#       Creation Date  : September 6, 2019                             #
#                                                                      #
########################################################################

def add_without_plus_operator(numA, numB):
    while numB != 0:
        data = numA & numB
        numA = numA ^ numB
        numB = data << 1
    return numA

if __name__ == "__main__":

    intA = int(input("Enter first number: "))
    intB = int(input("Enter second number: "))

    print(f"Sum of {intA} and {intB} is {add_without_plus_operator(numA=intA, numB=intB)}")

