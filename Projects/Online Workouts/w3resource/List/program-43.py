#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Split a list into different variables.                            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

if __name__ == "__main__":
    color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
             ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
    var1, var2, var3 = color
    print(f'Var #1: {var1}')
    print(f'Var #2: {var2}')
    print(f'Var #3: {var3}')