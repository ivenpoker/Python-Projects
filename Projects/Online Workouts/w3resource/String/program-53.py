#######################################################################################
#                                                                                     #
#       Program purpose: Finds the first repeated character in a given string.        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 25, 2019                                             #
#                                                                                     #
#######################################################################################

def obtain_data_from_user(input_mess: str):
    is_valid = False
    user_data = ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Please provide some data to work with')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def find_first_repeat_char(main_str: str):
    data = {}
    for char in main_str:
        if char in data:
            data[f'{char}'] += 1
        else:
            data[f'{char}'] = 1
    temp = [k for (k, v) in zip(data.keys(), data.values()) if v >= 2]
    return None if len(temp) == 0 else temp[0]

if __name__ == "__main__":
    main_data = obtain_data_from_user(input_mess='Enter some string: ')
    print(f'First repeat character: {find_first_repeat_char(main_str=main_data)}')
