#!/usr/bin/env  python3

###########################################################################################
#                                                                                         #
#       Program purpose: Capitalize first and last letters of each word of a given string #                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                            #
#       Creation Date  : October 30, 2019                                                 #
#                                                                                         #
###########################################################################################

def obtain_user_input(input_mess: str) -> str:
    is_valid, user_data = False, ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Please enter some data to work with')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def process_sentence(main_str: str) -> str:
    new_data = main_str.split()
    final_data = []
    for word in new_data:
        if len(word) > 0:
            word = word.strip()
            temp_list = list(word)
            temp_list[0] = str.upper(temp_list[0])
            temp_list[len(temp_list)-1] = str.upper(temp_list[len(temp_list)-1])
            final_data.append(''.join(temp_list))

    return ' '.join(final_data)

if __name__ == "__main__":
    main_data = obtain_user_input(input_mess='Enter some sentence: ')
    data = process_sentence(main_str=main_data)
    print(f'Processed data is: {data}')
