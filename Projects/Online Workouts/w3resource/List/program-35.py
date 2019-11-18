#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Creates a list by concatenating a given list which range goes     #
#                        from 1 to n.                                                      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

def obtain_user_data(input_mess: str) -> list:
    user_data, is_valid = [], False
    while is_valid is False:
        try:
            temp_data = input(input_mess).strip()
            if len(temp_data) == 0:
                raise ValueError('Oops, data is needed')
            unit_temp = temp_data.split()
            for x in unit_temp:
                if len(x) < 2:
                    user_data.append(x)
                else:
                    user_data = []  # erase previous data
                    raise ValueError(f"'{x}' is not valid. Only SINGLE characters needed")
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def obtain_max_num(input_mess: str) -> int:
    user_data, is_valid = int(-1), False
    while is_valid is False:
        try:
            user_data = int(input(input_mess).strip())
            if user_data < 0:
                raise ValueError('Oops, only +ve number is required.')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def do_processing(main_list: list, num: int) -> list:
    new_list_data = []
    for x in main_list:
        for i in range(1, num):
            new_list_data.append(f'{x}{i}')
    return sorted(new_list_data, key=lambda val: val[-1:])


if __name__ == "__main__":

    new_data = obtain_user_data(input_mess='Enter data (single chars separated with space): ')
    new_num = obtain_max_num(input_mess="Enter value of 'n': ")

    print(f'Processed data: {do_processing(main_list=new_data, num=new_num)}')
