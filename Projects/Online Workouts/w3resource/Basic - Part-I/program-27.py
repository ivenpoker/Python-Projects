# !/usr/bin/env  python3

#############################################################################
#                                                                           #
#       Program purpose: Concatenates content of list as string and return  #
#                        the results.                                       #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>              #
#       Creation Date  : July 17, 2019                                      #
#                                                                           #
#############################################################################

# URL: https://www.w3resource.com/python-exercises/python-basic-exercises.php


def concat_list(some_list):
    val = ''
    for x in some_list:
        val += str(x)
    return val


if __name__ == "__main__":
    aList = [123, 'val', 'demo', 'test', 123.23]
    print(f"Main list: {aList}\nConcatenated list as string: {concat_list(aList)}")
