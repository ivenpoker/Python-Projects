#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Converts a user provide string (or sentence) to a list.      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 17, 2019                                             #
#                                                                                     #
#######################################################################################

def obtain_user_data(input_mess: str):
    is_valid = False
    user_str = ''
    while is_valid is not True:
        try:
            user_str = input(input_mess)
            if len(user_str) == 0:
                raise ValueError('Please provide some text to work with')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_str

if __name__ == "__main__":
    user_data = obtain_user_data(input_mess='Enter some a sentence: ')
    print(f"Text data to list: {user_data.split(' ')}")