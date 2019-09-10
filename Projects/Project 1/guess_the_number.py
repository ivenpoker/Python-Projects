#!/usr/bin/env  python3

#################################################################################
#                                                                               #
#       Program purpose: Guess a number that the computer guessed.              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                  #
#       Creation Date  : September 10, 2019                                     #
#                                                                               #
#################################################################################

import random

if __name__ == "__main__":
    low = 1
    high = 100
    comp_guess = random.choice(seq=range(low, high))
    user_guess = 0

    print(f"Computer has guessed number in range {low} and {high}")

    cont = True

    while cont:
        try:
            user_guess = int(input("Enter your guess of the number: "))
            if user_guess == comp_guess:
                print("Well done, you've got that right!")
                cont = False
            elif user_guess < comp_guess:
                print("That was too low!")
            else:
                print("That was too high!")
        except ValueError as ve:
            print(f"[ERROR]: {ve}")
    print("Terminating....")