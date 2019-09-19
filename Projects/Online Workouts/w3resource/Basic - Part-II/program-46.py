#!/usr/bin/env  python3

##################################################################################
#                                                                                #
#       Program purpose: Prints date between (2016/1/1 to 2016/12/31)            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                   #
#       Creation Date  : September 19, 2019                                      #
#                                                                                #
##################################################################################

from datetime import date

if __name__ == "__main__":
    valid = False
    month, day = 0, 0
    while not valid:
        try:
            print("Enter month and date (separated by a single space): ", end="")
            month, day = map(int, input().split())
            valid = True
        except ValueError as ve:
            print(f"[ERROR]: Invalid input. Please try again.")
    weeks = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
             4: 'Thursday', 5: 'Friday', 6: 'Saturday',
             7: 'Sunday'}
    w = date.isoweekday(date(year=2016, month=month, day=day))
    print(f"Name of the date: {weeks[w]}")