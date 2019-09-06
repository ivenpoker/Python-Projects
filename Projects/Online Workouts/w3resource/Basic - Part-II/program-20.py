#!/usr/bin/env  python3

##############################################################################
#                                                                            #
#       Program purpose: Finds the number of zeros at the end of a factorial #
#                        of a given positive number.                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>               #
#       Creation Date  : September 6, 2019                                   #
#                                                                            #
##############################################################################

def fact_end_zero(num):
    x = num // 5
    y = x
    while x > 0:
        x /= 5
        y += int(x)
    return y

if __name__ == "__main__":

    print(fact_end_zero(5))
    print(fact_end_zero(12))
    print(fact_end_zero(100))
