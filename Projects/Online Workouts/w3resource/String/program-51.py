#######################################################################################
#                                                                                     #
#       Program purpose: Finds the first non-repeating character in a given string.   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 25, 2019                                             #
#                                                                                     #
#######################################################################################


def get_user_data(mess: str):
    is_valid = False
    user_data = ''
    while is_valid is False:
        try:
            user_data = input(mess)
            if len(user_data) == 0:
                raise ValueError('Please provide some string to work with')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data


def find_first_non_repeating_char(main_str: str):
    data = {}
    for char in main_str:
        if char in data:
            data[f'{char}'] += 1
        else:
            data[f'{char}'] = 1
    data = [k for (k, v) in zip(data.keys(), data.values()) if v == 1]
    return None if len(data) == 0 else data[0]


if __name__ == "__main__":

    print(f"Testing string 'abcdef': {find_first_non_repeating_char(main_str='abcdef')}")
    print(f"Testing string 'abcabcdef': {find_first_non_repeating_char(main_str='abcabcdef')}")
    print(f"Testing string 'aabbcc': {find_first_non_repeating_char(main_str='aabbcc')}")
