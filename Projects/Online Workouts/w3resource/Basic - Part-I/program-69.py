# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Sorts 3 numbers without using conditional statements.        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 19, 2019                                              #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":
    try:
        intA = int(input("Enter first integer: "))
        intB = int(input("Enter second integer: "))
        intC = int(input("Enter third integer: "))

    except ValueError as ve:
        print(f"Last input cannot be converted to integer")

    inputs = [intA, intB, intC]
    list.sort(inputs)

    print(f"Sorted input: {inputs}")