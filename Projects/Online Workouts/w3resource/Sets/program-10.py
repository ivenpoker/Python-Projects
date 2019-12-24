#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Perform issubset and issuperset on set data.                      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 24, 2019                                                 #
#                                                                                          #
############################################################################################

from random import randint

def random_set_data(low: int, high: int, size: int) -> set:
    if size < 0:
        raise ValueError(f"Invalid size ({size}). Must be > 0")
    return set([randint(low, high) for _ in range(size)])

def check_locally(setA: set, setB: set) -> bool:
    fst_pass = True
    for x in setA:
        if x not in setB:
            fst_pass = False
            break
    if fst_pass:
        snd_pass = True
        for x in setB:
            if x not in setA:
                snd_pass = False
                break
    return fst_pass and snd_pass

if __name__ == "__main__":
    set_A = random_set_data(low=0, high=10, size=15)
    set_B = random_set_data(low=0, high=10, size=15)

    issubset = set_A <= set_B
    print(issubset)

    issuperset = set_A >= set_B
    print(issuperset)

    print(f'-' * 30)
    print(f'Checking locally: {check_locally(setA=set_A, setB=set_B)}')