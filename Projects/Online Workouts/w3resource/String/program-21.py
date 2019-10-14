#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Converts a string to all uppercase if it contains at least 2 #
#                        uppercase characters in the first 4 characters.              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 14, 2019                                             #
#                                                                                     #
#######################################################################################

def read_user_data(input_mess: str):
    is_valid = False
    user_data = ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Please enter some string')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def process_data(main_data: str):
    if len(main_data) < 4:
        return main_data
    else:
        temp, cnt = main_data[:4], 0
        for x in temp:
            if cnt >= 2: break
            if str.isupper(x):
                cnt += 1
        if cnt >= 2:
            return str.upper(main_data)
        else:
            return main_data

if __name__ == "__main__":
    user_str = read_user_data(input_mess='Enter a string: ')
    proc_data = process_data(main_data=user_str)
    print(f'Processed data: {process_data(main_data=proc_data)}')
