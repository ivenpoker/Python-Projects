#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Removes the nth index character from a nonempty string.      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 11, 2019                                             #
#                                                                                     #
#######################################################################################

def get_user_string(mess: str):
    is_valid = False
    data = ''
    while is_valid is False:
        try:
            data = input(mess)
            if len(data) == 0:
                raise ValueError('Please enter a string')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return data

def get_index_to_del(mess: str, max_ind: int):
    is_valid = False
    ind = -1
    while is_valid is False:
        try:
            ind = int(input(mess))
            if ind < 0 or ind > max_ind:
                raise ValueError(f'Please provide index in range [{0}, {max_ind}]')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
        except RuntimeError as re:
            print(f'[ERROR]: {re}')
    return ind

def remove_data_at_ind(data: str, main_ind: int):
    return data[:main_ind] + data[main_ind+1:]

if __name__ == "__main__":
    user_data = get_user_string(mess='Enter some string: ')
    user_ind = get_index_to_del(mess='Enter index to remove: ', max_ind=len(user_data)-1)
    new_data = remove_data_at_ind(data=user_data, main_ind=user_ind)
    print(f'Processed data: {new_data}')

