#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Accepts a sequence of comma separated 4 digits binary numbers as  #
#                        its input and print the numbers that are divisible by 5 in a      #
#                        comma separated sequence.                                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 21, 2019                                                  #
#                                                                                          #
############################################################################################

def obtain_user_binary_data(input_mess) -> list:
    user_data, valid = [], False
    while not valid:
        try:
            temp_data = input(input_mess)
            if len(temp_data) == 0:
                raise ValueError(f"Oops, data needed!")
            user_data = temp_data.split(',')
            user_data = [x.strip() for x in user_data]      # remove white space for individual binary 'strings'
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def find_divisibles(main_data: list, num: int) -> list:
    results = []
    for x in main_data:
        if int(x, 2) % num == 0:
            results.append(x)
    return results

if __name__ == "__main__":

    core_data = obtain_user_binary_data(input_mess='Enter binary data: ')
    print(f'Obtinaed data: {core_data}')

    divisor = 5
    new_data = find_divisibles(main_data=core_data, num=5)
    print(f'All values divisble by {divisor}: {new_data}')

