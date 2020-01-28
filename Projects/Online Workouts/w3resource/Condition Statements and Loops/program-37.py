#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Reads two integers representing a month and day and prints the    #
#                        season for that month and day.                                    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 28, 2019                                                  #
#                                                                                          #
############################################################################################

def obtain_user_data(input_mess: str, expected_type=str) -> [int, str]:
    user_data, valid = '', False
    while not valid:
        try:
            if expected_type == 'int':
                user_data = int(input(input_mess))
                valid = True
            elif expected_type == 'str':
                user_data = input(input_mess)
                if len(user_data) == 0:
                    raise ValueError(f"Oops, data needed!")
            else:
                raise ValueError(f"Invalid specified type '{expected_type}'")
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def get_season(some_month: str, some_day: int) -> str:
    if some_month.lower() in ('january', 'february', 'march'):
        season = 'winter'
    elif some_month.lower() in ('april', 'may', 'june'):
        season = 'spring'
    elif some_month.lower() in ('july', 'august', 'september'):
        season = 'summer'
    else:
        season = 'autumn'

    if some_month == 'march' and some_day > 19:
        season = 'spring'
    elif month_name == 'june' and some_day > 20:
        season = 'summer'
    elif month_name == 'september' and some_day > 21:
        season = 'winter'

    return season


if __name__ == "__main__":
    month_name = obtain_user_data(input_mess='Enter the month name: ', expected_type='str')
    month_day = obtain_user_data(input_mess='Enter the month day: ', expected_type='int')

    print('-' * 25)
    print(f'Season: {get_season(some_month=month_name, some_day=month_day)}')

