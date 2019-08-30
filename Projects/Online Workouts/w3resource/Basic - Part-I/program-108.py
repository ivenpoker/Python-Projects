# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Find path refers to a file or directory when you encounter a #
#                        path name.                                                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 30, 2019                                              #
#                                                                                     #
#######################################################################################

import os.path

if __name__ == "__main__":

    for file in [__file__, os.path.dirname(__file__), '/', './broken_link']:
        print(f"\nFile        : {file}")
        print(f"Absolute    : {os.path.isabs(file)}")
        print(f"Is File?    : {os.path.isfile(file)}")
        print(f"Is Dir?     : {os.path.isdir(file)}")
        print(f"Is Link?    : {os.path.islink(file)}")
        print(f"Exists?     : {os.path.exists(file)}")
        print(f"Link Exists : {os.path.lexists(file)}")
