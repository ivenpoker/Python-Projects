#!/usr/bin/env  python3

####################################################################################
#                                                                                  #
#       Program purpose: Reads n digits (given) chosen from 0 to 9 and prints the  #
#                        number of combinations where the sum of the digits equal  #
#                        to another given number (s). Not using the same digits in #
#                        a combination.                                            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                     #
#       Creation Date  : September 19, 2019                                        #
#                                                                                  #
####################################################################################

import itertools

def read_val(mess: str):
    valid = False
    while not valid:
        try:
            val_a, val_b = map(int, input(mess).split())
            valid = True
            return val_a, val_b
        except ValueError as ve:
            print(f"[ERROR]: {ve}")


if __name__ == "__main__":
    while True:
        int_vals = read_val(mess="Enter two integer values [input 0 0 to exit]: ")
        if int_vals[0] == int_vals[1]:
            break
        vals = list(itertools.combinations(range(10), int_vals[0]))
        ctr = 0
        for temp in vals:
            if sum(temp) == int_vals[1]:
                print(temp)
                ctr += 1
    print(ctr)
