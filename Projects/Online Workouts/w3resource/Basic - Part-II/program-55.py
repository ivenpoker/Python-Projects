#!/usr/bin/env  python3

####################################################################################
#                                                                                  #
#       Program purpose: Given 4 points on a plane, program test if the points are #
#                        orthogonal or not.                                        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                     #
#       Creation Date  : September 23, 2019                                        #
#                                                                                  #
####################################################################################

class Point:

    def __init__(self, x_cord: int, y_cord: int):
        self.x_cord = x_cord
        self.y_cord = y_cord

    def get_x_cord(self):
        return self.x_cord

    def get_y_cord(self):
        return self.y_cord

    def set_x_cord(self, new_x_cord: int):
        self.x_cord = new_x_cord

    def set_y_cord(self, new_y_cord: int):
        self.y_cord = new_y_cord

def get_point(mess: str):
    valid = False
    point = Point(x_cord=0, y_cord=0)

    while not valid:
        try:
            x_cord, y_cord = map(float, input(mess).split())
            point.set_x_cord(new_x_cord=x_cord)
            point.set_y_cord(new_y_cord=y_cord)
            valid = True
        except ValueError as ve:
            print(f"[ERROR]: {ve}")
    return point

def point_orthogonal(pt_P: Point, pt_Q: Point, pt_R: Point, pt_S: Point):

    pq_x, pq_y = pt_Q.get_x_cord() - pt_P.get_x_cord(), pt_Q.get_y_cord() - pt_P.get_y_cord()
    rs_x, rs_y = pt_S.get_x_cord() - pt_R.get_x_cord(), pt_S.get_y_cord() - pt_R.get_y_cord()
    rs = pq_x * rs_x + pq_y * rs_y

    return abs(rs) > 1e-10



if __name__ == "__main__":

    point_P = get_point(mess="Enter coordinates for point P [as x y]: ")
    point_Q = get_point(mess="Enter coordinates for point Q [as x y]: ")
    point_R = get_point(mess="Enter coordinates for point R [as x y]: ")
    point_S = get_point(mess="Enter coordinates for point S [as x y]: ")

    if point_orthogonal(pt_P=point_P, pt_Q=point_Q, pt_R=point_R, pt_S=point_S):
        print("PQ and RS are NOT orthogonal!")
    else:
        print("PQ and CD are orthogonal!")



