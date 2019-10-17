#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Reverse words in a string.                                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 17, 2019                                             #
#                                                                                     #
#######################################################################################

def get_user_sentence(input_mess: str):
    is_valid = False
    user_data = ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Please enter a sentence (or string)')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def process_text(main_text: str):
    data = main_text.split()
    new_data = []
    for word in data:
        new_data.append(word.strip()[::-1])
    return ' '.join(new_data)

if __name__ == "__main__":
    user_text = get_user_sentence(input_mess='Enter some text: ')
    proc_data = process_text(main_text=user_text)
    print(f'New data is: {proc_data}')
