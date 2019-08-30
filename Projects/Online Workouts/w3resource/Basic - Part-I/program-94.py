# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Convert byte string to a list of integers.                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 30, 2019                                              #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":
    string = b"Sample byte string"
    print(f"String is: {string}")
    print(f"List is: {list(string)}")
