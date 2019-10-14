#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Reverses a string if it's length is a multiple of 4.         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 14, 2019                                             #
#                                                                                     #
#######################################################################################

def obtain_user_data(input_mess: str):
    is_valid = False
    user_str = ''
    while is_valid is False:
        try:
            user_str = input(input_mess)
            if len(user_str) == 0:
                raise ValueError('Please provide a string')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_str


def reverse_string(main_data: str, mult: int):
    if int(len(main_data)) % mult == 0:
        return main_data[::-1]
    else:
        return main_data

if __name__ == "__main__":
    user_data = obtain_user_data(input_mess='Enter some string: ')
    print(f'Reversed string: {reverse_string(main_data=user_data, mult=4)}')
    print(f"Reverse of string 'abcd': {reverse_string(main_data='abcd', mult=4)} ")