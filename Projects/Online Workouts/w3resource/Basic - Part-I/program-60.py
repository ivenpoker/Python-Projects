# !/usr/bin/env  python3

###################################################################################
#                                                                                 #
#       Program purpose: Calculates the hypotenuse of a right angled triangle.    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                    #
#       Creation Date  : August 10, 2019                                          #
#                                                                                 #
###################################################################################


def compute_hypotenuse(sideA, sideB):
    import math
    return math.sqrt(math.pow(int(sideA), 2) + math.pow(int(sideB), 2))

if __name__ == "__main__":
    sideA = int(input("Enter value for side A: "))
    sideB = int(input("Enter value for side B: "))

    print(f"Hypotenuse is: {int(compute_hypotenuse(sideA=sideA, sideB=sideB))}")
