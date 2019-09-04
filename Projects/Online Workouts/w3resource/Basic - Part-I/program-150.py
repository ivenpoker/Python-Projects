#!/usr/bin/env python3

#######################################################################################
#                                                                                     #
#       Program purpose: Takes a positive integer and returns the sum of the cube of  #
#                        all the positive integers smaller than the specified number. #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 3, 2019                                            #
#                                                                                     #
#######################################################################################

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


def find_odd_pair_product(someList=None):
    """
    Find pair of integers in list whose product is odd,
     and returns a list of tuples, where a tuple is made up
    of both integers whose product is odd.

    :param someList: List to find pairs within.
    :return: List of pair-tuples.
    """
    listPair = []
    if someList is None:
        someList = []
    if len(someList) == 0:
        return []

    for i in range(len(someList)):
        for j in range(1, len(someList), 1):
            if (i * j) % 2 == 1:
                listPair.append((i, j))
    return listPair


if __name__ == "__main__":
    randList = create_random_list(size=15)
    print(f"Generated List is: {randList}")
    print(f"Odd pairs: {find_odd_pair_product(randList)}")
