# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Calculates body mass index.                                  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 15, 2019                                              #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":
    height = float(input("Enter your height in metres: "))
    weight = float(input("Enter your weight in metres: "))

    print(f"Your body mass index is: {round(weight / (height * height))}")