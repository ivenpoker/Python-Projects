#!/usr/bin/env  python3

######################################################################################
#                                                                                    #
#       Program purpose: Creates a string from a given string where all occurrences  #
#                        of its first char have been changed with '$', except the    #
#                        first char itself.                                          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                       #
#       Creation Date  : October 10, 2019                                            #
#                                                                                    #
######################################################################################

def get_user_string(mess: str):
    is_valid = False
    data = ''
    while is_valid is False:
        try:
            data = input(mess)
            if len(data) == 0:
                raise ValueError("Please provide a string")
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return data

def process_data(data: str, repl: str):
    temp = data[1:].replace(data[0], repl)
    return data[0] + temp


if __name__ == "__main__":
    user_data = get_user_string(mess='Enter some string: ')
    new_data = process_data(data=user_data, repl='$')
    print(f'Processed data: {new_data}')
