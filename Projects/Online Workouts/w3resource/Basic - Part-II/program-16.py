#!/usr/bin/env  python3

########################################################################
#                                                                      #
#       Program purpose: Get the third side of right angled triangle   #
#                        from two given sides.                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>         #
#       Creation Date  : September 6, 2019                             #
#                                                                      #
########################################################################

import math

def pythagoras(opposite_side=0, adjacent_side=0, hypotenuse=0):
    if opposite_side == str('x'):
        return f"Opposite = {math.sqrt(math.pow(float(hypotenuse), 2) - math.pow(float(adjacent_side), 2))}"
    elif adjacent_side == str('x'):
        return f"Adjacent = {math.sqrt(math.pow(float(hypotenuse), 2) - math.pow(float(opposite_side), 2))}"
    elif hypotenuse == str('x'):
        return f"Hypotenuse = {math.sqrt(math.pow(float(opposite_side), 2) + math.pow(float(adjacent_side), 2))}"
    else:
        return "You know the answer!"

if __name__ == "__main__":

    cont = True
    sideA = 0
    sideB = 0
    while cont:
        try:
            sideA = int(input("Enter value for side A: "))
            cont = False
        except ValueError as re:
            print("Invalid input. Try again.")
    cont = True
    while cont:
        try:
            sideB = int(input("Enter value for side B: "))
            cont = False
        except ValueError as re:
            print("Invalid input: Try again.")

    print(pythagoras(opposite_side=sideA, adjacent_side=sideB, hypotenuse='x'))
    print(pythagoras(opposite_side='x', adjacent_side=sideA, hypotenuse=sideB))
    print(pythagoras(opposite_side=sideA, adjacent_side='x', hypotenuse=sideB))

