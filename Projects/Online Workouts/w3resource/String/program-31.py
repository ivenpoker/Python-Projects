#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Print a floating point number to 2 decimal places with sign. #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 17, 2019                                             #
#                                                                                     #
#######################################################################################

def obtain_user_data(input_mess: str):
    is_valid = False
    user_data = float(0)
    while is_valid is False:
        try:
            user_data = float(input(input_mess))
            is_valid = True
        except RuntimeError as re:
            print(f"[ERROR]: {re}")
    return user_data

if __name__ == "__main__":
    user_float = obtain_user_data(input_mess='Enter some floating point number: ')
    print(f"Float number '{user_float}' with sign (2 d.p): {user_float:+.2f}")
