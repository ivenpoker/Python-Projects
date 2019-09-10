#!/usr/bin/env  python3

#################################################################################
#                                                                               #
#       Program purpose: Generate message based on user input.                  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                  #
#       Creation Date  : September 10, 2019                                     #
#                                                                               #
#################################################################################

def get_message(info: {}):
    basic_info = f"Hi there {info['name']}!, nice knowing you!"
    if int(info['age']) < 18:
        basic_info += f" You're relatively young at {info['age']}."

    if 18 < int(info['age']) < 30:
        if info['gender'] == "male":
            basic_info += f" Becoming a man, huh!"

        else:
            basic_info += f" Becoming a woman, hun!"
    elif int(info['age']) < 18:
        basic_info += " Enjoy your teens"
    else:
        basic_info += " You're getting old, you know!"
    basic_info += f" Living in {info['location']} should be pretty fun!"
    return basic_info


if __name__ == "__main__":
    name = str(input("Enter your name: "))
    gender = str(input("Enter your gender: "))
    age = 0
    cont = True

    while cont:
        try:
            age = int(input("Enter your age: "))
            cont = False
        except ValueError as ve:
            print(f"[ERROR]: {ve}")

    location = str(input("Where do you live: "))
    print(get_message({'name': name, 'gender': gender, 'age': age, 'location': location}))


