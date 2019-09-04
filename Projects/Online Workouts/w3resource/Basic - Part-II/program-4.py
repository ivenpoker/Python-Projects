#!/usr/bin/env  python3

###########################################################################################
#                                                                                         #
#       Program purpose: Find unique triplets whose three elements gives the sum of zero  #
#                        from an array of integers.                                       #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                            #
#       Creation Date  : September 4, 2019                                                #
#                                                                                         #
###########################################################################################

import random

def random_integer_list(list_size=10, start=0, stop=10, step=1):
    list_data = []
    for x in range(list_size):
        list_data.append(random.randrange(start=start, stop=stop, step=step))
    return list_data

def find_triplets(list_data=None):
    if list_data is None:
        return []
    triplet_list = []

    for x in range(len(list_data)):
        for i in range(x+1, len(list_data), 1):
            if i + 2 <= len(list_data):
                val = int(list_data[x]) + int(list_data[i]) + int(list_data[i + 1])
                if val == 0:
                    temp_data = tuple([list_data[x], list_data[i], list_data[i+1]])
                    if temp_data not in triplet_list:
                        triplet_list.append(temp_data)
    return triplet_list

if __name__ == "__main__":

    random_list = random_integer_list(list_size=100, start=-2, stop=15, step=1)
    print(f"\nGenerated list: {random_list}")

    triplet_data = find_triplets(random_list)

    print(f"\nFound unique triplets: \n{triplet_data}")



