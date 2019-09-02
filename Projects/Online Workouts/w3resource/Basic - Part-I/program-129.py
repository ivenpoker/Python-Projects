# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Add leading zeros to a string.                               #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 2, 2019                                            #
#                                                                                     #
#######################################################################################

if __name__ == '__main__':
    str1 = '122.22'
    print(f"Original string is: {str1}")
    str1 = str1.ljust(10, '0')

    print(f"String now is: {str1}")

    str1 = str1.ljust(15, '0')
    print(f"String now is: {str1}")