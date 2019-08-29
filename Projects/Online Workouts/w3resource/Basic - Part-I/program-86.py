# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Print corresponding ASCII codes for characters in string.    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 29, 2019                                              #
#                                                                                     #
#######################################################################################

def print_ascii(string=""):
    if len(string) is not 0:
        for x in range(len(string)):
            print(f"Character '{string[x]}' -- ASCII code is {ord(string[x])}")

if __name__ == "__main__":

    user_str = input("Enter a sentence (or string): ")
    print_ascii(string=user_str)