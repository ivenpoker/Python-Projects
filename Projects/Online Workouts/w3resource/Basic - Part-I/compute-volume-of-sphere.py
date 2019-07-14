#!/usr/bin/env  python3

####################################################################################
#                                                                                  #
#       Program purpose: Computes the volume of a sphere for a given radius.       #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                     #
#       Creation Date  : 19/04/2019                                                #
#                                                                                  #
####################################################################################

def compute_volume_of_sphere(_radius):
    import math
    return float(4/3) * math.pi * pow(_radius, 3)

def main():
    radius = float(input("Enter radius of sphere: "))
    print("Volume of sphere is: {}".format(compute_volume_of_sphere(radius)))


if __name__ == '__main__':
    main()