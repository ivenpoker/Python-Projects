#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Check if an variable is of integer type or string type.      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 3, 2019                                            #
#                                                                                     #
#######################################################################################

def find_type(someVar=None):
    if someVar is None:
        raise TypeError("Invalid argument")
    typeInfo = str(type(someVar))

    if typeInfo.find("str") >= 0:
        return "str"
    elif typeInfo.find("int") >= 0:
        return "int"

if __name__ == '__main__':
    varA = int(1)
    print(f"Variable type of varA: {find_type(varA)}")
    varB = str("james")
    print(f"Variable type of varB: {find_type(varB)}")
