#!/usr/bin/env  python3

######################################################################################
#                                                                                    #
#       Program purpose: Count the occurrences of each character in a string.        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                       #
#       Creation Date  : October 10, 2019                                            #
#                                                                                    #
######################################################################################

def get_user_string(mess: str):
    user_str = ''
    cont = True
    while cont:
        try:
            user_str = input(mess)
            if len(user_str) == 0:
                raise ValueError("Please provide a string")
            cont = False
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_str

def count_chars_occurrence(main_str: str):
    data = {}
    for ch in main_str:
        if ch in data.keys():
            data[ch] += 1
        else:
            data[ch] = 1
    return data

if __name__ == "__main__":
    string = get_user_string(mess='Enter some string: ')
    print(f'Processed data: {count_chars_occurrence(main_str=string)}')
