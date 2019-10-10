#!/usr/bin/env  python3

######################################################################################
#                                                                                    #
#       Program purpose: Find the number of combinations that satisfy a+b+c+d=n      #
#                        where n is a given number <= 4000 and a,b,c and d are in    #
#                        the range 0 to 1000.                                        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                       #
#       Creation Date  : October 10, 2019                                            #
#                                                                                    #
######################################################################################

def do_computations():
    from collections import Counter
    print("Input a positive integer: [ctrl+d to exit]")
    pair_dict = Counter()
    for i in range(2001):
        pair_dict[i] = min(i, 2000 - i) + 1

    while True:
        try:
            n = int(input())
            ans = 0
            for i in range(n + 1):
                ans += pair_dict[i] * pair_dict[n - i]
            print(f"Number of combinations a,b,c,d: {ans}")
        except EOFError:
            break

if __name__ == "__main__":
    do_computations()
