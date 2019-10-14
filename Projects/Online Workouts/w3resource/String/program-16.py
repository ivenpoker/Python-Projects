#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Inserts a string in the middle of another string.            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 14, 2019                                             #
#                                                                                     #
#######################################################################################

def get_user_data(mess: str):
    is_valid = False
    user_data = ''
    while is_valid is False:
        try:
            user_data = input(mess)
            if len(user_data) == 0:
                raise ValueError('Please enter some string')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def place_text_in_middle(main_text: str, middle_text: str):
    return main_text[:int(len(main_text)/2)] + middle_text + main_text[int(len(main_text)/2):]

if __name__ == "__main__":
    main_data = get_user_data(mess='Enter main text: ')
    middle_data = get_user_data(mess='Enter middle text: ')
    print(f'Processed data: {place_text_in_middle(main_text=main_data, middle_text=middle_data)}')