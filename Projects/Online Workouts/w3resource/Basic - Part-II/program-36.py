#!/usr/bin/env  python3

#################################################################################
#                                                                               #
#       Program purpose: Compute amount of debts in month.                      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                  #
#       Creation Date  : September 10, 2019                                     #
#                                                                               #
#################################################################################

def round_n(n):
    if n % 1000:
        return (1 + n // 1000) * 1000

def compute_debt(n):
    if n == 0:
        return 10000
    return float(str(round_n(compute_debt(n - 1) * 1.05)))

if __name__ == "__main__":

    is_valid = False
    num_months = 0

    while is_valid is False:
        try:
            print("Input number of months: ", end="")
            num_months = int(input().strip())

            if 0 < num_months < 13:
                is_valid = True
            else:
                print("Month must be in range [1, 12]")

        except ValueError as ve:
            print("Invalid input. Try again")

    result = compute_debt(num_months)
    print(f"Amount of debt: ${str(result).strip()}")
