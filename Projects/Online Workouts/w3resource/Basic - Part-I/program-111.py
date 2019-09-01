# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Make file lists from current directory using a wildcard.     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 1, 2019                                            #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":
    import glob
    file_list = glob.glob('*.*')
    print(f"{file_list}")
