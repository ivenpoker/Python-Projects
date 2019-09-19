#################################################################################
#                                                                               #
#       Program purpose: Finds and prints the number of prime numbers that are  #
#                        less than or equal a certain number (integer).         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                  #
#       Creation Date  : September 19, 2019                                     #
#                                                                               #
#################################################################################

def find_number_of_primes(some_max: int):
    prime_cnt = 0
    temp_val = 1
    while temp_val <= some_max:
        if is_prime(temp_val):
            prime_cnt += 1
        temp_val += 1
    return prime_cnt

def is_prime(some_num: int):
    return num_factors(some_num=some_num) is 2

def num_factors(some_num: int):
    factors = 0
    temp = 1
    while temp <= some_num / 2:
        if some_num % temp is 0:
            factors += 1
        temp += 1
    return factors + 1

if __name__ == "__main__":
    is_valid = False
    max_num = 0
    while not is_valid:
        try:
            max_num = int(input("Enter maximum number: "))
            is_valid = True
        except ValueError as ve:
            print(f"ERROR: {ve}")
    prime_max = find_number_of_primes(some_max=max_num)
    print(f"Number of primes less than or equal to {max_num}: {prime_max}")
