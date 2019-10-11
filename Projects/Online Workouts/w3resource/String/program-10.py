#!/usr/bin/env  python3

########################################################################################
#                                                                                      #
#       Program purpose: Change a given string to new string where the first and the   #
#                        last characters have been exchanged.                          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                         #
#       Creation Date  : October 11, 2019                                              #
#                                                                                      #
########################################################################################

def get_user_string(mess: str):
    is_valid = False
    data = ''
    while is_valid is False:
        try:
            data = input(mess)
            if len(data) == 0:
                raise ValueError('Please provide a string')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return data

def do_exchange(main_data: str):
    return main_data[-1:] + main_data[1:len(main_data)-1] + main_data[0]

if __name__ == "__main__":
    user_data = get_user_string(mess='Enter a string: ')
    new_data = do_exchange(main_data=user_data)
    print(f'Processed data: {new_data}')
