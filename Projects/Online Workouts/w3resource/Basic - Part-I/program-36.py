# !/usr/bin/env  python3

##################################################################################
#                                                                                #
#       Program purpose: Find the sum of two integers making sure they are ints. #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                   #
#       Creation Date  : July 17, 2019                                           #
#                                                                                #
##################################################################################

# URL: https://www.w3resource.com/python-exercises/python-basic-exercises.php



def add_numbers(valA, valB):
    if not (isinstance(valA, int) and isinstance(valB, int)):
        raise TypeError("Input must be integer")
    return valA + valB


if __name__ == "__main__":
    intA = int(input("Enter first integer: "))
    intB = int(input("Enter second integer: "))

    print(f"Sum of {intA} and {intB}: {add_numbers(intA, intB)}")