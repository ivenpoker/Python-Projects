# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Sum of all counts in a collection.                           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 2, 2019                                            #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":
    import collections
    sumNum = [2, 2, 4, 6, 6, 8, 6, 10, 4]
    print(sum(collections.Counter(sumNum).values()))
