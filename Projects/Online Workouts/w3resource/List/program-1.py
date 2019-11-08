#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Sums the contents of a list.                                      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 8, 2019                                                  #
#                                                                                          #
############################################################################################

import random

def obtain_random_list(low: int, high: int, size: int) -> list:
    new_data = []
    for x in range(size):
        new_data.append(random.randint(low, high))
    return new_data

def sum_list_data(some_list: list) -> int:
    new_sum = 0
    for x in some_list:
        new_sum += x
    return new_sum

if __name__ == "__main__":
    data = obtain_random_list(low=0, high=100, size=20)
    print(f'Random data: {data}')

    """
    Test if out defined function is working well, by checking if the 
    result of the function is same as that of the build-in function 
    'sum'
    """

    if sum_list_data(some_list=data) == sum(data):
        print(f'Test status: PASSED, sum: {sum_list_data(some_list=data)}')
    else:
        print(f'Test status: FAILED, user defined function not working!')
