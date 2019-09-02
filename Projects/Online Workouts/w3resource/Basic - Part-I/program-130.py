# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Use double quotes ("") to display a string.                  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 2, 2019                                            #
#                                                                                     #
#######################################################################################

import json

if __name__ == '__main__':
    print(json.dumps({'Alex': 1, "Suresh": 2, 'Agnessa': 3}))