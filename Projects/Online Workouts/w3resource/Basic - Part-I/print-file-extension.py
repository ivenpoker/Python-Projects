#!/usr/bin/env  python3

#############################################################################
#                                                                           #
#       Program purpose: When give the name of a file with it's extension,  #
#                        program prints the file extension                  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>              #
#       Creation Date  : 19/04/2019                                         #
#                                                                           #
#############################################################################

def main():
    file = input("Enter sample filename: ")
    file_parts = file.split('.')
    print("File extension: {}".format(file_parts[-1]))

if __name__ == '__main__':
    main()