#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Adds 'ing' at the end of a user provided string (length is   #
#                        at least 3). If the given string already ends with 'ing'     #
#                        then add 'ly' instead. If the string of the the given string #
#                        is less than 3, it's left unchanged.                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 10, 2019                                             #
#                                                                                     #
#######################################################################################

def get_input_from_user(mess: str):
    is_valid = False
    data = ''
    while is_valid is False:
        try:
            data = input(mess)
            if len(data) == 0:
                raise ValueError('Please enter a string')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return data

def process_string(main_data: str):
    if len(main_data) < 3:
        return main_data
    if main_data[-3:] == "ing":
        return main_data + "ly"
    else:
        return main_data + "ing"


if __name__ == "__main__":
    main_str = get_input_from_user(mess='Enter some string: ')
    print(f'Processed data: {process_string(main_data=main_str)}')
