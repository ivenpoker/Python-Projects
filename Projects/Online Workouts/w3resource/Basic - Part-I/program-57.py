# !/usr/bin/env  python3

###################################################################################
#                                                                                 #
#       Program purpose: Python program to get the execution time of a method.    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                    #
#       Creation Date  : August 14, 2019                                          #
#                                                                                 #
###################################################################################

import time

def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1, n+1):
        s = s + i
    end_time = time.time()
    return s, end_time - start_time

if __name__ == "__main__":
    n = 5
    print(f"\nTime to sum of 1 to {n} and required time to calculate is: {sum_of_n_numbers(n)}")