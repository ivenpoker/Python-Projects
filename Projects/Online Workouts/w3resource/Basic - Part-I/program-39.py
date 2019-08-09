# !/usr/bin/env  python3

################################################################################
#                                                                              #
#       Program purpose: Compute the future value of a specified principal     #
#                        amount, rate of interest, and a number of years.      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                 #
#       Creation Date  : August 9, 2019                                        #
#                                                                              #
################################################################################


def findFutureValue(amount, interest, years):
    return amount * ((1 + (0.01 * interest)) ** years)


if __name__ == "__main__":

    amount = float(input("Enter amount: "))
    interest = float(input("Enter interest: "))
    years = int(input("Enter years: "))

    print(f"Future value: {round(findFutureValue(amount=amount, interest=interest, years=years))}")




