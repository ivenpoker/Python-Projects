#!/usr/bin/env  python3

####################################################################################
#                                                                                  #
#       Program purpose: Computes the first n prime numbers.                       #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                     #
#       Creation Date  : September 22, 2019                                        #
#                                                                                  #
####################################################################################

def read_data(mess: str):
    valid = False
    data = 0
    while not valid:
        try:
            data = int(input(mess))
            valid = True
        except ValueError as ve:
            print(f"[ERROR]: {ve}")
    return data

def find_sum_of_primes(prime_cnt: int):
    cnt, tmp_cnt = 1, 1
    temp_sum = 0
    while tmp_cnt <= prime_cnt:
        if is_prime(cnt):
            temp_sum += cnt
            tmp_cnt += 1
        cnt += 1
    return temp_sum

def is_prime(num: int):
    return num_factors(num) == 2

def num_factors(num: int):
    factors = 0
    temp = 1
    while temp <= num / 2:
        if num % temp == 0:
            factors += 1
        temp += 1
    return factors + 1


if __name__ == "__main__":
    main_data = read_data(mess="Enter number of primes to compute sum: ")
    print(f"First {main_data} prime number(s) sum: {find_sum_of_primes(main_data)}")
