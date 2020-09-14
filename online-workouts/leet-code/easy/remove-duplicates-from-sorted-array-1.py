#!/usr/bin/env python3

#######################################################################################
#                                                                                     #
#       Program purpose: Removes duplicates element (leaving just a single one) using #
#                        O(1) memory algorithm.                                       #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 14, 2020                                           #
#                                                                                     #
#######################################################################################

from typing import List

def remove_duplicates(sorted_array: List[int]) -> None:
    for val in sorted_array:
        while sorted_array.count(val) > 1:
            sorted_array.remove(val)

if __name__ == "__main__":
    main_test = [1, 1, 1, 1]
    print("[BEFORE] main_test:", main_test)

    remove_duplicates(sorted_array=main_test)

    print("[AFTER] main_test:", main_test)