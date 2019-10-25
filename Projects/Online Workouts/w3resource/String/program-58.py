#########################################################################################
#                                                                                       #
#       Program purpose: Moves spaces found in a string (or sentence) to the front.     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                          #
#       Creation Date  : October 25, 2019                                               #
#                                                                                       #
#########################################################################################

def obtain_user_data(input_mess: str):
    is_valid, user_data = False, ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Please enter string data')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def moves_spaces_to_front(main_str: str):
    no_spaces_str = [ch for ch in main_str if ch != ' ']
    num_spaces = len(main_str) - len(no_spaces_str)
    new_spaces = ' ' * num_spaces
    main_str = main_str.replace(' ', '')
    return f'{new_spaces}{main_str}'


if __name__ == "__main__":
    main_data = obtain_user_data(input_mess='Enter some string data: ')
    print(f'After moving spaces: {moves_spaces_to_front(main_str=main_data)}')