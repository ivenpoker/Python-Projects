#!/usr/bin/env  python3

#############################################################################
#                                                                           #
#       Program purpose: Checks if the number of occurrences of '4' in list #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>              #
#       Creation Date  : July 14, 2019                                      #
#                                                                           #
#############################################################################

# URL: https://www.w3resource.com/python-exercises/python-basic-exercises.php


def find_count(some_list, key):
    cnt = 0
    for x in some_list:
        if x == key:
            cnt += 1
    return cnt


if __name__ == "__main__":
    list1 = [1, 2, 4, 5, 3, 2, 0, 33, 55, 1, 4, 5, 3, 4]
    list2 = [3, 4, 5, 6, 7, 8]
    list3 = [8, 0, 9]

    print(f"list1: {list1} -- Number of 4's: {find_count(list1, 4)}")
    print(f"list2: {list2} -- Number of 4's: {find_count(list2, 4)}")
    print(f"list3: {list3} -- Number of 4's: {find_count(list3, 4)}")

