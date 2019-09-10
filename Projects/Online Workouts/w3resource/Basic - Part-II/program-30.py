#!/usr/bin/env  python3

##############################################################################
#                                                                            #
#       Program purpose: Reverse the digits of a given number and add it to  #
#                        the original, if the sum is not a palindrome repeat #
#                        the procedure.                                      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>               #
#       Creation Date  : September 9, 2019                                   #
#                                                                            #
##############################################################################

def reverse_digits(num: int):
    digit_list = list(f"{num}")
    digit_list.reverse()                 # reverse list contents
    return int(''.join(digit_list))

def is_palindrome(string: str):
    rev = string[::-1]
    return string == rev

def reverse_add(num: int):
    temp = reverse_digits(num=num)
    main_sum = num + temp
    print(f"{num} + {temp} = {main_sum}")
    return main_sum

if __name__ == "__main__":
    user_int = 0
    cont = True

    while cont:
        try:
            user_int = int(input("Enter number to check: "))
            cont = False
        except ValueError as ve:
            print(f"{ve}")

    some_sum = reverse_add(num=user_int)

    while is_palindrome(string=f"{some_sum}") is False:
        some_sum = reverse_add(num=some_sum)

