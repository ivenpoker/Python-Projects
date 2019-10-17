#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Display a number in left, right and center aligned of width  #
#                        10.                                                          #
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
    user_int = obtain_user_data(input_mess='Enter some integer value [0 to quit]: ')
    while user_int != 0:
        print('-' * 60)
        print(f'Left aligned (width 10)    : {user_int:< 10d}')
        print(f'Right aligned (width 10)   : {user_int:10d}')
        print(f'Centered aligned (width 10): {user_int:^10d}')
        print('-' * 60)
        user_int = obtain_user_data(input_mess='Enter some integer value [0 to quit]: ')
    print('-' * 60)
