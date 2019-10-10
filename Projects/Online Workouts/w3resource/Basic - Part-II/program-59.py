#!/usr/bin/env  python3

######################################################################################
#                                                                                    #
#       Program purpose: Computes the area of the polygon.                           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                       #
#       Creation Date  : October 10, 2019                                            #
#                                                                                    #
######################################################################################

def poly_area(c):
    add = []
    for i in range(0, (len(c)-2), 2):
        add.append(c[i] * c[i + 3] - c[i + 1] * c[i + 2])
        add.append(c[len(c) - 2] * c[i] - c[len(c) - 1] * c[0]);
    return abs(sum(add) / 2)

if __name__ == "__main__":
    print(poly_area([1, 0, 0, 0, 1, 1, 3, 0, -1, 1]))
