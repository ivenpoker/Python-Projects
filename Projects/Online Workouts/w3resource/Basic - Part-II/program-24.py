#!/usr/bin/env  python3

###########################################################################
#                                                                         #
#       Program purpose: Finds the number of divisors of a given integer, #
#                        even or odd.                                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>            #
#       Creation Date  : September 9, 2019                                #
#                                                                         #
###########################################################################


def count_divisors(num):
    div_list = [n for n in range(1, num+1) if num % n is 0]
    return {"div": div_list, "size": len(div_list)}

if __name__ == "__main__":
    user_int = 0
    cont = True

    while cont:
        try:
            user_int = int(input("Enter a number: "))
            cont = False
        except ValueError as ve:
            print(f"{ve}")
    print(f"{count_divisors(num=user_int)}")
