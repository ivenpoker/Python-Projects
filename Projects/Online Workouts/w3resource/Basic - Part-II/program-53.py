#!/usr/bin/env  python3

######################################################################################
#                                                                                    #
#       Program purpose: Accepts an even number (>=4, Goldbach number) from the user #
#                        and create combinations that express the given number as    #
#                        sum of two prime numbers. Print the number of combinations  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                       #
#       Creation Date  : September 23, 2019                                          #
#                                                                                    #
######################################################################################

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

def find_prime_comb(key_num: int, num_comb: int):
    prime_nums = []
    prime_comb = []
    temp_cnt = 1

    while len(prime_comb) < num_comb:
        if is_prime(temp_cnt):
            prime_nums.append(temp_cnt)
            for x in prime_nums:
                if x + temp_cnt == key_num:
                    prime_comb.append((x, temp_cnt))
        temp_cnt += 1

    return prime_comb

def is_prime(num: int):
    return num_factors(some_num=num) == 2

def num_factors(some_num: int):
    fact = 0
    temp = 1
    while temp <= some_num / 2:
        if some_num % temp == 0:
            fact += 1
        temp += 1
    return fact + 1


if __name__ == "__main__":
    even_num = 1
    while even_num % 2 != 0:
        even_num = read_data(mess="Enter an even number: ")
    comb_num = 0
    while comb_num <= 0:
        comb_num = read_data(mess="Enter number of combinations (>= 1): ")

    new_data = find_prime_comb(key_num=even_num, num_comb=comb_num)
    print(f"Combinations [found: {len(new_data)}]")

    temp = 1
    for comb in new_data:
        print(f"{temp}. {comb} -> [{comb[0]} + {comb[1]} = {even_num}]")
        temp += 1
