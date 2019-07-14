#!/usr/bin/env  python3

#: Program Purpose:
#:          Obtains from user the radius of a circle and
#:          Computes it's area.
#:
#: Program Author : Happi Yvan <ivensteinpoker@gmail.com>
#: Program Date   : 11/04/2019

def compute_area(radius):
    import math
    return math.pi * (radius * radius)

def main():
    radius = float(input("Enter radius of circle: "))
    print("Area of circle is: %f" % (compute_area(radius)))

if __name__ == '__main__':
    main()