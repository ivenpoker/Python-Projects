#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Prints a list except for the first 5 elements, where the values   #
#                        of numbers between 1 and 30 (both included).                      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 11, 2019                                                 #
#                                                                                          #
############################################################################################

def do_the_computation(size: int) -> list:
    if size < 5:
        raise ValueError('Invalid size for list. Must be > 5')
    temp_list = []
    for i in range(size):
        if i in range(6, size):
            temp_list.append(i ** 2)
    return temp_list

if __name__ == "__main__":
    print(f'Generated data: {do_the_computation(size=21)}')
