#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Print a floating point number to 2 decimal places.           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 17, 2019                                             #
#                                                                                     #
#######################################################################################

def get_user_data(input_mess: str):
    is_valid = False
    user_data = float(0)
    while is_valid is False:
        try:
            user_data = float(input(input_mess))
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

if __name__ == "__main__":
    user_float = get_user_data(input_mess='Enter some floating point number: ')
    print(f"Float number '{user_float}' to 2 decimal places: {user_float:.2f}\n")
