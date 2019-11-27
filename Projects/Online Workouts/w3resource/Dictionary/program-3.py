#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Concatenates dictionaries.                                        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 27, 2019                                                 #
#                                                                                          #
############################################################################################

import operator
import random

def random_dict(low: int, high: int, size: int) -> dict:
    if size < 0:
        raise ValueError(f'Invalid size [{size}] for dictionary')
    key_data = [random.randint(low, high) for _ in range(size)]
    value_data = [random.randint(low, high) for _ in range(size)]

    return {k: v for (k, v) in zip(key_data, value_data)}

def concat_dict(dict_A: dict, dict_B: dict) -> dict:
    final_dict = {k: v for (k, v) in zip(dict_A.keys(), dict_A.values())}
    for (k, v) in zip(dict_B.keys(), dict_B.values()):
        final_dict[k] = v
    return dict(sorted(final_dict.items(), key=operator.itemgetter(0)))

if __name__ == "__main__":
    rand_dict_A = random_dict(low=0, high=10, size=5)
    rand_dict_B = random_dict(low=11, high=20, size=5)

    print(f'Random dictionary A: {rand_dict_A} --> [size: {len(rand_dict_A)}]')
    print(f'Random dictionary B: {rand_dict_B} --> [size: {len(rand_dict_B)}]')

    merged_dict = concat_dict(dict_A=rand_dict_A, dict_B=rand_dict_B)
    print(f'Concatenated (and sorted) merge: {merged_dict} --> [size: {len(merged_dict)}]')

