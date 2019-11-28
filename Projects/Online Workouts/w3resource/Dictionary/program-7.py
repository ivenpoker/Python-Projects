#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Generates and prints a dictionary that contains a number in range #
#                        1 and 15 (both included) and the values are square of keys.       #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 28, 2019                                                 #
#                                                                                          #
############################################################################################

def find_keys(some_dict: dict) -> dict:
    range_dict = dict()
    for temp_key in some_dict.keys():
        if 1 <= temp_key <= 15 and some_dict[temp_key] == pow(temp_key, 2):
            range_dict[temp_key] = some_dict[temp_key]
    return range_dict

def N_generate_dict(max_n: int) -> dict:
    return {x: pow(x, 2) for x in range(1, max_n+1)}

if __name__ == "__main__":

    demo_dict = N_generate_dict(max_n=15)
    print(f'Generated dictionary: {demo_dict}')

    print(f'Keys withing the range: {find_keys(some_dict=demo_dict)}')