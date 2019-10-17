#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Count number of occurrences of substring in a string.        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 17, 2019                                             #
#                                                                                     #
#######################################################################################

def obtain_user_string(input_mess: str):
    is_valid = False
    user_data = ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Please provide some input to work with')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def count_substring_occurrences(main_data: str, sub_str: str):
    return main_data.count(sub_str)

if __name__ == "__main__":

    user_string = obtain_user_string(input_mess='Enter some string: ')
    sub_string = obtain_user_string(input_mess='Enter substring to count: ')
    print(f"Number of occurrences of '{sub_string}': "
          f"{count_substring_occurrences(main_data=user_string, sub_str=sub_string)}")
