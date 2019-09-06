#!/usr/bin/env  python3

##########################################################################
#                                                                        #
#       Program purpose: Finds the value of n where n degrees of number  #
#                        2 are written sequentially in a line without    #
#                        spaces.                                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>           #
#       Creation Date  : September 6, 2019                               #
#                                                                        #
##########################################################################

def n_degrees(num):
    ans = True
    n, tempn, i = 2, 2, 2
    while ans:
        if str(tempn) in num:
            i += 1
            tempn = pow(n, i)
        else:
            ans = False
    return i - 1

if __name__ == "__main__":
    print(n_degrees("2481632"))
    print(n_degrees("248163264"))
