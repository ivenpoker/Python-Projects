#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Executes user defined code from terminal (standard input).        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 01, 2020                                                 #
#                                                                                          #
############################################################################################

def obtain_user_code(input_mess: str) -> str:
    user_code, valid = '', False
    while not valid:
        try:
            user_code = input(input_mess).strip()
            if len(user_code) == 0:
                raise ValueError("Oops, data needed")
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_code

def execute_user_code(some_code: str) -> object:
    results = exec(some_code)
    return results

if __name__ == "__main__":

    main_code = obtain_user_code(input_mess='Enter some peice of code to execute: ')
    print(f'Executing code ... ')

    print('-' * 25)
    response = execute_user_code(some_code=main_code)
    print('-' * 25)

    print(f'[DONE]')
