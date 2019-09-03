#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Find files and skip directories of a given directory.        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 2, 2019                                            #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":
    import os
    print([f for f in os.listdir(f"/home/killerbean/Downloads") if os.path.isfile(os.path.join('/home/students', f))])

