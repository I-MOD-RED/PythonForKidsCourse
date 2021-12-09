import turtle
import math

def vecMag(vector : turtle.Vec2D) -> float:
    return math.sqrt(vector[0]*vector[0] + vector[1]*vector[1])

def arcDist(radius : float, angle : float) -> float:
    return (math.pi * radius * angle) / 180

t = turtle.Pen()
# c^2 = a^2 + b^2
# a = b
# c^2 = 2 (a^2)
# (c^2) / 2 = a^2
# a = sqrt(c*c/2)
wallLength = 100.0
roofLength = math.sqrt(wallLength*wallLength/2)
print("Wall length:%f roof length:%f" % (wallLength, roofLength))

# house
t.forward(wallLength)
t.right(90.0)
t.forward(wallLength)
t.right(90.0)
t.forward(wallLength)
t.right(90.0)
t.forward(wallLength)

# roof
t.right(45.0)
t.forward(roofLength)
t.right(90.0)
t.forward(roofLength)

# clear canvas
t.reset()

# spiral
angle = 15.0
distance = 1.0
for i in range(0,50):
    t.forward(distance)
    t.left(angle)
    turtlePos = t.pos()
    vectorMagnitude = vecMag(turtlePos)
    arcLength = arcDist(vectorMagnitude, angle)
    # distance += vectorMagnitude
    # distance += arcLength
    distance += arcLength / vectorMagnitude
    print("Turtle position [%f,%f] magnitude %f arcLength %f distance %f"
          % (turtlePos[0],turtlePos[1],vectorMagnitude,arcLength,distance))

# do not exit until click
turtle.exitonclick()