from turtle import *
from numpy import *

def getBracket(len):
    x = array([-1.0, -1, 1, 1])
    y = array([-1.0, 1, 1, -1])

    x *= len
    y *= len

    return (x, y)

def drawPoints(points):

    x = points[0]
    y = points[1]

    penup()

    for i in range(min(len(x), len(y))):
        goto(x[i], y[i])
        pendown()


def hilbertsCurve(n, l):
    if n == 1:
        return getBracket(l)

    points = hilbertsCurve(n - 1, l * (3/2))

    xscales = array([1.0, 1, 1, -1])
    yscales = array([-1.0, 1, 1, 1])

    xscales /= 3
    yscales /= 3

    rotation = array([[0, -1], [1, 0], [1, 0], [0, -1]])

    xshift = array([-1.0, -1, 1, 1])
    yshift = array([-1.0, 1, 1, -1])

    xshift *= l
    yshift *= l

    allPoints = (array([]), array([]))

    for i in range(4):
        oldX = points[0]
        oldY = points[1]

        newX = ( xscales[i] * ((rotation[i][0] * oldX) - (rotation[i][1] * oldY))) + xshift[i]
        newY = ( yscales[i] * ((rotation[i][1] * oldX) + (rotation[i][0] * oldY))) + yshift[i]

        allPointsX = append(allPoints[0], newX)
        allPointsY = append(allPoints[1], newY)

        allPoints = (allPointsX, allPointsY)

    return allPoints