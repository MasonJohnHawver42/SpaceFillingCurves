from hilbertsCurve import *

def main():
    speed(10)

    for i in [2, 3, 4, 5, 6]:
        points = hilbertsCurve(i, 200)
        print("calculated the points")
        drawPoints(points)

    done()

main()