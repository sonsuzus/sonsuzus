try:
    import os,sys
    import ctypes
    from ctypes import c_long, c_wchar_p, c_ulong, c_void_p
    from termcolor import colored
    from colorama import Fore, Back, Style
    import colorama
    from enum import Enum
    import random
    from msvcrt import getch, getche, kbhit
    import win32gui
    import time
except ImportError:
    output = str(sys.exc_info()[1])
    module_name = ""
    temporary = False
    for i in output:
        if i == "'":
            temporary = not temporary
            continue
        if temporary:
            module_name += i
    print("No module named {}! You should use 'pip install {}'".format(module_name,module_name))
    exit(0)

gHandle = ctypes.windll.kernel32.GetStdHandle(c_long(-11))

def move (y, x):
   value = x + (y << 16)
   ctypes.windll.kernel32.SetConsoleCursorPosition(gHandle, c_ulong(value))

class Vector2:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

class Direction(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3

def randomPair(size:Vector2):
    return Vector2(random.randint(1, size.x - 2), random.randint(1, size.y - 2))

head = "O"
tail = "o"
size = Vector2(30, 30)
wall = '█'
fruit = '■'
headPos = Vector2(15, 10)
tails = list()
wallColor = Fore.WHITE
headColor = Fore.LIGHTMAGENTA_EX
tailColor = Fore.LIGHTBLUE_EX
fruitColor = Fore.RED
default_console_size = Vector2(os.get_terminal_size().columns, os.get_terminal_size().lines)

def main():
    score = 0
    gameOver = False
    dir = Direction.RIGHT
    fruitPos = randomPair(size)
    colorama.init()
    tails.append(Vector2(headPos.x - 1, headPos.y))
    tails.append(Vector2(headPos.x - 2, headPos.y))
    os.system("mode con: cols={} lines={}".format(size.x + 2, size.y + 7))
    os.system("cls")
    while not gameOver:
        move(0, 0)
        print()
        print(("{:^" + str(size.x + 2) + "}").format("SNAKE GAME"))
        print()
        for y in range(size.y):
            print(" ", end='')
            for x in range(size.x):
                printed = False
                if x == 0 or y == 0 or x == size.x - 1 or y == size.y - 1:
                    print(wallColor + wall, end='')
                    printed = True
                elif x == headPos.x and y == headPos.y:
                    print(headColor + head, end='')
                    printed = True
                elif x == fruitPos.x and y == fruitPos.y:
                    print(fruitColor + fruit, end = '')
                    printed = True
                for t in tails:
                    if x == t.x and y == t.y:
                        printed = True
                        print(tailColor + tail, end='')
                if not printed:
                    print(" ", end='')
            print(Style.RESET_ALL + " ")
        print()
        print(("{:^" + str(size.x + 2) + "}").format("Score: {}".format(score)))
        print()
        if kbhit():
            try:
                key = getch().lower().decode("utf-8")
            except:
                pass
            if key == 'w' and dir != Direction.DOWN: dir = Direction.UP
            elif key == 'a' and dir != Direction.RIGHT: dir = Direction.LEFT
            elif key == 's' and dir != Direction.UP: dir = Direction.DOWN
            elif key == 'd' and dir != Direction.LEFT: dir = Direction.RIGHT
            elif key == 'x':
                os.system("mode con: cols={} lines={}".format(default_console_size.x, default_console_size.y))
                exit(0)
        if headPos.x == fruitPos.x and headPos.y == fruitPos.y:
            fruitPos = randomPair(size)
            score += 10
            tails.append(Vector2(tails[-1].x, tails[-1].y))
            for t in range(len(tails)):
                if (tails[t].x == fruitPos.x and tails[t].y == fruitPos.y) or (headPos.x == fruitPos.x and headPos.y == fruitPos.y):
                    t = 0
                    fruitPos = randomPair(size)
        for i in range (1, len(tails)):
            tails[-i].x = tails[-i - 1].x
            tails[-i].y = tails[-i - 1].y
        tails[0].x = headPos.x
        tails[0].y = headPos.y
        if dir == Direction.RIGHT: headPos.x += 1
        elif dir == Direction.LEFT: headPos.x -= 1
        elif dir == Direction.UP:
            headPos.y -= 1
        elif dir == Direction.DOWN: headPos.y += 1
        if headPos.x == 0 or headPos.x == size.x - 1 or headPos.y == 0 or headPos.y == size.y - 1:
            gameOver = True
        for i in tails:
            if i.x == headPos.x and i.y == headPos.y:
                gameOver = True
    print("You Died! ", end='')
    os.system("pause")
    os.system("mode con: cols={} lines={}".format(default_console_size.x, default_console_size.y))


if __name__ == "__main__":
    main()
