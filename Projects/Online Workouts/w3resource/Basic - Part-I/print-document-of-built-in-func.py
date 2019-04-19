#!/usr/bin/env python3

###################################################################################
#                                                                                 #
#       Program purpose: Print the documents (syntax, description etc.) of Python #
#                        built-in function(s                                      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                    #
#       Creation Date  : 19/04/2019                                               #
#                                                                                 #
###################################################################################


def main():
    func_name = input("Enter name of document: ")
    print("\nData obtained:\n----------------------\n{}".format(func_name.__doc__))

if __name__ == "__main__":
    main()