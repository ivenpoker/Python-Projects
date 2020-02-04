#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Finds whether a given string starts with a given character using  #
#                        lambda.                                                           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 04, 2020                                                 #
#                                                                                          #
############################################################################################

def obtain_user_data(input_mess) -> str:
    user_data, valid = '', False
    while not valid:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError("Oops, data needed")
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

if __name__ == "__main__":

    lambda_func = lambda data, search: True if data.startswith(search) else False

    main_str = obtain_user_data(input_mess='Enter main string: ')
    search_str = obtain_user_data(input_mess='Enter search string: ')

    print(f"Search 'startswith' found: {lambda_func(main_str, search_str)}")
