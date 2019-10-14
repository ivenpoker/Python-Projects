#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Parses string from input, removes duplicates and print the   #
#                        distinct ones back to the user.                              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 14, 2019                                             #
#                                                                                     #
#######################################################################################

def read_user_data(mess: str):
    is_valid = False
    user_str = ''
    while is_valid is False:
        try:
            user_str = input(mess)
            if len(user_str) == 0:
                raise ValueError('Please provided a string')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_str

def process_data(main_data: str):
    datums = main_data.split(',')
    result = set()
    for dat in datums:
        result.add(dat.strip())
    return sorted(result, reverse=False)

if __name__ == "__main__":

    user_data = read_user_data(mess='Enter some string: ')
    proc_data = process_data(main_data=user_data)
    print(f'Processed data: {", ".join(proc_data)}')


