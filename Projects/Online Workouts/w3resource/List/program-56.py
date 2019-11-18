#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Converts a string to a list.                                      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

def obtain_use_str(input_mess: str) -> str:
    user_data, is_valid = '', False
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Oops, data needed!')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def convert_str_to_list(main_str: str) -> list:
    return list(main_str)

if __name__ == "__main__":

    main_data = obtain_use_str(input_mess='Enter string to convert to list: ')
    list_str = convert_str_to_list(main_str=main_data)

    print(f'Conversion to list: {list_str}')


