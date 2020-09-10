#!/usr/bin/env python3

#######################################################################################
#                                                                                     #
#       Program purpose: Given an array of integer list items, finds the first index  #
#                        within the array where the sum of all elements to the left   #
#                        of the index of the array equals does to the right of the    #
#                                                                                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 10, 2020                                           #
#                                                                                     #
#######################################################################################

def find_even_index(arr: list) -> int:
    eq_idx = -1
    for (idx, num) in enumerate(arr):
        fst_half = arr[0:idx]
        snd_half = arr[idx+1:]
        if sum(fst_half) == sum(snd_half):
            eq_idx = idx
            break
    return eq_idx

if __name__ == "__main__":
    print(find_even_index([10, -80 ,10, 10, 15, 35, 20]))


