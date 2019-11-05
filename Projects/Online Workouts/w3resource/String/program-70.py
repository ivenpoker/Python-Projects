#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Create a string from two given strings concatenating uncommon     #
#                        characters of the said strings.                                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 5, 2019                                                  #
#                                                                                          #
############################################################################################

def obtain_user_main_data(input_mess: str) -> str:
    is_valid, user_data = False, ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Oops, data needed')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def do_the_processing(valA: str, valB: str) -> str:
    uncommon = []
    list_valA = list(valA)
    list_valB = list(valB)

    if len(list_valA) >= len(list_valB):
        for i in range(len(list_valA)):
            if list_valA[i] not in list_valB:
                uncommon.append(list_valA[i])
    elif len(list_valA) < len(list_valB):
        for i in range(len(list_valB)):
            if list_valB[i] not in list_valA:
                uncommon.append(list_valB[i])

    return ''.join(uncommon)

if __name__ == "__main__":
    strA = obtain_user_main_data(input_mess=' Enter first string: ')
    strB = obtain_user_main_data(input_mess='Enter second string: ')
    print(f'Uncommon concatenation: {do_the_processing(valA=strA, valB=strB)}')
