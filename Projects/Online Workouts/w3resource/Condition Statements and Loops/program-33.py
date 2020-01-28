#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Converts month name to a number of days.                          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 28, 2019                                                  #
#                                                                                          #
############################################################################################

def obtain_month_name(input_mess: str) -> str:
    user_month, valid = '', False
    while not valid:
        try:
            user_month = input(input_mess)
            if len(user_month) == 0:
                raise ValueError(f"Oops! Month name invalid.")
            valid = True
        except ValueError as ve:
            print(f"[ERROR]: {ve}")
    return user_month

def display_num_of_days(month_name: str) -> None:
    if not month_name or len(month_name) == 0:
        raise ValueError(f"Invalid month name")

    if month_name.lower() == 'february':
        print(f'Number of days: 28/29 days')
    elif month_name.lower() in ('april', 'june', 'september', 'november'):
        print(f'Number of days: 30 days')
    elif month_name.lower() in ('january', 'march', 'may', 'july', 'august', 'october', 'december'):
        print(f'Number of days: 31 days')

if __name__ == '__main__':
    month = obtain_month_name(input_mess='Enter month name: ')
    display_num_of_days(month_name=month)
