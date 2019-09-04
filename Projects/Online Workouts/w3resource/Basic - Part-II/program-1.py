#!/usr/bin/env python3

########################################################################################
#                                                                                      #
#       Program purpose: Takes a sequence of numbers and determines if all the numbers #
#                        are different from each other.                                #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                         #
#       Creation Date  : September 4, 2019                                             #
#                                                                                      #
########################################################################################

import random

def create_random_list(size=10):
    """
    Generates of random list with size, made of random integers

    :param size: Size of the list to generate
    :return: List of integers with random data (based on size of list)
    """
    mainList = []
    for i in range(size):
        mainList.append(random.choice(range(size)))     # append random integers based on 'size'
    return mainList

def items_unique_1(seq=None):
    if seq is None:
        return True
    tmpList = []
    for x in seq:
        if x in tmpList:
            return False
        else:
            tmpList.append(x)
    return True

def items_unique_2(seq=None):
    if seq is None:
        return True
    return len(seq) == len(set(seq))

if __name__ == "__main__":
    listA = create_random_list(size=15)
    listB = [1, 2, 3, 4, 5]

    print(f"List-A: {listA}")
    print(f"List-B: {listB}")
    print(f"Does list have unique elements: {'YES' if items_unique_1(listA) else 'NO'}")
    print(f"Does list have unique elements: {'YES' if items_unique_1(listB) else 'NO'}")

    print("\n---------------------------------\n")

    # using a different formula

    print(f"List-A: {listA}")
    print(f"List-B: {listB}")
    print(f"Does list have unique elements: {'YES' if items_unique_2(listA) else 'NO'}")
    print(f"Does list have unique elements: {'YES' if items_unique_2(listB) else 'NO'}")

