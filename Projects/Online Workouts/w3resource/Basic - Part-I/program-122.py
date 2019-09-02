# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Empty a variable without destroying it.                      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 2, 2019                                            #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":
    n = 20
    d = {"x": 200}
    l = [1, 3, 5]
    t = (5, 7, 8)

    print(type(n)())
    print(type(d)())
    print(type(l)())
    print(type(t)())