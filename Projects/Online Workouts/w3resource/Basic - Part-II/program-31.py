#!/usr/bin/env  python3

##############################################################################
#                                                                            #
#       Program purpose: Count the number of carry operations for each set   #
#                        of addition problems.                               #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>               #
#       Creation Date  : September 10, 2019                                  #
#                                                                            #
##############################################################################

def carry_number(x, y):
    ctr = 0
    if x == 0 and y == 0:
        return 0
    z = 0
    for i in reversed(range(10)):
        z = x % 10 + y % 10 + z
        if z > 9:
            z = 1
        else:
            z = 0
        ctr += z
        x //= 10
        y //= 10

    if ctr == 0:
        return "No carry operation."
    elif ctr == 1:
        return ctr
    else:
        return ctr

if __name__ == "__main__":
    print(carry_number(786, 457))
    print(carry_number(5, 6))