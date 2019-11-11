#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Generates a 3*4*6 3D array whose each element is *.               #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 11, 2019                                                 #
#                                                                                          #
############################################################################################

def array_2D(row: int, height: int, char: str) -> list:
    return [list(char * height) for _ in range(row)]

def array_3D(dim_3d: int, array_2d: list) -> list:
    return [array_2d for _ in range(dim_3d)]

if __name__ == "__main__":
    data_2D = array_2D(row=4, height=6, char='*')
    new_data_3D = array_3D(dim_3d=3, array_2d=data_2D)
    print(f'Generated data:\n{new_data_3D}')
