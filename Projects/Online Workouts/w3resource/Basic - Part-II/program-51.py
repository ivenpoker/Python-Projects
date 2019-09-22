#!/usr/bin/env  python3

####################################################################################
#                                                                                  #
#       Program purpose: Finds the difference between the largest and the smallest #
#                        integer which are created by numbers from 0 to 9. The     #
#                        number that can be rearranged shall start with 0 as in    #
#                        00135668.                                                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                     #
#       Creation Date  : September 22, 2019                                        #
#                                                                                  #
####################################################################################

def read_data(mess: str):
    valid = False
    data = 0
    while not valid:
        try:
            temp_data = list(input(mess).strip())
            if len(temp_data) != 8:
                raise ValueError("Number must be 8-digit long")
            else:
                for x in range(len(temp_data)):
                    if not f"{temp_data[x]}".isdigit():
                        raise ValueError(f"'{temp_data[x]}' is not an integer")
                data = temp_data
                valid = True
        except ValueError as ve:
            print(f"[ERROR]: {ve}")
    return data


if __name__ == "__main__":
    main_data = read_data("Enter an integer created by 8 numbers from 0 to 9: ")
    largest = ''.join(sorted(main_data, reverse=True))
    smallest = ''.join(sorted(main_data))
    print(f"Difference between the largest {largest} and smallest {smallest}:"
          f" {int(''.join(largest)) - int(''.join(smallest))}")
