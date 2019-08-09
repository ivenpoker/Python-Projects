# !/usr/bin/env  python3

################################################################################
#                                                                              #
#       Program purpose: Does some computation based on some formula           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                 #
#       Creation Date  : August 9, 2019                                        #
#                                                                              #
################################################################################

def doComputation(x, y):
    import math
    return math.pow((int(x) + int(y)), 2)


if __name__ == "__main__":
    xVal = int(input("Enter value for x: "))
    yVal = int(input("Enter value for y: "))

    print(f"Computation results: {doComputation(x=xVal, y=yVal)}")