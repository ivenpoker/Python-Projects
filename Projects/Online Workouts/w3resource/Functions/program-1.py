#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Finds the max of three numbers.                                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 01, 2020                                                 #
#                                                                                          #
############################################################################################

def obtain_user_input(input_mess: str) -> int:
    user_data, valid = int(-1), False
    while not valid:
        try:
            user_data = int(input(input_mess))
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def find_max_1(valA: int, valB: int, valC: int) -> int:
    temp_max = valA
    temp_max = valB if temp_max < valB else temp_max
    temp_max = valC if temp_max < valC else temp_max
    return temp_max

def find_max_2(valA: int, valB: int, valC: int) -> int:
    def inner_max(fst: int, snd: int) -> int:
        return snd if fst < snd else fst
    return inner_max(valA, inner_max(valB, valC))

if __name__ == "__main__":

    fstNum = obtain_user_input(input_mess='Enter number A: ')
    sndNum = obtain_user_input(input_mess='Enter number B: ')
    thrdNum = obtain_user_input(input_mess='Enter number C: ')

    print(f'-' * 25)

    print(f' Using first func, max: {find_max_1(valA=fstNum, valB=sndNum, valC=thrdNum)}')
    print(f'Using second func, max: {find_max_2(valA=fstNum, valB=sndNum, valC=thrdNum)}')

