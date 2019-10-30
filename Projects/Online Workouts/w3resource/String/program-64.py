#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Finds maximum length of consecutive 0's in a given binary string. #                       #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : October 30, 2019                                                  #
#                                                                                          #
############################################################################################

def count_max_consecutive_zeros(main_str: str) -> int:
    zero_max = int(0)
    for i in range(len(main_str)):
        if main_str[i] == '0':
            temp, j = int(1), i+1
            while j < len(main_str) and main_str[j] == '0':
                temp += 1
                j += 1
            if temp > zero_max:
                zero_max = temp
    return zero_max

if __name__ == "__main__":

    strA = str(bin(23))[2:]
    strB = str(bin(89))[2:]
    strC = str(bin(782))[2:]
    strD = str(bin(892))[2:]

    print(f'String A: {strA}, Max Zeros: {count_max_consecutive_zeros(main_str=strA)}')
    print(f'String B: {strB}, Max Zeros: {count_max_consecutive_zeros(main_str=strB)}')
    print(f'String C: {strC}, Max Zeros: {count_max_consecutive_zeros(main_str=strC)}')
    print(f'String D: {strD}, Max Zeros: {count_max_consecutive_zeros(main_str=strD)}')
