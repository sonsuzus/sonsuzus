import turtle
import math

def main():
    bob = turtle.Turtle()
    bob.shape('turtle')

    r = 1
    angle = math.radians(0)
    while True:
        bob.goto(r * math.cos(angle), r * math.sin(angle))
        r += 0.1
        angle += math.radians(1)

if __name__ == '__main__':
    main()