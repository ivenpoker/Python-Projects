#!/usr/bin/env python3

#############################################################################
#                                                                           #
#       Program purpose: Computes the area of the circle when given radius  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>              #
#       Creation Date  : 19/04/2019                                         #
#                                                                           #
#############################################################################

def compute_circle_area(_radius):
    import math
    return math.pi * math.pow(_radius, 2)

def main():
    radius = float(input("Enter cirlce's radius: "))
    print("Circle's are is: {}".format(compute_circle_area(radius)))

if __name__ == "__main__":
    main()