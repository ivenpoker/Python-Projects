#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Guess a number between 1 and 9 (in a game).                       #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 21, 2019                                                  #
#                                                                                          #
############################################################################################

from random import randint

def get_random_guess(low: int, high: int):
    return randint(low, high)

def begin_game():
    main_guess, play, success = get_random_guess(1, 9), True, False
    print(f'Computer has guessed number!')
    print('-' * 30)
    while play:
        try:
            user_guess = int(input('Enter guess: '))
            if user_guess == main_guess:
                play = False
                success = True
            else:
                print('-' * 30)
                print(f'Oops! wrong.')
                print('-' * 30)
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    if success:
        print('-' * 30)
        print(f'Well guessed!')


if __name__ == "__main__":
    begin_game()