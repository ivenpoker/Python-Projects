#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Prints a nested list (each list on a new line) using the print()  #
#                        function.                                                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

if __name__ == "__main__":
    colors = [['Red'], ['Green'], ['Black']]
    print('\n'.join([str(val) for val in colors]))