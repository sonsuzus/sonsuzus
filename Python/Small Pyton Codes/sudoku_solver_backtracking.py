import numpy as np

grid = [[0, 0, 0, 0, 9, 0, 2, 0, 5],
	[0, 1, 0, 0, 4, 2, 6, 0, 8],
	[0, 0, 0, 5, 0, 8, 9, 0, 0],
	[0, 7, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 5, 1, 7, 6, 2],
	[0, 0, 0, 4, 0, 3, 8, 0, 0],
	[1, 0, 2, 0, 0, 0, 0, 0, 0],
	[5, 9, 8, 7, 0, 0, 0, 0, 0],
	[0, 0, 4, 0, 1, 9, 0, 8, 0]]

def isPossible(y, x, n):
    global grid
    for i in range(9):
        if grid[y][i] == n:
            return False
    for i in range(9):
        if grid[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if isPossible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(np.matrix(grid))
    input("More?")

solve()
