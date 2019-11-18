#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Checks if all items of a list is equal to a given string.         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

def do_checking(main_list: list, key_str: str) -> bool:
    return all(temp_str == key_str for temp_str in main_list)

if __name__ == "__main__":

    color1 = ["green", "orange", "black", "white"]
    color2 = ["green", "green", "green", "green"]

    print(f'Check in color1 ... [{"YES" if do_checking(main_list=color1, key_str="green") else "NO"}]')
    print(f'Check in color2 ... [{"YES" if do_checking(main_list=color2, key_str="green") else "NO"}]')

