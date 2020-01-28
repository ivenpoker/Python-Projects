#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Computes a dog's age in dog's years.                              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 28, 2019                                                  #
#                                                                                          #
############################################################################################

def obtain_dog_age(input_mess: str) -> int:
    dog_age, valid = int(-1), False
    while not valid:
        try:
            dog_age = int(input(input_mess))
            if dog_age <= 0:
                raise ValueError(f"Invalid dog age '{dog_age}'. Must be > 0")
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return dog_age

def convert_to_dog_age(human_dog_age: int) -> int:
    dog_year = human_dog_age * 10.5 if human_dog_age <= 2 else 21 + (human_dog_age - 2) * 4
    return dog_year

if __name__ == '__main__':
    age = obtain_dog_age(input_mess="Enter a dog's age in human years: ")
    print(f"The dog's age in dog's years is: {convert_to_dog_age(human_dog_age=age)}")
