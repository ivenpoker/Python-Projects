#!/usr/bin/env  python3

########################################################################################
#                                                                                      #
#       Program purpose: Create all possible stings from a user provided string        #                           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                         #
#       Creation Date  : September 4, 2019                                             #
#                                                                                      #
########################################################################################

import random

def find_all_combination(seq=None, list_size=1):
    if seq is None:
        return []
    tempList = []

    x = 0
    while x is not list_size:
        random.shuffle(seq)
        temp = ''.join(seq)
        if temp not in tempList:
            tempList.append(temp)
        x += 1
    return tempList


if __name__ == "__main__":

    stringList = list(input("Enter some string to find all combinations: "))
    data = find_all_combination(seq=stringList, list_size=len(stringList) * 10)
    print(f"Generated combinations [{len(data)}]:\n{data}")
