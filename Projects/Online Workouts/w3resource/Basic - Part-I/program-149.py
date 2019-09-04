#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Takes a positive integer and returns the sum of the cube of  #
#                        all the positive integers smaller than the specified number. #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 3, 2019                                            #
#                                                                                     #
#######################################################################################

import math

def find_sum_of_cubes(intVal):
    cubeSum = 0
    for i in range(1, intVal, 1):
        cubeSum += math.pow(i, 3)
    return cubeSum

if __name__ == "__main__":
    userInt = int(input("Enter some integer: "))
    print(f"Sum of cubes of all positive integer less than {userInt}: "
          f"{int(find_sum_of_cubes(userInt))}")
