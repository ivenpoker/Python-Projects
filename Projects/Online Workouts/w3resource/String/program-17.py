#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Gets a string made of 4 copies of the last two characters of #
#                        a specified string (length must be at least 2).              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 14, 2019                                             #
#                                                                                     #
#######################################################################################

def obtain_user_data(input_mess: str):
    is_valid = False
    user_data = ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) < 2:
                raise ValueError('Please enter some string (length >= 2)')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def process_data(main_str: str):
    return main_str[-2:] * 4

if __name__ == "__main__":
    user_data = obtain_user_data(input_mess='Enter a string: ')
    proc_data = process_data(main_str=user_data)
    print(f'Processed data: {proc_data}')
