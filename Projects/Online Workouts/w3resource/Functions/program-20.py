#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Detect the number of local variables declared in a function.      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 01, 2020                                                 #
#                                                                                          #
############################################################################################

def demo_func(val: int):
    x = 1
    y = 2
    str1 = 'deathshot'
    print('One shot ... one kill')

if __name__ == "__main__":
    print(f'Number of local variables: {demo_func.__code__.co_nlocals}')
