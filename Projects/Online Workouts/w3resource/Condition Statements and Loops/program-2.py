#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Converts from celcius to fahrenheit and vice versa.               #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 21, 2019                                                  #
#                                                                                          #
############################################################################################

def convert_fah_to_cel(fahrenheit: float) -> float:
    return (fahrenheit - (32/9)) * 5


def convert_cel_to_fah(celcius: float) -> float:
    return ((celcius * 9)/5 + 32) / 9

if __name__ == "__main__":

    print(f'60c is {convert_cel_to_fah(celcius=60)} fahrenheit')
    print(f'45c is {convert_fah_to_cel(fahrenheit=45)} celcius')
