#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Finds numbers between 100 and 400 (both included) where each      #
#                        digit of a number is an even number. The numbers obtained should  #
#                        be printed in a comma-separated sequence.                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 21, 2019                                                  #
#                                                                                          #
############################################################################################

def all_even(some_list: list) -> bool:
    for num in some_list:
        if int(num) % 2 != 0:
            return False
    return True

def find_evens_in_range(low: int, high: int) -> str:
    evens = []
    for num in range(low, high):
        digits = list(str(num))
        if all_even(digits):
            evens.append(str(num))
    return ','.join(evens)

if __name__ == "__main__":
    digit_evens = find_evens_in_range(low=100, high=400)
    print(f'All evens: {digit_evens}')
