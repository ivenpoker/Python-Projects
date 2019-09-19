#!/usr/bin/env python3

#################################################################################
#                                                                               #
#       Program purpose: Test whether two lines are parallel.                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                  #
#       Creation Date  : September 19, 2019                                     #
#                                                                               #
#################################################################################

class Point:

    def __init__(self, x_cord: 0, y_cord: 0):
        self.x_cord = x_cord
        self.y_cord = y_cord

    def set_x_cord(self, new_x_cord: int):
        self.x_cord = new_x_cord

    def set_y_cord(self, new_y_cord: int):
        self.y_cord = new_y_cord

    def get_x_cord(self):
        return self.x_cord

    def get_y_cord(self):
        return self.y_cord


class Line_2D:
    point_a = 0
    point_b = 0

    def __init__(self, point_a: Point(x_cord=0, y_cord=0), point_b: Point(x_cord=0, y_cord=0)):
        self.point_a = point_a
        self.point_b = point_b

    def get_point_a(self):
        return self.point_a

    def get_point_b(self):
        return self.point_b

    def set_point_a(self, new_point_a):
        self.point_a = new_point_a

    def set_point_b(self, new_point_b):
        self.point_b = new_point_b


def read_point(input_mess: str):
    valid = False
    pt = 0
    while not valid:
        try:
            data = list(input(input_mess).split(' '))
            pt = Point(x_cord=int(data[0]), y_cord=int(data[1]))
            valid = True
        except ValueError as ve:
            print(f"[ERROR]: {ve}")
    return pt


def is_parallel(main_line_a: Line_2D, main_line_b: Line_2D):
    return line_2D_gradient(main_line_a) == line_2D_gradient(main_line_b)


def line_2D_gradient(some_line: Line_2D):
    pt_a = some_line.get_point_a()
    pt_b = some_line.get_point_b()

    val_a = pt_b.get_x_cord() - pt_a.get_x_cord()
    val_b = pt_b.get_y_cord() - pt_a.get_x_cord()

    return val_b / val_a


if __name__ == '__main__':

    # Read points for first line
    pt_a = read_point("Enter point A [as x y] for line A: ")
    pt_b = read_point("Enter point B [as x y] for line A: ")

    line_a = Line_2D(point_a=pt_a, point_b=pt_b)

    print(f"{'-' * 30}")

    # Read points for second line
    pt_c = read_point("Enter point A [as x y] for line B: ")
    pt_d = read_point("Enter point B [as x y] for line B: ")

    line_b = Line_2D(point_a=pt_c, point_b=pt_d)

    if is_parallel(main_line_a=line_a, main_line_b=line_b):
        print(f"Lines are parallel")
    else:
        print(f"Lines are NOT parallel")
