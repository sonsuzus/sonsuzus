import turtle
import math

class Dog:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.shape('turtle')
        self.rotation = 0
        self.speed = 0.1
        self.turtle.speed(100)

    def rotate(self, degrees):
        self.rotation += degrees
        self.turtle.left(degrees)

    def towards(self, dog):
        return self.turtle.towards(dog.turtle.pos()) - self.rotation

    def moveForward(self):
        self.turtle.forward(self.speed)

    def getPosition(self):
        return self.turtle.pos()


dogs = list()
length = 10
screen = turtle.Screen()

def moveTo(m_dog: Dog, x, y):
    m_dog.turtle.penup()
    m_dog.turtle.goto(x, y)
    m_dog.turtle.pendown()

def main():
    screen.setworldcoordinates(-1, -1, 1, 1)
    dogSetup()
    for i in range(200):
        whistle()
        
    turtle.mainloop()


def whistle():
    next_dog = lambda i: i + 1 if i != 3 else 0
    angles = [dogs[i].towards(dogs[next_dog(i)]) for i in range(4)]
    for i in range(4):
        dogs[i].rotate(angles[i])
    for dog in dogs:
        dog.moveForward()


def dogSetup():
    for i in range(4):
        dogs.append(Dog())
        dogs[-1].rotate(i * 90)
    moveTo(dogs[0], -length / 2, -length / 2)
    moveTo(dogs[1], length / 2, -length / 2)
    moveTo(dogs[2], length / 2, length / 2)
    moveTo(dogs[3], -length / 2, length / 2)



if __name__ == '__main__':
    main()