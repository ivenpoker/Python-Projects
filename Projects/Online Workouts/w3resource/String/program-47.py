#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Convert the first n characters of a string to lowercase.     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 24, 2019                                             #
#                                                                                     #
#######################################################################################

def get_user_data(mess: str):
    is_valid = False
    user_data = ''
    while is_valid is False:
        try:
            user_data = input(mess)
            if len(user_data) == 0:
                raise ValueError('Please provide a string to work with.')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def lower_first_n_characters(main_str: str, n_val: int):
    if len(main_str) < n_val:
        return
    return f'{str.upper(main_str[:n_val])}{main_str[n_val:]}'

if __name__ == "__main__":
    main_data = get_user_data(mess='Enter some string: ')
    max_len = -1

    while max_len < 0:
        try:
            max_len = int(get_user_data(mess='How many number of characters to lower: '))
        except ValueError as ve:
            print(f'[ERROR]: {ve}')

    new_data = lower_first_n_characters(main_str=main_data, n_val=max_len)
    print(f'String with first {max_len} character(s) lowered: {lower_first_n_characters(main_str=main_data, n_val=max_len)}')