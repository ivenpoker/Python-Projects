# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Compute the product of a lit of integers (without a loop).   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 1, 2019                                            #
#                                                                                     #
#######################################################################################

import random
import functools

def random_list(size=0):
    newList = []
    for x in range(size):
        newList.append(random.randrange(start=-size, stop=size, step=1))
    return newList

if __name__ == "__main__":
    randomList = random_list(size=10)
    print(f"Generated List: {randomList}")

    listProduct = functools.reduce((lambda x, y: x * y), randomList)
    print(f"Product of numbers in list: {listProduct}")
