#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Test if a variable is a list or tuple or set.                #
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
    elif typeInfo.find("tuple") >= 0:
        return "tuple"
    elif typeInfo.find("list") >= 0:
        return "list"
    elif typeInfo.find("set") >= 0:
        return "set"
    else:
        return "[unknown]"

if __name__ == '__main__':
    varA = {1, 2, 3, 4, 5}  # set
    varB = [1, 2, 3, 4, 5]  # list
    varC = (1, 2, 3, 4, 5)  # tuple


    print(f"Type for varA: {find_type(varA)}")
    print(f"Type for varB: {find_type(varB)}")
    print(f"Type for varC: {find_type(varC)}")

    print("-------------------------")

    # OR we could just do this

    if isinstance(varA, set):
        print(f"Type for varA is set")
    if isinstance(varB, list):
        print(f"Type for varB is list")
    if isinstance(varC, tuple):
        print(f"Type for varC is tuple")

    print("--------------------------")

    # OR we could just do this again as such...

    if type(varA) is set:
        print("varA is a set")

    if type(varB) is list:
        print("varB is a list")

    if type(varC) is tuple:
        print("varC is a tuple")
