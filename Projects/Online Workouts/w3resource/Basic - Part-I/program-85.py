
# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: To check if a file path is file or a directory.           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 19, 2019                                              #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":
    import os

    path = input("Enter a path to directory or file: ")
    if os.path.isdir(path):
        print(f"\nIt is a directory")
    elif os.path.isfile(path):
        print(f"\nIt is a normal file")
    else:
        print(f"It is a special file (socket, FIFO, device file)")
    print()