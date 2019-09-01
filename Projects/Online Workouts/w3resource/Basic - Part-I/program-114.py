# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Filters positive numbers from a list.                        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 1, 2019                                            #
#                                                                                     #
#######################################################################################

import random

def random_list(size=0):
    newList = []
    for x in range(size):
        newList.append(random.randrange(start=-size, stop=size, step=1))
    return newList

if __name__ == "__main__":

    # Generate random list (with random integers in it based on it's size)
    randList = random_list(size=10)
    print(f"Generated list: {randList}")

    # Now lets filter out the positive numbers
    positiveList = [x for x in randList if x >= 0]

    print(f"Positive from generated list: {positiveList}")