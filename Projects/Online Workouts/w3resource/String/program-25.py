#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Encrypts data using caesar cipher.                           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 16, 2019                                             #
#                                                                                     #
#######################################################################################

char_uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
char_lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def get_user_message(input_mess: str):
    is_valid = False
    user_data = ''
    while is_valid is not True:
        try:
            user_data = input(input_mess)
            if len(user_data) is 0:
                raise ValueError('Please provide some string to work with')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data


def caesar_encrypt(real_data: str, step: int):
    main_data = list(real_data)
    encrypted_text = []

    for char in main_data:

        if str.isupper(char):
            ind = char_uppercase.index(char)
            encrypt_ind = (ind + step) % len(char_uppercase)
            encrypted_text.append(char_uppercase[encrypt_ind])

        elif str.islower(char):
            ind = char_lowercase.index(char)
            encrypt_ind = (ind + step) % len(char_lowercase)
            encrypted_text.append(char_lowercase[encrypt_ind])
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text)


if __name__ == "__main__":

    real_text = get_user_message(input_mess='Enter text to encrypt: ')
    encrypt_step = int(get_user_message(input_mess='Enter step (integer) to use: '))
    encrypted_data = caesar_encrypt(real_data=real_text, step=encrypt_step)
    print(f'Encrypted text using Caesar cipher: {encrypted_data}')
