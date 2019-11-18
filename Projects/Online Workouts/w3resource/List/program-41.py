#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Creates multiple lists.                                           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

def obtain_user_size(input_mess: str) -> int:
    is_valid, user_data = False, int(-1)
    while is_valid is False:
        try:
            user_data = int(input(input_mess))
            if user_data < 0:
                raise ValueError('Invalid number of list.')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def create_multiple_lists(max_size: int) -> dict:
    obj = dict()
    for i in range(1, max_size+1):
        obj[str(i)] = []
    return obj

if __name__ == "__main__":

    user_size = obtain_user_size(input_mess='Enter max number of lists: ')
    multi_list = create_multiple_lists(max_size=user_size)
    print(f'Generated List:\n{multi_list}')
