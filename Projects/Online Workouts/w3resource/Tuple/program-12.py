#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Removes an item from a tuple.                                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 19, 2019                                                 #
#                                                                                          #
############################################################################################

from random import randint

def random_tuple(low: int, high: int, size: int) -> tuple:
    if size < 0:
        raise ValueError(f"Invalid size ({size}) for list.")
    return tuple([randint(low, high) for _ in range(size)])

def do_removals(main_tuple: tuple) -> None:
    stop, user_val = False, int(-1)
    while not stop:
        try:
            user_val = input("Enter value in tuple to remove [type '.' to stop]: ").strip()
            if user_val == '.':
                stop = True
            else:
                user_val = int(user_val)
                if user_val in main_tuple:
                    temp = list(main_tuple)  # because tuples are immutable
                    temp.remove(user_val)
                    main_tuple = tuple(temp)
                    print(f'New tuple data: {main_tuple}')
                else:
                    print(f"Value '{user_val}' NOT FOUND in list.")
        except TypeError as te:
            print(f'[TYPE-ERROR]: {te}')
        except ValueError as ve:
            print(f'[VALUE-ERROR]: {ve}')

if __name__ == "__main__":
    new_tuple = random_tuple(low=0, high=10, size=15)
    print(f'New list data: {new_tuple}')

    # Do the removals
    do_removals(main_tuple=new_tuple)
