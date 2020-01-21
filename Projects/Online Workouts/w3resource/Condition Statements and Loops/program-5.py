#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Reverses a string obtained from user.                             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 21, 2019                                                  #
#                                                                                          #
############################################################################################

def obtain_user_data(input_mess: str) -> str:
    user_data, valid = '', False
    while not valid:
        try:
            user_data = input(input_mess).strip()
            if len(user_data) == 0:
                raise ValueError(f"Oops! word needed")
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def reverse_word(main_word: str) -> str:
    return main_word[::-1]

if __name__ == "__main__":
    word = obtain_user_data(input_mess='Enter a word to reverse: ')
    print(f'Reverse of word is: {reverse_word(main_word=word)}')
