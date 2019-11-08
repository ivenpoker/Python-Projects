#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Find the list of words that are longer than n from a given list   #
#                        of words.                                                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 8, 2019                                                  #
#                                                                                          #
############################################################################################

def obtain_user_input(input_mess: str) -> str:
    is_valid, user_data = False, ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Oops, data needed!')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def do_processing(str_data: str, min_n: int) -> str:
    str_data = str_data.split()
    new_data = []
    for word in str_data:
        if len(word.strip()) <= min_n:
            new_data.append(word)
    return ' '.join(new_data)

if __name__ == "__main__":
    input_data = obtain_user_input(input_mess='Enter some string input: ')
    n_val = int(-1)

    while n_val < 0:
        try:
            n_val = int(input("Enter the 'n' value: "))
            if n_val < 0:
                raise ValueError("Only positive 'n' value works!")
        except ValueError as ve:
            print(f'[ERROR]: {ve}')

    new_val_data = do_processing(str_data=input_data, min_n=n_val)
    print(f'After processing, data is: {new_val_data}')
