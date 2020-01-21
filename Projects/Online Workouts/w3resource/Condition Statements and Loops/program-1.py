#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Finds those numbers which are divisble by 7 and multiples of 5    #
#                        between 1500 and 2700                                             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 21, 2019                                                  #
#                                                                                          #
############################################################################################

def find_divisibles(valA: int, valB: int, lower_bound: int, upper_bound: int) -> list:
    if upper_bound <= lower_bound:
        raise ValueError("Invalid bounds! Upper must be < lower")
    nums = []
    for i in range(lower_bound, upper_bound):
        if i % valA == 0 and i % valB == 0:
            nums.append(i)
    return nums

if __name__ == "__main__":
    found_data = find_divisibles(valA=7, valB=5, lower_bound=1500, upper_bound=2700)
    print(f'Found values: {found_data}')
