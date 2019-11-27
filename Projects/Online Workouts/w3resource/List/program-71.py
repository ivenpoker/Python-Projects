#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Checks if all dictionaries in list are empty.                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 27, 2019                                                 #
#                                                                                          #
############################################################################################

if __name__ == "__main__":

    my_list_A = [{}, {}, {}]
    my_list_B = [{1, 2}, {}, {}]

    print(f'All dictionaries empty in list A: {all(not d for d in my_list_A)}')
    print(f'All dictionaries empty in list B: {all(not d for d in my_list_B)}')
