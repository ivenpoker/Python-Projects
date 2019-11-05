#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Finds the longest common sub-string from two given strings.       #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 5, 2019                                                  #
#                                                                                          #
############################################################################################

def obtain_user_data(input_mess: str) -> str:
    is_valid, user_data = False, ''
    while is_valid is not True:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError("Invalid data. Please enter some data to work with")
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def do_the_processing(valA: str, valB: str) -> str:
    sub_strings = []
    for i in range(len(valA)):
        for j in range(len(valB)):
            if valA[i] == valB[j]:
                temp_i = i
                temp_j = j
                temp_str = ''
                while (temp_i in range(len(valA))) and (temp_j in range(len(valB))):
                    if valA[temp_i] == valB[temp_j]:
                        temp_str += valB[temp_i]
                        temp_i += 1
                        temp_j += 1
                    else:
                        break
                sub_strings.append(temp_str)

    # Sort new data in reversed order based on length of substrings
    new_data = sorted(sub_strings, reverse=True, key=len)

    return new_data[0] if len(new_data) > 0 else None


if __name__ == "__main__":
    strA = obtain_user_data(input_mess=' Enter first string: ')
    strB = obtain_user_data(input_mess='Enter second string: ')
    print(f'Processed data: {do_the_processing(valA=strA, valB=strB)}')
