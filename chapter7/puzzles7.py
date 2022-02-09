import sys

def moon_weight():
    print("Please enter your current Earth weight")
    weight = float(input())
    print("Please enter the amount your weight might increase each year")
    up = float(input())
    print("Please enter the number of years")
    scale = float(input())
    weight = weight + up * scale
    moon_weight = weight * 0.165
    print("year %s = %f" % (scale, moon_weight))

moon_weight()
