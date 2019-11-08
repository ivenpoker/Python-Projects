#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Determines if a list is empty or not.                             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 8, 2019                                                  #
#                                                                                          #
############################################################################################

def is_list_empty(list_data: list) -> bool:
    return len(list_data) == 0

if __name__ == "__main__":

    list_a = [1, 2]
    list_b = [4, 4, ""]
    list_c = []
    list_d = []

    print(f'Is list A empty ?: {"YES" if is_list_empty(list_data=list_a) else "NO"}')
    print(f'Is list B empty ?: {"YES" if is_list_empty(list_data=list_b) else "NO"}')
    print(f'Is list C empty ?: {"YES" if is_list_empty(list_data=list_c) else "NO"}')
    print(f'Is list D empty ?: {"YES" if is_list_empty(list_data=list_d) else "NO"}')
