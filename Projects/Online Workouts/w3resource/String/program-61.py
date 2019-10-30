#!/usr/bin/env  python3

###########################################################################################
#                                                                                         #
#       Program purpose: Remove duplicate characters from a given string.                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                            #
#       Creation Date  : October 30, 2019                                                 #
#                                                                                         #
###########################################################################################

def get_user_data(input_mess: str) -> str:
    is_valid, user_data = False, ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Please enter some data')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def remove_duplicate_char(main_str: str) -> str:
    from collections import OrderedDict
    return ''.join(OrderedDict.fromkeys(main_str))

if __name__ == "__main__":
    main_data = get_user_data(input_mess='Enter a word (or sentence): ')
    new_data = remove_duplicate_char(main_str=main_data)
    print(f'After removing duplicates: {remove_duplicate_char(main_str=new_data)}')
