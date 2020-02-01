#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Creates and prints a list where the values are squares of numbers #
#                        from a specified size (by user).                                  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 01, 2020                                                 #
#                                                                                          #
############################################################################################

def obtain_user_data(input_mess: str) -> int:
    user_size, valid = int(-1), False
    while not valid:
        try:
            user_size = int(input(input_mess))
            if user_size <= 0:
                raise ValueError("Invalid size. Must be > 0")
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_size

def get_squares_A(size: int) -> list:
    squares = []
    for x in range(1, size+1):
        squares.append(int(pow(x, 2)))
    return squares

def get_squares_B(size: int) -> list:
    return [int(pow(x, 2)) for x in range(1, size+1)]

if __name__ == "__main__":
    main_size = obtain_user_data(input_mess='Enter max size for squares: ')
    print(f'Squares list [func A]: {get_squares_A(size=main_size)}')
    print(f'Squares list [func B]: {get_squares_B(size=main_size)}')
