#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Extract single key-value pair of dictionary in variables.    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 3, 2019                                            #
#                                                                                     #
#######################################################################################

if __name__ == '__main__':
    d = {"name": "James Bond", "type": "actor"}
    (c1, c2) = d.items()
    print(f"{c1}\n{c2}")