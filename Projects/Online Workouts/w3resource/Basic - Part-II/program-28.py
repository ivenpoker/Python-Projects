#!/usr/bin/env  python3

###########################################################################
#                                                                         #
#       Program purpose: Prints the length of the series and the series   #
#                        from the given 3rd term, 3rd last term an the    #
#                        sum of a series.                                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>            #
#       Creation Date  : September 9, 2019                                #
#                                                                         #
###########################################################################

if __name__ == "__main__":
    series_term = 0
    third_last_term = 0
    series_sum = 0
    cont = True

    while cont:
        try:
            series_term = int(input("Input third term of the series: "))
            cont = False
        except ValueError as ve:
            print(f"{ve}")

    cont = True

    while cont:
        try:
            third_last_term = int(input("Enter 3rd last term: "))
            cont = False
        except ValueError as ve:
            print(f"{ve}")

    cont = True

    while cont:
        try:
            series_sum = int(input("Sum of the series: "))
            cont = False
        except ValueError as ve:
            print(f"{ve}")

    temp = int(2 * series_sum / (series_term + third_last_term))
    print(f"Length of the series: {temp}")

    d = (third_last_term - series_term) / (temp - 5)
    a = series_term - 2 * d
    j = 0

    print("Series: ", end="")
    for j in range(temp-1):
        print(int(a), end=" ")
        a += d
    print(int(a), end=" ")

