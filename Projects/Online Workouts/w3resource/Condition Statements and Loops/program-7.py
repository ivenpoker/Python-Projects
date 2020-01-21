#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Constructs a pyramidal pattern, using nested for loop.            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 21, 2019                                                  #
#                                                                                          #
############################################################################################

def print_types(main_data: list) -> None:
    for item in main_data:
        print(f"Type of '{item}': {type(item)}")

if __name__ == "__main__":

    data_list = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {'class': 'V', 'section': 'A'}]
    print_types(main_data=data_list)
