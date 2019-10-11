#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Gets user input and prints it back in upper and lower case.  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 11, 2019                                             #
#                                                                                     #
#######################################################################################

def obtain_user_data(mess: str):
    is_valid = False
    data = ''
    while is_valid is False:
        try:
            data = input(mess)
            if len(data) == 0:
                raise ValueError('Please provide a string (or sentence)')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return data

if __name__ == "__main__":
    user_data = obtain_user_data(mess='Enter a string: ')
    print(f'String in uppercase: {user_data.upper()}')
    print(f'String in lowercase: {user_data.lower()}')
