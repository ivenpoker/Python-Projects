#!/usr/bin/env  python3

#############################################################################
#                                                                           #
#       Program purpose: Find common divisor between two numbers in a given #
#                        pair.                                              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>              #
#       Creation Date  : September 9, 2019                                  #
#                                                                           #
#############################################################################

def find_divisor(num: int):
    div_data = [x for x in range(1, num+1) if num % x is 0]
    return div_data

def find_intersections(list_a: list, list_b: list):
    main_inter = []
    for x in range(len(list_a)):
        if list_a[x] in list_b:
            main_inter.append(list_a[x])
    return main_inter


if __name__ == "__main__":
    int_a = 0
    int_b = 0
    cont = True

    # Get the first integer.
    while cont:
        try:
            int_a = int(input("Enter first number: "))
            cont = False
        except ValueError as ve:
            print(f"{ve}")

    cont = True

    # Get the second integer
    while cont:
        try:
            int_b = int(input("Enter second number: "))
            cont = False
        except ValueError as ve:
            print(f"{ve}")

    div_a = find_divisor(int_a)
    div_b = find_divisor(int_b)

    print(f"Divisors of {int_a}: {div_a}")
    print(f"Divisors of {int_b}: {div_b}")
    print(f"Common divisors of {int_a} and {int_b}: "
          f"{find_intersections(list_a=div_a, list_b=div_b)}")

