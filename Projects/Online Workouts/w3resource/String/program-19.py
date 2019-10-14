#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Gets the last part of a string before a specified character. #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 14, 2019                                             #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":
    str1 = "https://www.w3resource.com/python-exercises/string"
    print(str1.rsplit('/', 1)[0])
    print(str1.rsplit('-', 1)[0])
