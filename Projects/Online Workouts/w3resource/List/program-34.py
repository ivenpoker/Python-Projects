#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Finds a number of prime numbers up to an upper limit              #
#                        using Eratosthenes algorithm.                                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

def obtain_user_input(input_mess: str) -> int:
    user_data, is_valid = int(-1), False
    while is_valid is False:
        try:
            user_data = int(input(input_mess))
            if user_data < 0:
                raise ValueError('Oops, data must be > 0')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def prime_eratosthenes(num) -> list:
    prime_list = []
    found_primes = []
    for i in range(2, num + 1):
        if i not in prime_list:
            found_primes.append(i)
            for j in range(i*i, num + 1, i):
                prime_list.append(j)
    return found_primes

if __name__ == "__main__":

    user_input = obtain_user_input(input_mess='Enter number of primes to compute (using Eratosthenes algorithm): ')
    primes = prime_eratosthenes(num=user_input)
    print(f'Found primes: {primes}')