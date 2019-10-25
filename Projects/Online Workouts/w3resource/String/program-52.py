#############################################################################################
#                                                                                           #
#       Program purpose: Prints all permutation with given repetition number of characters  #
#                        of a given string.                                                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                              #
#       Creation Date  : October 25, 2019                                                   #
#                                                                                           #
#############################################################################################

from itertools import product

def obtain_user_data(mess: str):
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

def all_repeat(main_str: str, perm_num: int):
    chars = list(main_str)
    results = []
    for c in product(chars, repeat=perm_num):
        results.append(c)
    return results

if __name__ == "__main__":
    main_data = obtain_user_data(mess='Enter some data: ')
    num_perm, valid = 0, False
    while not valid:
        try:
            num_perm = int(obtain_user_data(mess='Enter number of permutations: '))
            if num_perm <= 0:
                raise ValueError('Please, enter positive number')
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')

    # main test
    print(f"Combinations with repeat #{num_perm}: {all_repeat(main_str=main_data, perm_num=num_perm)}")