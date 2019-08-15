# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Get file creation and modification date/times.               #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 15, 2019                                              #
#                                                                                     #
#######################################################################################

def get_info(file_name):
    import os.path
    import time

    return [time.ctime(os.path.getmtime(file_name)), time.ctime(os.path.getctime(file_name))]

if __name__ == "__main__":
    name = input("Enter file name: ")
    data = get_info(file_name=name)
    print(f"Last modified: {data[0]}\nCreated: {data[1]}")