
# !/usr/bin/env  python3

##############################################################################
#                                                                            #
#       Program purpose: Checks elements that are not found in both list and #
#                        return the results.                                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>               #
#       Creation Date  : July 17, 2019                                       #
#                                                                            #
##############################################################################

# URL: https://www.w3resource.com/python-exercises/python-basic-exercises.php

def find_diff(listA, listB):
    diffList = []
    for x in listA:
        if x not in listB:
            diffList.append(x)
    return diffList


if __name__ == "__main__":
    aList = ["White", "Black", "Red"]
    bList = ["Red", "Green"]

    print(f"List A: {aList}\nList B: {bList}")
    print(f"Diff: {find_diff(listA=aList, listB=bList)}")
