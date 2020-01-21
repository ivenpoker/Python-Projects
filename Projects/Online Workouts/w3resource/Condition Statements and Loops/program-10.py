#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Prints to console certain strings based on certain properties.    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 21, 2019                                                  #
#                                                                                          #
############################################################################################

def do_computation(low: int, high: int) -> None:
    if high < low:
        raise ValueError(f"Invalid parameters. 'High' must be > 'Low'")
    temp = low
    while temp < high:
        if temp % 3 == 0 and temp % 5 == 0:
            print('FizzBuzz')
            continue
        elif temp % 3 == 0:
            print('Fizz')
            continue
        elif temp % 5 == 0:
            print('Buzz')
            continue
        else:
            print(f'{temp}')


if __name__ == "__main__":
    do_computation(low=1, high=50)