#!/usr/bin/env python3

def display_calendar(year, month):
    import calendar
    print(calendar.month(year, month))

def main():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    display_calendar(year, month)

if __name__ == '__main__':
    main()