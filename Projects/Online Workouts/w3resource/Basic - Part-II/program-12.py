#!/usr/bin/env  python3

#######################################################################
#                                                                     #
#       Program purpose: Find all permutations of a list.             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>        #
#       Creation Date  : September 5, 2019                            #
#                                                                     #
#######################################################################

import random

def random_integer_list(list_size=10):
    data = []
    for i in range(list_size):
        data.append(random.choice(seq=range(list_size)))
    return data

def find_permutations(nums=None):
    if nums is None:
        return []

    result_perms = [[]]
    for n in nums:
        new_perms = []
        for perm in result_perms:
            for i in range(len(perm) + 1):
                new_perms.append(perm[:i] + [n] + perm[i:])
                result_perms = new_perms
    return result_perms

if __name__ == "__main__":

    random_list = random_integer_list(list_size=5)
    perms = find_permutations(nums=random_list)

    print(f"List: {random_list}")
    print(f"Permutations:\n{perms}")
