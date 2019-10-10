#!/usr/bin/env  python3

######################################################################################
#                                                                                    #
#       Program purpose: Creates a string made of the first 2 and the last 2 chars   #
#                        from a given string. If the string length is less than 2,   #
#                        returns instead an empty string.                            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                       #
#       Creation Date  : October 10, 2019                                            #
#                                                                                    #
######################################################################################

def get_user_string(mess: str):
    is_valid = False
    data = ''
    while is_valid is False:
        try:
            data = input(mess)
            if len(data) == 0:
                raise ValueError("Please provide a string")
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return data

def process_data(main_data: str):
    if len(main_data) < 2:
        return ''
    return main_data[:2] + main_data[-2:]

if __name__ == "__main__":
    user_str = get_user_string('Enter some string: ')
    print(f'Processed data: {process_data(main_data=user_str)}')