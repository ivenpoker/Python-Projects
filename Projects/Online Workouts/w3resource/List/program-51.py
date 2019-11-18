#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Splits a list every Nth element.                                  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

def obtain_nth_val(input_mess: str) -> int:
    is_valid, user_data = False, int(-1)
    while is_valid is False:
        try:
            user_data = int(input(input_mess))
            if user_data < 0:
                raise ValueError(f'Oops, input must be >= 0!')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data


def split_list(list_data: list, nth_val: int) -> list:
    if nth_val >= len(list_data):
        raise ValueError('Invalid size for the list')
    new_list = []
    for i in range(len(list_data)):
        if i + nth_val < len(list_data):
            ind, temp = i, []
            while ind + nth_val < len(list_data):
                temp.append(list_data[ind])
                ind += nth_val
            new_list.append(temp)
    return new_list

if __name__ == "__main__":
    main_list = list("abcdefghijklmnopqrstuvwxyz")
    print(f'Main list: \n{main_list}')

    user_nth_val = obtain_nth_val(input_mess='Enter the nth-value: ')
    split_data = split_list(list_data=main_list, nth_val=user_nth_val)

    print(f'After splitting the data:\n{split_data}')
