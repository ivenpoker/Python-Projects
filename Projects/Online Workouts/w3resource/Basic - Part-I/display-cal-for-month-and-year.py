#!/usr/bin/env python3

###################################################################################
#                                                                                 #
#       Program purpose: Display calendar for a specified day and year            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                    #
#       Creation Date  : 19/04/2019                                               #
#                                                                                 #
###################################################################################

def display_calendar(year, month):
    import calendar
    print(calendar.month(year, month))

def main():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    display_calendar(year, month)

if __name__ == '__main__':
    main()