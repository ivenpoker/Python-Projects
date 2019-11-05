#!/usr/bin/env  python 3

##############################################################################################
#                                                                                            #
#       Program purpose: Moves all spaces to the front of a given string in single traversal #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                               #
#       Creation Date  : November 5, 2019                                                    #
#                                                                                            #
##############################################################################################

def retrieve_user_data(input_mess: str) -> str:
    is_valid, user_data = False, ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Oops, data needed')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def do_the_processing(main_str: str) -> str:
    char_no_spaces = [char for char in main_str if char != ' ']
    space = len(main_str) - len(char_no_spaces)

    # Create string with spaces
    result = ' ' * space
    return result + ''.join(char_no_spaces)

if __name__ == "__main__":
    user_input = retrieve_user_data(input_mess='Enter some string data: ')
    print(f'After processing: {do_the_processing(main_str=user_input)}')