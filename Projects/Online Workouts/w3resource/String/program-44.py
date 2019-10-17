#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Prints the index of character(s) in a string.                #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 17, 2019                                             #
#                                                                                     #
#######################################################################################

def get_user_text(input_mess: str):
    is_valid = False
    user_data = ''
    while is_valid is not True:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Please provide some data')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def print_info(main_data: str):
    for ind in range(len(main_data)):
        print(f'Current character {main_data[ind]} position {ind}')

if __name__ == "__main__":
    user_text = get_user_text(input_mess='Enter some text: ')
    print_info(main_data=user_text)
