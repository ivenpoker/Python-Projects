#!/usr/bin/env  python3

###############################################################################################
#                                                                                             #
#       Program purpose: Accepts name of given subject and marks. Input number of subjects    #
#                        in first line and subject name, marks separated by a space in next   #
#                        line. Print subject name and marks in order of its first occurrence. #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                                #
#       Creation Date  : December 27, 2019                                                    #
#                                                                                             #
###############################################################################################

from collections import OrderedDict

def read_all_data() -> OrderedDict:

    num, valid = int(-1), False
    while not valid:
        try:
            num = int(input('Enter number of subjects: '))
            if num < 0:
                raise ValueError('Invalid number of subjects must be +ve (>0)')
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')

    item_order = OrderedDict()

    for i in range(num):
        list_data = input('Enter subject name and mark: ').strip().split(' ')
        subject_name = list_data[0]
        subject_mark = int(list_data[1])

        if subject_name not in item_order.keys():
            item_order[subject_name] = subject_mark
        else:
            item_order[subject_name] = item_order[subject_name] + subject_mark

    return item_order

def display_data(main_data: OrderedDict) -> None:
    for key in main_data.keys():
        print(f'{key} {main_data[key]}')

if __name__ == "__main__":
    processed_data = read_all_data()
    display_data(main_data=processed_data)
