#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Gets the Fibonacci series between 0 to 50.                        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 21, 2019                                                  #
#                                                                                          #
############################################################################################

def compute_fibonacci_till_max(max_num: int) -> list:
    list_nums, curr = [0, 1], 1
    while curr < max_num:
        list_nums.append(curr)
        temp_len = len(list_nums)
        curr = list_nums[temp_len-2] + list_nums[temp_len-1]
    return list_nums

if __name__ == "__main__":
    num_list = compute_fibonacci_till_max(max_num=50)
    print(f'Numbers are: {num_list}')
