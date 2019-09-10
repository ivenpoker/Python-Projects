#!/usr/bin/env  python3

#################################################################################
#                                                                               #
#       Program purpose: Determines if sides of a triangle forms a right angle  #
#                        triangle.                                              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                  #
#       Creation Date  : September 10, 2019                                     #
#                                                                               #
#################################################################################

if __name__ == "__main__":

    int_num = list(map(int, input("Enter three integers (sides of a triangle): ").split()))
    x, y, z = sorted(int_num)
    if pow(x, 2) + pow(y, 2) == pow(z, 2):
        print("That is a right angle triangle")
    else:
        print("That isn't a right angle triangle")
