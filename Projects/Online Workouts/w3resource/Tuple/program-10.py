#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Checks if a tuple exists in a list of tuples.                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 19, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_tuples_list(low: int = 0, high: int = 10, size: int = 10):
    if size < 0:
        raise ValueError(f"Invalid size 'f{size}'. Must be >  0")
    return [(random.randint(low, high), random.randint(low, high)) for _ in range(size)]

def do_checking(tuple_list: list) -> None:
    stop, user_data = False, ''
    while not stop:
        try:
            user_data = input("Enter tuple (as -> a b) to check existence [type '.' to stop]: ").strip()
            if user_data == '.':
                stop = True
            else:
                temp = user_data.split(' ')
                if len(temp) != 2:
                    raise ValueError('Invalid input. Must be as -> a b')
                (a, b) = int(temp[0].strip()), int(temp[1].strip())

                print(f'Checking if ({a}, {b}) is found in tuples above ... '
                      f'{"[FOUND]" if tuple_list.count((a, b)) > 0 else "[NOT FOUND]"}')

        except ValueError as ve:
            print(f'[WARNING]: {ve}')
        except TypeError as te:
            print(f'[ERROR]: {te}')


if __name__ == "__main__":
    new_tuples = random_tuples_list(low=0, high=10, size=10)
    print(f'New random tuples: {new_tuples}')

    # let's now do the checking
    do_checking(tuple_list=new_tuples)