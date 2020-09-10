#!/usr/bin/env python3

#######################################################################################
#                                                                                     #
#       Program purpose: Create a phone number structure from a list of numbers.      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 10, 2020                                           #
#                                                                                     #
#######################################################################################

def create_phone_number(nums: list) -> str:
    seg_1 = ''.join([f'{x}' for x in nums[0:3]])
    seg_2 = ''.join([f'{x}' for x in nums[3:6]])
    seg_3 = ''.join([f'{x}' for x in nums[6:]])
    return f"({seg_1}) {seg_2}-{seg_3}"


if __name__ == "__main__":
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

