# !/usr/bin/env  python3

###################################################################################
#                                                                                 #
#       Program purpose: Parse a string to Float or Integer.                      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                    #
#       Creation Date  : August 9, 2019                                           #
#                                                                                 #
###################################################################################

if __name__ == "__main__":

    sample = "781.65892"
    print(f"As float: {float(sample)}")
    print(f"As In: {int(float(sample))}")