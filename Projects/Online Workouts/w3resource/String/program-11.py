#!/usr/bin/env  python3

########################################################################################
#                                                                                      #
#       Program purpose: Removes the characters which have odd index values of a given #
#                        string.                                                       #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                         #
#       Creation Date  : October 11, 2019                                              #
#                                                                                      #
########################################################################################

def obtain_user_data(mess: str):
    is_valid = False
    data = ''
    while is_valid is False:
        try:
            data = input(mess)
            if len(data) == 0:
                raise ValueError('Please provide some data')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return data

def remove_odd_index_data(main_data: str):
    temp_data = ''
    for x in range(0, len(main_data), 2):
        temp_data += main_data[x]
    return temp_data

if __name__ == "__main__":
    user_data = obtain_user_data(mess='Enter some string: ')
    new_data = remove_odd_index_data(main_data=user_data)
    print(f'After removing all odd index data: {new_data}')
