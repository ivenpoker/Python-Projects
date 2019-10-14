#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Removes a newline in strings.                                #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 14, 2019                                             #
#                                                                                     #
#######################################################################################

def remove_newline(main_str: str):
    return main_str.lstrip().rstrip()

if __name__ == "__main__":
    test1 = '\nJames is the king\n'
    test2 = '\nSweet potatoes'
    test3 = 'James Bond\n'

    print(f'After striping on test1: {remove_newline(main_str=test1)}')
    print(f'After striping on test2: {remove_newline(main_str=test2)}')
    print(f'After striping on test3: {remove_newline(main_str=test3)}')