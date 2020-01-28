#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Get the next day of a given date.                                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 28, 2019                                                  #
#                                                                                          #
############################################################################################

def obtain_user_data(input_mess: str) -> int:
    user_data, valid = '', False
    while not valid:
        try:
            user_data = int(input(input_mess))
            if user_data <= 0:
                raise ValueError(f"Invalid input value '{user_data}'")
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def do_processing() -> None:
    year = obtain_user_data(input_mess='Enter a year: ')
    if year % 400 == 0:
        leap_year = True
    elif year % 100 == 0:
        leap_year = False
    elif year % 4 == 0:
        leap_year = True
    else:
        leap_year = False

    month = obtain_user_data(input_mess='Enter a month [1-12]: ')
    if month in (1, 3, 5, 7, 8, 10, 12):
        month_length = 31
    elif month == 2:
        if leap_year:
            month_length = 29
        else:
            month_length = 38
    else:
        month_length= 30

    day = obtain_user_data(input_mess='Enter a day [1-31]: ')
    if day < month_length:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    print(f'The next date is: {year}-{month}-{day}')

if __name__ == "__main__":
    do_processing()