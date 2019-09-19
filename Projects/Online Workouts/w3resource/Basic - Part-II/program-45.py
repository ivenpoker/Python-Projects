#!/usr/bin/env  python3

##################################################################################
#                                                                                #
#       Program purpose: Does some checks on circles.                            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                   #
#       Creation Date  : September 19, 2019                                      #
#                                                                                #
##################################################################################

class Point:

    x_cord = 0
    y_cord = 0

    def __init__(self, x_cord: 0, y_cord: 0):
        self.x_cord = x_cord
        self.y_cord = y_cord

    def set_x_cord(self, new_x_cord: int):
        self.x_cord = new_x_cord

    def set_y_cord(self, new_y_cord: int):
        self.y_cord = new_y_cord

    def get_x_cord(self):
        return self.y_cord

    def get_y_cord(self):
        return self.y_cord

class Circle:

    radius = 0.0
    central_coord = Point(0, 0)

    def __init__(self, central_pt: Point, radius: int):
        self.central_coord = central_pt
        self.radius = radius

    def get_central_point(self):
        return self.central_coord

    def set_central_point(self, new_point: Point):
        self.central_coord = new_point

    def get_radius(self):
        return self.radius

def compute_pt_distance(point_a: Point, point_b: Point):
    import math
    return math.sqrt((point_a.get_x_cord() - point_b.get_x_cord()) ** 2 +
                     (point_a.get_y_cord() - point_b.get_y_cord()) ** 2)

def get_circle_data(input_mess):
    valid = False
    circle = 0
    while not valid:
        try:
            data = input(input_mess).strip().split(' ')
            pt = Point(x_cord=int(data[0]), y_cord=int(data[1]))
            circle = Circle(central_pt=pt, radius=int(data[2]))
            valid = True
        except ValueError as ve:
            print(f"[ERROR] Invalid data. Try again")
    return circle

if __name__ == "__main__":

    circle_a = get_circle_data("Enter circle A's data [as x y r]: ")
    circle_b = get_circle_data("Enter circle B's data [as x y r]: ")

    dist = compute_pt_distance(circle_a.get_central_point(), circle_b.get_central_point())

    if dist < (circle_a.get_radius() - circle_b.get_radius()):
        print(f"Circle B is in Circle A")
    elif dist < (circle_b.get_radius() - circle_a.get_radius()):
        print(f"Circle As in in Circle B")
    elif dist > (circle_a.get_radius() + circle_b.get_radius()):
        print("Circumferences of Circle A and Circle B intersects")
    else:
        print("Circle A and Circle B do not overlap")