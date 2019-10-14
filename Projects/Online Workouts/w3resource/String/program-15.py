#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Adds HTML string tags around word(s) in text.                #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 14, 2019                                             #
#                                                                                     #
#######################################################################################

def get_user_data(mess: str):
    is_valid = False
    user_data = ''
    while is_valid is False:
        try:
            user_data = input(mess)
            if len(user_data) == 0:
                raise ValueError('Please enter some string')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def add_tags(tag_name: str, tag_data: str):
    return f'<{tag_name}>{tag_data}</{tag_name}>'

def process_words(data: str, tag_name: str):
    new_data = []
    for word in data.split():
        new_data.append(add_tags(tag_name=tag_name, tag_data=word.strip()))
    return new_data

if __name__ == "__main__":
    main_data = get_user_data(mess='Enter some text: ')
    tag_name = get_user_data(mess='Enter tag name around words: ')
    proc_data = process_words(data=main_data, tag_name=tag_name)
    print(f'Processed data: {proc_data}')

