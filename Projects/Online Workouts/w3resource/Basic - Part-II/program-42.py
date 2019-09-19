#!/usr/bin/env python3

###################################################################################
#                                                                                 #
#       Program purpose: Accepts six numbers as input and sorts them in ascending #
#                        order.                                                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                    #
#       Creation Date  : September 10, 2019                                       #
#                                                                                 #
###################################################################################

def read_numbers(size=0):
    valid = False
    int_list = []
    while not valid:
        try:
            int_list = list(input("Enter six numbers: ").split(' '))
            if len(int_list) != size:
                raise ValueError(f"invalid number of integers. Must be {size}")
            int_list = list(map(int, int_list))
            valid = True
        except ValueError as ve:
            print(f"[ERROR]: {ve}")
    return sorted(int_list, reverse=True)


if __name__ == "__main__":
    some_list = read_numbers(size=6)
    print(f"List of ints is: {some_list}")

