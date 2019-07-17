
# !/usr/bin/env  python3

#############################################################################
#                                                                           #
#       Program purpose: Computes the area of a triangle.                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>              #
#       Creation Date  : July 17, 2019                                      #
#                                                                           #
#############################################################################

# URL: https://www.w3resource.com/python-exercises/python-basic-exercises.php


def triangle_area(base, height):
    return (1/2) * base * height

if __name__ == "__main__":
    base = int(input("Enter base of triangle: "))
    height = int(input("Enter height of triangle: "))

    print(f"Area of triangle: {triangle_area(base=base, height=height)}")
