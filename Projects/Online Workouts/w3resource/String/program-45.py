#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Checks if a string contains all letters of the alphabet.     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 17, 2019                                             #
#                                                                                     #
#######################################################################################

def check_all_alphabetic_chars(main_data: str):
    found_chars = []
    main_data = str.lower(main_data)

    for char in main_data:
        if char not in found_chars and str.isalpha(char):
            found_chars.append(char)
    return len(found_chars) == 26

if __name__ == "__main__":

    input_string_A = 'The quick brown fox jumps over the lazy dog'
    print(f"Does first string passes test: {'YES' if check_all_alphabetic_chars(main_data=input_string_A) else 'NO'}")

    input_string_B = 'The quick brown fox jumps over the lazy cat'
    print(f"Does second string passes test: {'YES' if check_all_alphabetic_chars(main_data=input_string_B) else 'NO'}")

