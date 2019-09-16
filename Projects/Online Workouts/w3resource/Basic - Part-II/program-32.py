#!/usr/bin/env  python3

#################################################################################
#                                                                               #
#       Program purpose: Finds top 'n' heights from a given sequence of heights #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                  #
#       Creation Date  : September 10, 2019                                     #
#                                                                               #
#################################################################################

import random

def random_integer_list(list_size=10):
    data = []
    for i in range(list_size):
        data.append(random.choice(seq=range(list_size)))
    return data

def find_big_three(data: list, max_size: int):
    if len(data) < max_size:
        return data
    if len(data) == max_size:
        return sorted(data, reverse=True)
    data = sorted(data, reverse=True)
    big_data = []
    for i in range(len(data)):
        if len(big_data) != max_size:
            big_data.append(data[i])
        else:
            big_data = sorted(big_data, reverse=True)
            for j in range(len(big_data)):
                if big_data[j] < data[i]:
                    big_data[j] = data[i]
                    break
    return big_data

if __name__ == "__main__":
    building_heights = random_integer_list(list_size=20)

    print(f"Building heights : {building_heights}")
    print(f"Top 3 heights: {find_big_three(building_heights, max_size=3)}")
    print(f"Top 4 heights: {find_big_three(building_heights, max_size=4)}")
    print(f"Top 5 heights: {find_big_three(building_heights, max_size=5)}")

