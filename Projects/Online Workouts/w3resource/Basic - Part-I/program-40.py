# !/usr/bin/env  python3

################################################################################
#                                                                              #
#       Program purpose: Computes the distance between two points.             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                 #
#       Creation Date  : August 9, 2019                                        #
#                                                                              #
################################################################################

def getPoint(pointName):
    point = []         # structure to store point coordinates
    point.append(int(input(f"Enter x-coordinate for {pointName}: ")))
    point.append(int(input(f"Enter y-coordinate for {pointName}: ")))

    return point

def computeDistanceBetweenPoints(listOfPoints):
    if len(listOfPoints) != 2:
        return "Error"
    import math
    ptA_x = listOfPoints[0][0]
    ptA_y = listOfPoints[0][1]
    ptB_x = listOfPoints[1][0]
    ptB_y = listOfPoints[1][1]

    return math.sqrt(math.pow(ptB_x - ptA_x, 2) + math.pow(ptB_y - ptA_y, 2))


if __name__ == "__main__":

    pointList = []
    pointList.append(getPoint("Point A"))
    pointList.append(getPoint("Point B"))

    print(f"Distance between points: {computeDistanceBetweenPoints(pointList)}")




