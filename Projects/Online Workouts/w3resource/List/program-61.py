#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Create a list of dictionaries for a specified length.             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 23, 2019                                                 #
#                                                                                          #
############################################################################################

def obtain_user_nth_value(input_mess: str) -> int:
    is_valid, user_val = False, 0
    while is_valid is False:
        try:
            user_val = int(input(input_mess))
            if user_val < 0:
                raise ValueError('Invalid nth value')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_val


def create_list_of_n_dictionaries(n_val: int) -> list:
    if n_val < 0:
        raise ValueError("Invalid number of specified dictionaries")
    return [{} for _ in range(n_val)]

if __name__ == "__main__":
    nth_val = obtain_user_nth_value(input_mess='Enter user value: ')
    print(f'List data: {create_list_of_n_dictionaries(n_val=nth_val)}')
