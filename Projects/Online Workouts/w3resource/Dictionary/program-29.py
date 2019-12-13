#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Removes spaces from dictionary keys.                              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 13, 2019                                                 #
#                                                                                          #
############################################################################################

def remove_spaces_from_dict_keys(main_dict: dict) -> dict:
    dict_keys = list(main_dict.keys())
    new_keys = []
    for key in dict_keys:
        temp = [x for x in str(key).split() if not str.isspace(x)]
        new_keys.append(''.join(temp))

    return {k: v for (k, v) in zip(new_keys, main_dict.values())}

if __name__ == "__main__":

    temp_dict = {'S 001': ['Math', 'Science'], 'S     002': ['Math', 'English']}
    print(f'Original dictionary: {temp_dict}')
    new_dict = remove_spaces_from_dict_keys(main_dict=temp_dict)

    print(f'New dictionary: {new_dict}')