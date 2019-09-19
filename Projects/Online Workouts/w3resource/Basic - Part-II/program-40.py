#################################################################################
#                                                                               #
#       Program purpose: Checks if a point (x, y) is in a triangle or not.      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                  #
#       Creation Date  : September 10, 2019                                     #
#                                                                               #
#################################################################################


class Point:
    def __init__(self, x: 0, y: 0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, new_x: int):
        self.x = new_x

    def set_y(self, new_y: int):
        self.y = new_y

    def __str__(self):
        return f"pt-[{self.x}, {self.y}]"

def read_point(input_mess: str):

    valid = False
    pt = Point(0, 0)

    while not valid:
        try:
            data = input(input_mess).strip().split(" ")
            pt.set_x(int(data[0]))
            pt.set_y(int(data[1]))
            valid = True
        except ValueError as ve:
            print(f"{ve}")
    return pt

def check_in_triangle(triangle_points, check_pt: Point):

    x1, y1 = triangle_points[0].get_x(), triangle_points[0].get_y()
    x2, y2 = triangle_points[0].get_x(), triangle_points[0].get_y()
    x3, y3 = triangle_points[0].get_x(), triangle_points[0].get_y()
    xp, yp = check_pt.get_x(), check_pt.get_y()

    c1 = (x2 - x1) * (yp - y1) - (y2 - y1) * (xp - x1)
    c2 = (x3 - x2) * (yp - y2) - (y3 - y2) * (xp - x2)
    c3 = (x1 - x3) * (yp - y3) - (y1 - y3) * (xp - x3)

    return (c1 < 0 and c2 < 0 and c3 < 0) or (c1 > 0 and c2 > 0 and c3 > 0)

if __name__ == "__main__":

    pointA = read_point("Enter triangle point A [as -> x y]: ")
    pointB = read_point("Enter triangle point B [as -> x y]: ")
    pointC = read_point("Enter triangle point C [as -> x y]: ")
    pointD = read_point("Enter triangle point to check [as -> x y]: ")

    point_list = [pointA, pointB, pointC]

    if check_in_triangle(point_list, pointD):
        print(f"Point {pointD} is in triangle")
    else:
        print(f"Point {pointD} is not in triangle")


