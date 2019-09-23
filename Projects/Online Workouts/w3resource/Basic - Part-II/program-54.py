#!/usr/bin/env  python3

####################################################################################
#                                                                                  #
#       Program purpose: Finds the maximum number of regions obtained by drawing   #
#                        n given straight lines.                                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                     #
#       Creation Date  : September 23, 2019                                        #
#                                                                                  #
####################################################################################

if __name__ == "__main__":
    while True:
        print("Enter number of straight lines (0 to exit): ", end="")
        try:
            num = int(input())
            if num <= 0:
                break
            print(f"Number of regions: {(num * num + num + 2) // 2}")
        except ValueError as ve:
            print(f"[ERROR]: {ve}")

