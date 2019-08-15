# !/usr/bin/env  python3

###################################################################################
#                                                                                 #
#       Program purpose: Convert height (in feet and inches) to centimeters.      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                    #
#       Creation Date  : August 14, 2019                                          #
#                                                                                 #
###################################################################################


if __name__ == "__main__":
    print("Input your height:")
    h_ft = int(input("Feet: "))
    h_inch = int(input("Inches: "))

    h_inch += h_ft * 12
    h_cm = round(h_inch * 2.54, 1)

    print(f"You height is: {h_cm} cm")
