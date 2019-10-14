#!/usr/bin/env  python3

########################################################################################
#                                                                                      #
#       Program purpose: Returns a string made of its first three characters of a      #
#                        a specified string. If the length is less than 3,the original #
#                        string is returned.                                           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                         #
#       Creation Date  : October 14, 2019                                              #
#                                                                                      #
########################################################################################

def obtain_user_data(input_mess: str):
    is_valid = False
    user_data = ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Please provide a string')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def process_data(data: str):
    if len(data) <= 3:
        return data
    return data[:3]

if __name__ == "__main__":
    main_data = obtain_user_data(input_mess='Enter some string: ')
    proc_data = process_data(data=main_data)
    print(f'Processed data: {proc_data}')