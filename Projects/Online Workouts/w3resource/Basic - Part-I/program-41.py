# !/usr/bin/env  python3

################################################################################
#                                                                              #
#       Program purpose: Checks if a file exists from a path                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                 #
#       Creation Date  : August 9, 2019                                        #
#                                                                              #
################################################################################


def createFile(fileName):
    open(fileName, 'w')

if __name__ == "__main__":
    import os

    newFileName = "sample.txt"
    createFile(fileName=newFileName)

    if os.path.isfile(newFileName):
        print(f"File with name {newFileName} exists!")
    else:
        print(f"File with name {newFileName} does not exists!")