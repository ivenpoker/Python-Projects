#!/usr/bin/env  python3

######################################################################################
#                                                                                    #
#       Program purpose: Creates a single string from two given strings, separated   #
#                        by a space and swap the first two characters of each string #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                       #
#       Creation Date  : October 10, 2019                                            #
#                                                                                    #
######################################################################################

def get_input_from_user(mess: str):
    is_valid = False
    data = ''
    while is_valid is False:
        try:
            data = input(mess)
            if len(data) == 0:
                raise ValueError('Please enter a string')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return data

def process_data(str_A: str, str_B: str):
    temp = str_A[0] + str_A[1]
    str_A = str_B[0] + str_B[1] + str_A[2:]
    str_B = temp + str_B[2:]

    return f'{str_A} {str_B}'


if __name__ == "__main__":

    first_str = get_input_from_user(mess='Enter first string: ')
    second_str = get_input_from_user(mess='Enter second string: ')
    print(f'Processed data is: {process_data(str_A=first_str, str_B=second_str)}')
