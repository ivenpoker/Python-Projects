#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Accepts a hyphen-separated sequence of words as input from user   #
#                        and prints the words in a hyphen-separated sequence after sorting #
#                        them alphabetically.                                              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 01, 2020                                                 #
#                                                                                          #
############################################################################################

def obtain_user_data(input_str: str) -> str:
    user_data, valid = '', False
    while not valid:
        try:
            user_data = input(input_str)
            if len(user_data) == 0:
                raise ValueError("Oops, data needed!")
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def process_data(some_data: str) -> str:
    words = [x.strip() for x in some_data.split('-') if len(x.strip()) > 0]
    words = sorted(words)       # sorte the 'words'
    return '-'.join(words)

if __name__ == "__main__":

    main_data = obtain_user_data(input_str='Enter some hyphen-separated string: ')
    print(f'After processing and sorting: {process_data(some_data=main_data)}')