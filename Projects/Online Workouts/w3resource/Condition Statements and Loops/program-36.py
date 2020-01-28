#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Determines if a user defined triangle is scalene, equilateral or  #
#                        isosceles.                                                        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 28, 2019                                                  #
#                                                                                          #
############################################################################################

class Triangle:
    def __init__(self, side_A: int, side_B: int, side_C: int):
        self.side_A = side_A
        self.side_B = side_B
        self.side_C = side_C

def obtainer_user_data(input_mess: str) -> int:
    user_data, valid = '', False
    while not valid:
        try:
            user_data = int(input(input_mess))
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def is_equilaterial(triangle: Triangle) -> bool:
    return triangle.side_A == triangle.side_B and triangle.side_B == triangle.side_C

def is_scalene(triangle: Triangle) -> bool:
    return triangle.side_A != triangle.side_B and triangle.side_A != triangle.side_C \
           and triangle.side_B != triangle.side_C

def is_isosceles(triangle: Triangle) -> bool:
    if triangle.side_A == triangle.side_B:
        return True
    elif triangle.side_A == triangle.side_C:
        return True
    elif triangle.side_B == triangle.side_C:
        return True
    return False

if __name__ == "__main__":

    side_A = obtainer_user_data(input_mess='Enter triangle side A: ')
    side_B = obtainer_user_data(input_mess='Enter triangle side B: ')
    side_C = obtainer_user_data(input_mess='Enter triangle side C: ')

    new_triangle = Triangle(side_A=side_A, side_B=side_B, side_C=side_C)

    print('-' * 25)

    print(f'Is equilaterial: {is_equilaterial(triangle=new_triangle)}')
    print(f'     Is scalene: {is_scalene(triangle=new_triangle)}')
    print(f'   Is isosceles: {is_isosceles(triangle=new_triangle)}')
