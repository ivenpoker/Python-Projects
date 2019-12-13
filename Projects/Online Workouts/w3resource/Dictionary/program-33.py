#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Checks multiple keys exists in a dictionary                       #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 13, 2019                                                 #
#                                                                                          #
############################################################################################

def check_multiple_keys(main_dict: dict, keys: set) -> bool:
    return main_dict.keys() >= keys

if __name__ == "__main__":
    student = {'name': 'Alex', 'class': 'V', 'roll_id': '2'}

    print(check_multiple_keys(main_dict=student, keys={'class', 'name'}))
    print(check_multiple_keys(main_dict=student, keys={'name', 'Alex'}))
    print(check_multiple_keys(main_dict=student, keys={'roll_id', 'name'}))
