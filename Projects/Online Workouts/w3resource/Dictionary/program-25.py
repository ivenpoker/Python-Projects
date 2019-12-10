#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Prints a dictionary in table format.                              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 10, 2019                                                 #
#                                                                                          #
############################################################################################

main_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 70], 'C3': [9, 10, 11], 'C4': [], 'James': [1, 4]}

def display_dict(some_dict: dict) -> None:
    keys = list(some_dict.keys())
    for val in keys:
        print(f'{val}\t', end='')
    print()
    values = list(some_dict.values())
    temp = 0
    for x in range(len(values)):
        for tmp_list in values:
            if x < len(tmp_list):
                print(f'{tmp_list[x]}\t', end='')
            else:
                print(f'\t', end='')
        print()
        temp += 1

if __name__ == "__main__":
    display_dict(some_dict=main_dict)
