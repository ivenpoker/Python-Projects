#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Sorts a string lexicographically.                            #
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
            if len(user_data) == 0:
                raise ValueError('Please provide an input')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def process_user_data(main_data: str):
    return sorted(list(main_data))

if __name__ == "__main__":
    user_str = obtain_user_data(input_mess='Enter some string: ')
    print(f'Lexicographically sorted data: {process_user_data(main_data=user_str)}')
