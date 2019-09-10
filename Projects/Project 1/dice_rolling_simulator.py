#!/usr/bin/env  python3

#################################################################################
#                                                                               #
#       Program purpose: Dice rolling simulator.                                #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                  #
#       Creation Date  : September 10, 2019                                     #
#                                                                               #
#################################################################################

def random_in_range(low: int, high: int):
    import random
    return random.choice(seq=range(low, high+1))


if __name__ == "__main__":
    num_times = 0
    cont = True

    while cont:
        try:
            num_times = int(input("Enter number of times to roll dice: "))
            cont = False
        except ValueError as ve:
            print(f"{ve}")
    temp = 1
    while temp != num_times+1:
        print(f"Dice rolling #{temp}: {random_in_range(low=1, high=6)}")
        temp += 1

