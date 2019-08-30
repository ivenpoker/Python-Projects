# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Check if a string is numeric.                                #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 29, 2019                                              #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":
    user_str = input("Enter sample string: ")
    try:
        data = float(user_str)
    except (ValueError, TypeError) as error:
        print(f"\nNot numeric:\n\n{error}")