#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Formats a number with a percentage.                          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 17, 2019                                             #
#                                                                                     #
#######################################################################################

def obtain_user_data(input_mess: str):
    is_valid = False
    main_data = float(0)
    while is_valid is not True:
        try:
            main_data = float(input(input_mess))
            is_valid = True
        except ValueError as ve:
            print(f"[ERROR]: {ve}")
    return main_data

if __name__ == "__main__":
    user_float = obtain_user_data(input_mess='Enter some decimal floating number: ')
    while user_float != float(0):
        print('-' * 60)
        print(f'Formatter number with percentage: {user_float:.2%}')
        print('-' * 60)
        user_float = obtain_user_data(input_mess='Enter some decimal floating number: ')
    print('-' * 60)
