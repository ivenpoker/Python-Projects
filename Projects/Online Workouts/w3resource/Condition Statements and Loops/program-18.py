#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Prints letter 'D' to the console.                                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 27, 2019                                                  #
#                                                                                          #
############################################################################################

def print_letter_D(char: str, max_size: int) -> None:
    print(f'{char}' * max_size)
    for x in range(max_size+1):
        for y in range(max_size+1):
            if y == 0:
                print(f'{char}', end='')
            elif y == max_size:
                print(f'{char}')
            else:
                print(f' ', end='')
    print(f'{char}' * max_size)

if __name__ == "__main__":
    print_letter_D('#', 20)
