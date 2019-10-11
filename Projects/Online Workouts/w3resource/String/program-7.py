#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Finds the first appearance of the substring 'not' and 'poor' #
#                        from a given string, if 'not' follows the 'poor', replace    #
#                        the whole 'not'...'poor' substring with 'good'.              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 11, 2019                                             #
#                                                                                     #
#######################################################################################

def get_user_string(mess: str):
    is_valid = False
    data = ''
    while is_valid is False:
        try:
            data = input(mess)
            if len(data) == 0:
                raise ValueError('Please provide a string')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return data

def process_string(main_data: str):
    val = main_data.find('not')
    new_data = ''
    if val != -1:
        temp = main_data.find('poor')
        if temp != -1:
            new_data = main_data[:val] + 'good' + main_data[temp + len('poor'):]
    else:
        temp = main_data.find('poor')
        if temp != -1:
            new_data = main_data[:temp] + 'good' + main_data[temp + len('poor'):]

    if len(new_data) == 0:
        return main_data
    return new_data


if __name__ == "__main__":

    main_str = get_user_string(mess='Enter some string: ')
    proc_data = process_string(main_data=main_str)
    print(f'Processed data: {proc_data}')