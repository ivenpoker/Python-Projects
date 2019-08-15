# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Program to get an absolute file path.                        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 15, 2019                                              #
#                                                                                     #
#######################################################################################

def absolute_file_path(path_file_name):
    import os
    return os.path.abspath(path_file_name)

if __name__ == "__main__":
    file_name = input("Enter file name: ")
    print(f"Absolute file path: {absolute_file_path(path_file_name=file_name)}")
