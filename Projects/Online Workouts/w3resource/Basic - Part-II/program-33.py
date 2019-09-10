#!/usr/bin/env  python3

#################################################################################
#                                                                               #
#       Program purpose: Compute the digit number of sum of two given numbers.  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                  #
#       Creation Date  : September 10, 2019                                     #
#                                                                               #
#################################################################################

if __name__ == "__main__":
    int_a = 0
    int_b = 0
    cont = True

    while cont:
        try:
            int_a = int(input("Enter first integer: "))
            cont = False
        except ValueError as ve:
            print("Invalid input. Try again.")
    cont = True
    while cont:
        try:
            int_b = int(input("Enter second integer: "))
            cont = False
        except ValueError as ve:
            print("Invalid input. Try again.")
    num_sum = int_a + int_b
    print(f"Digit number of sum [{int_a} + {int_b}]: {len(f'{num_sum}')}")
