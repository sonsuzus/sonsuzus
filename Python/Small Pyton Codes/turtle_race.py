import turtle
from time import sleep
from random import shuffle, randint

turtleCount = 6
maxCount = 15
minCount = 2
colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue',
              'cyan', 'turquoise', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray', 'white']

windowSize = (800, 600)

def setPos(m_turtle, x, y):
    m_turtle.penup()
    m_turtle.goto(x, y)
    m_turtle.pendown()

def main():
    global turtleCount
    while (turtleCount := int(input('Tutle count: '))) > maxCount or turtleCount < minCount:
        if turtleCount < minCount:
            print('Sorry! minimum tutle count is', minCount)
        else:
            print('Sorry! maximum tutle count is', maxCount)
    windowSetup()
    drawFinishLine()
    my_turtles = turtleSetup()
    play(my_turtles)

    turtle.done()


def drawFinishLine():
    finish_line = turtle.Turtle()
    finish_line.shape('square')
    finish_line.shapesize(0.01)
    setPos(finish_line, windowSize[0] / (turtleCount + 1) - (450), (windowSize[1] / 2 - 50))
    finish_line.forward((turtleCount - 1) * windowSize[0] / (turtleCount + 1) + 100)


def play(my_turtles):
    while True:
        end = False
        for bob in my_turtles:
            bob.forward(randint(0, 20))
            if bob.pos()[1] > (windowSize[1] / 2 - 50):
                print(bob.color()[0], 'one wins')
                end = True
                break
        if end:
            break


def turtleSetup():
    turtles = list()
    shuffle(colors)

    for i in range(turtleCount):
        turtles.append(turtle.Turtle())
        turtles[i].shape('turtle')
        turtles[i].speed(5)

    for i in range(turtleCount):
        turtles[i].color(colors[i], colors[i])

    for i in range(turtleCount):
        bob = turtles[i]
        bob.left(90)
        setPos(bob, (i + 1) * windowSize[0] / (turtleCount + 1) - (windowSize[0] / 2), -(windowSize[1] / 2 - 50))

    return turtles


def windowSetup():
    window = turtle.Screen()
    window.setup(width=windowSize[0], height=windowSize[1], startx=0, starty=0)
    turtle.bgcolor('lightgreen')
    winfo = window.getcanvas().winfo_toplevel()
    winfo.call('wm', 'attributes', '.', '-topmost', '1')
    winfo.call('wm', 'attributes', '.', '-topmost', '0')


if __name__ == '__main__':
    main()