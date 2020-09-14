#!/usr/bin/env python3

#######################################################################################
#                                                                                     #
#       Program purpose: Removes specific value in array 'in place'.                  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 14, 2020                                           #
#                                                                                     #
#######################################################################################

from typing import List

def remove_element(nums: List[int], val: int) -> None:
    while True:
        try:
            nums.remove(val)
        except ValueError:
            break

if __name__ == "__main__":
    main_list, val = [3, 2, 2, 3], 3

    print(f"[BEFORE] main_list:", main_list)
    remove_element(nums=main_list, val=3)

    print("[AFTER] main_list:", main_list)
