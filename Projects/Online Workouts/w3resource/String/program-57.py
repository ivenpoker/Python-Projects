#########################################################################################
#                                                                                       #
#       Program purpose: Remove spaces from a given string.                             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                          #
#       Creation Date  : October 25, 2019                                               #
#                                                                                       #
#########################################################################################

def obtain_user_input(input_mess: str):
    is_valid, user_data = False, ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Please enter a string or sentence to work with')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def remove_string_spaces(main_str: str):
    main_str = main_str.replace(' ', '')
    return main_str

if __name__ == "__main__":
    main_data = obtain_user_input(input_mess='Enter a sentence: ')
    print(f'Removed spaces: {remove_string_spaces(main_str=main_data)}')