#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Prints a user provided integer with '*' on the right of      #
#                        specified width.                                             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 17, 2019                                             #
#                                                                                     #
#######################################################################################

def obtain_user_data(input_mess: str):
    is_valid = False
    main_data = int(0)
    while is_valid is not True:
        try:
            main_data = int(input(input_mess))
            is_valid = True
        except ValueError as ve:
            print(f"[ERROR]: {ve}")
    return main_data

if __name__ == "__main__":
    user_int = obtain_user_data(input_mess='Enter some integer number [0 to quit]: ')
    while user_int is not 0:
        print('-' * 60)
        print(f"Formatted number (right padding [using '*'], width 2): {user_int:*< 3d}")
        print('-' * 60)
        user_int = obtain_user_data(input_mess='Enter some integer number [0 to quit]: ')

