#!/usr/bin/env  python3

##############################################################################################
#                                                                                            #
#       Program purpose: Prints all the numbers from 0 to 6 except 3 and 6 using 'continue'. #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                               #
#       Creation Date  : January 21, 2019                                                    #
#                                                                                            #
##############################################################################################

def print_nums():
    for x in range(6):
        if x == 3 or x == 6:
            continue
        print(f'Value of x: {x}')

if __name__ == "__main__":
    print_nums()