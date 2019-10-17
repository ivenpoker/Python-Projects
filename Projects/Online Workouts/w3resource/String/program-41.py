#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Strip a set of characters from a string.                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 17, 2019                                             #
#                                                                                     #
#######################################################################################

def get_user_string(input_mess: str):
    is_valid = False
    user_data = ''
    while is_valid is not True:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Please provide some text')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data


if __name__ == "__main__":
    main_str = get_user_string(input_mess='Enter some message: ')
    strip_chars = get_user_string(input_mess='Enter sub-string to strip of message: ')
    print(f'After doing the stripping: {main_str.strip(strip_chars)}')