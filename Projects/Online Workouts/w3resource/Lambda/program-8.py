#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Extracts year, month, day and time using lambdas.                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 04, 2020                                                 #
#                                                                                          #
############################################################################################

from typing import Callable
import datetime

def func_extract_year(some_date: datetime) -> Callable:
    return lambda: some_date.year

def func_extract_month(some_date: datetime) -> Callable:
    return lambda: some_date.month

def func_extract_day(some_date: datetime) -> Callable:
    return lambda: some_date.day

def func_extract_time(some_date: datetime) -> Callable:
    return lambda: some_date.time()

if __name__ == "__main__":

    now = datetime.datetime.now()
    print(f'Date: {now}')

    print('-' * 35)

    year_lambda = func_extract_year(some_date=now)
    month_lambda = func_extract_month(some_date=now)
    day_lambda = func_extract_day(some_date=now)
    time_lambda = func_extract_time(some_date=now)

    print(f'Year: {year_lambda()}')
    print(f'Month: {month_lambda()}')
    print(f'Day: {day_lambda()}')
    print(f'Time: {time_lambda()}')
