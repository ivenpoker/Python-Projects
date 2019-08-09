# !/usr/bin/env  python3

###################################################################################
#                                                                                 #
#       Program purpose: List all files in a directory.                           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                    #
#       Creation Date  : August 9, 2019                                           #
#                                                                                 #
###################################################################################

if __name__ == "__main__":
    from os import listdir
    from os.path import isfile, join

    files_list = [f for f in listdir("./") if isfile(join("./", f))]
    print(files_list)
