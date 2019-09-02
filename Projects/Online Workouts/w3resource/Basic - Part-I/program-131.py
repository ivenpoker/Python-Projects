# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Split variable length string into variables.                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 2, 2019                                            #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":
    varList = ['a', 'b', 'c']
    x, y, z = (varList + [None] * len(varList))[:len(varList)]
    print(x, y, z)
    varList = [100, 20.25]
    x, y = (varList + [None] * 2)[:2]
    print(x, y)
