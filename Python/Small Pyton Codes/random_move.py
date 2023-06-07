import pygetwindow as pg
from win32api import GetSystemMetrics
from random import randint

def getDesktopSize():
    return (GetSystemMetrics(0), GetSystemMetrics(1))

def getWindow(title: str):
    return pg.getWindowsWithTitle(title)[0]

def main():
    title = input('Window title: ')
    window = getWindow(title)
    window.activate()
    window_size = (window.size[0], window.size[1])
    desktop_size = getDesktopSize()
    random_pos = (randint(0, desktop_size[0] - window_size[0]), randint(0, desktop_size[1] - window_size[1]))
    window.moveTo(random_pos[0], random_pos[1])

if __name__ == '__main__':
    main()
