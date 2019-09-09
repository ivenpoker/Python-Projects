#!/usr/bin/env  python3

###########################################################################
#                                                                         #
#       Program purpose: Accept a positive number and subtract from this  #
#                        number the sum of its digits and so on.          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>            #
#       Creation Date  : September 6, 2019                                #
#                                                                         #
###########################################################################

def repeat_times(num):
    s = 0
    num_str = str(num)
    while num > 0:
        num -= sum([int(i) for i in list(num_str)])
        num_str = list(str(num))
        s += 1
    return s

if __name__ == "__main__":
    user_int = 0
    cont = True

    while cont:
        try:
            user_int = int(input("Enter a positive number: "))
            if user_int <= 0:
                raise ValueError("Integer must be positive [i.e > 0]")
            cont = False
        except ValueError as ve:
            print(f"{ve}")

    print(f"Final value: {repeat_times(user_int)}")

