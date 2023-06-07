import turtle
from math import pi, radians

r = 50

bob = turtle.Turtle()
bob.speed(10000)

bob.forward(2 * r)

bob.left(90)
for i in range(315):
    rad = radians(i)
    bob.forward(r * radians(1))
    bob.left(1)

turtle.done()