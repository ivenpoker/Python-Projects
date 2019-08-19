# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Calculates midpoint of a line.                               #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 19, 2019                                              #
#                                                                                     #
#######################################################################################

class Point:

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = x

    def __str__(self):
        return f"[{self.x}, {self.y}]"

    def getX(self):
        return self.x

    def getY(self):
        return self.y

def get_point(list_data):
    return Point(x=float(list_data[0]), y=float(list_data[1]))

def find_mid_point(ptA, ptB):
    return Point(x=((ptA.getX() + ptB.getX()) / 2), y=((ptB.getY() + ptB.getY()) / 2))


if __name__ == "__main__":
    try:
        pointA = get_point(input("Enter Point A [as: x y]: ").strip().split(" "))
        pointB = get_point(input("Enter Point B [as: x y]: ").strip().split(" "))

    except ValueError as val_err:
        print(f"Error with input: {val_err}")

    print(f"Midpoint is: {find_mid_point(pointA, pointB)}")

