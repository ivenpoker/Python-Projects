#!/usr/bin/env  python3

#################################################################################
#                                                                               #
#       Program purpose: Finds the solution to simultaneous equation.           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                  #
#       Creation Date  : September 16, 2019                                     #
#                                                                               #
#################################################################################

if __name__ == "__main__":
    print("Enter the values of a, b, c, d, e, f: ", end="")
    a, b, c, d, e, f = map(float, input().split())
    n = a * e - b * d
    print("Values of x and y: ")
    if n != 0:
        x = (c * e - b * f) / n
        y = (a * f - c * d) / n
        print(f"Solution is: {x + 0:.3f}, {y + 0:.3f}")

