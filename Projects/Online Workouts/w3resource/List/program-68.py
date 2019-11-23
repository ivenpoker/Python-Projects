#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Removes duplicates in a list.                                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 23, 2019                                                 #
#                                                                                          #
############################################################################################

def remove_duplicates(core_list: list) -> list:
    temp_list = []
    for data in core_list:
        if data not in temp_list:
            temp_list.append(data)
    return temp_list

if __name__ == "__main__":
    main_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    print(f'Main list is: {main_list}')
    print(f'After removing duplicates: {remove_duplicates(core_list=main_list)}')