# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Create a bytearray from a list.                              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 1, 2019                                            #
#                                                                                     #
#######################################################################################

import random

def random_list(size=0):
    newList = []
    for x in range(size):
        newList.append(random.choice(range(size)))
    return newList


if __name__ == "__main__":
    print()

    # Create bytearray from list of integers.
    randomList = random_list(size=10)
    values = bytearray(randomList)

    for x in values:
        print(x)
    print()
