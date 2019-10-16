#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Checks if a string starts with some specified character(s).  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 16, 2019                                             #
#                                                                                     #
#######################################################################################

def read_user_message(mess: str):
    is_valid = False
    user_str = ''
    while is_valid is not True:
        try:
            user_str = input(mess)
            if len(user_str) is 0:
                raise ValueError('Please provide some string to work with')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_str

if __name__ == "__main__":

    main_string = read_user_message(mess='Enter some string: ')
    start_string = read_user_message(mess='Enter string to check: ')
    print(f"Does '{main_string}' starts with '{start_string}': "
          f"{'YES' if main_string.startswith(start_string) else 'NO'}")
