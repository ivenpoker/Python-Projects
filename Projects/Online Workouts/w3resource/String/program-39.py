#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Reverses a user provided string.                             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 17, 2019                                             #
#                                                                                     #
#######################################################################################

def get_user_data(input_mess: str):
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

def reverse_string(main_str: str):
    main_str = main_str.strip()
    return main_str[::-1]

if __name__ == "__main__":
    main_data = get_user_data(input_mess='Enter some string to reverse: ')
    print(f'Reverse of main string: {reverse_string(main_str=main_data)}')
