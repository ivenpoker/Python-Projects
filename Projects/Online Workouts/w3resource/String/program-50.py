#######################################################################################
#                                                                                     #
#       Program purpose: Splits a string on the last occurrence of the delimiter.     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 24, 2019                                             #
#                                                                                     #
#######################################################################################

def get_user_data(mess: str):
    is_valid = False
    user_data = ''
    while is_valid is False:
        try:
            user_data = input(mess)
            if len(user_data) == 0:
                raise ValueError('Please provide some data to work with')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')

    return user_data

if __name__ == "__main__":
    main_data = get_user_data(mess='Enter some string data: ')
    delimiter = get_user_data(mess='Enter delimiter: ')

    print(f'Result 1: {main_data.rsplit(delimiter, 1)}')
    print(f'Result 2: {main_data.rsplit(delimiter, 2)}')
    print(f'Result 3: {main_data.rsplit(delimiter, 5)}')
