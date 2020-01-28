#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Determines if a letter is a vowel or a constant.                  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 28, 2019                                                  #
#                                                                                          #
############################################################################################

main_vowels = 'aeiou'

def obtain_user_char(input_mess: str) -> str:
    user_char, valid = '', False
    while not valid:
        try:
            user_char = input(input_mess).strip()
            if len(user_char) != 1:
                raise ValueError(f"Invalid input. Must be a single character")
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_char

def is_vowel(some_char: str) -> bool:
    return some_char.lower().isalpha() and some_char.lower() in main_vowels

if __name__ == "__main__":
    main_char = obtain_user_char(input_mess='Enter a letter of the alphabet: ')
    if is_vowel(some_char=main_char):
        print(f"{main_char} is a vowel")
    else:
        print(f"{main_char} is a constant")
