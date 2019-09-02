# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Determines if a variable is defined or not.                  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 2, 2019                                            #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":
    try:
        x = 1
    except NameError:
        print("Variable is not defined....")
    else:
        print("Variable is defined")

    try:
        y
    except NameError:
        print("Variable is not defined")
    else:
        print("Variable is defined")