#!/usr/bin/env  python3

###########################################################################################
#                                                                                         #
#       Program purpose: Compute sum of digits of a given string.                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                            #
#       Creation Date  : October 30, 2019                                                 #
#                                                                                         #
###########################################################################################

def obtain_user_data(input_mess: str) -> str:
    is_valid, user_data = False, ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Please provide some string data to work with')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def compute_sum_of_digits_in_string(main_str: str) -> int:
    digit_sum = int(0)
    for char in main_str:
        if str.isdigit(char):
            digit_sum += int(char)
    return digit_sum

if __name__ == "__main__":
    main_data = obtain_user_data(input_mess='Enter a string to compute sum of digits within it: ')
    new_sum = compute_sum_of_digits_in_string(main_str=main_data)
    print(f'Sum of digits in string: {new_sum}')