#!/usr/bin/env  python3

#######################################################################
#                                                                     #
#       Program purpose: Checks that the sum of three elements (each  #
#                        from an array) from three arrays is equal to #
#                        a target value.                              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>        #
#       Creation Date  : September 5, 2019                            #
#                                                                     #
#######################################################################

import random

MAX_LINE_LEN = 60

def random_integer_list(list_size=10):
    new_data = []
    for x in range(list_size):
        new_data.append(random.choice(seq=range(list_size)))
    return new_data

def find_sum_to_target(target, listA=[], listB=[], listC=[]):
    data = []  # list of tuples (triplets) whose sum equals 'target'

    for x in range(len(listA)):
        for y in range(len(listB)):
            for z in range(len(listC)):
                temp = int(listA[x]) + int(listB[y]) + int(listC[z])
                if temp == target:
                    data.append(tuple([listA[x], listB[y], listC[z]]))

    return data


if __name__ == "__main__":

    list_dataA = random_integer_list(list_size=10)
    list_dataB = random_integer_list(list_size=15)
    list_dataC = random_integer_list(list_size=20)


    print("-" * MAX_LINE_LEN)
    print(f"List A: {list_dataA}")
    print(f"List B: {list_dataB}")
    print(f"List C: {list_dataC}")
    print("-" * MAX_LINE_LEN)

    target_value = 12

    tuple_data = find_sum_to_target(target=target_value, listA=list_dataA,
                                    listB=list_dataB, listC=list_dataC)

    print(f"Triplets whose sum is {target_value}:\n{tuple_data}")


