#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Adds new members to a set.                                        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 20, 2019                                                 #
#                                                                                          #
############################################################################################

from random import randint

def random_set_data(low: int, high: int, size: int) -> set:
    if size < 0:
        raise ValueError("Invalid specified set size. Must be > 0")
    return set([randint(low, high) for _ in range(size)])

def add_data_to_set(main_set: set, low: int, high: int) -> set:
    cnt, max_num = 0, 5
    while True:  # add 5 random data
        if cnt == max_num:
            break
        temp = randint(low, high)
        if temp not in main_set:
            main_set.add(temp)
            cnt += 1
    return main_set

if __name__ == '__main__':
    new_set_data = random_set_data(low=0, high=1000, size=15)
    print(f'            New set data: {new_set_data}')

    # add five random data to set, using the 'add' method
    new_set_data = add_data_to_set(main_set=new_set_data, low=0, high=10)
    print(f'After adding 5 new items: {new_set_data}')
