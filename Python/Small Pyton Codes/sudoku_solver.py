sudoku = list()

"""
Squares: 
+-+-+-+
|0|1|2|
|3|4|5|
|6|7|8|
+-+-+-+
"""
def getSquare(game:list, square_num:int):
    my_list = list()
    for i in range(3):
        for j in range(3):
            if square_num == 0:
                my_list.append(game[i][j])
            elif square_num == 1:
                my_list.append(game[i][3 + j])
            elif square_num == 2:
                my_list.append(game[i][6 + j])
            elif square_num == 3:
                my_list.append(game[3 + i][j])
            elif square_num == 4:
                my_list.append(game[3 + i][3 + j])
            elif square_num == 5:
                my_list.append(game[3 + i][6 + j])
            elif square_num == 6:
                my_list.append(game[6 + i][j])
            elif square_num == 7:
                my_list.append(game[6 + i][3 + j])
            elif square_num == 8:
                my_list.append(game[6 + i][6 + j])
    return my_list

# Checks in all rows
def checkRows(game:list):
    for row in range(9):
        empty_characters = list()
        needed_characters = dict()
        # Empty characters
        for x in range(9):
            if game[row][x] == ' ':
                empty_characters.append((x, row)) # (x, y)
        # Find needed numbers
        for empty in empty_characters:
            needed_characters[empty] = set(range(1, 10))
            for _x in range(9):
                x, y = empty
                try:
                    needed_characters[empty].remove(int(game[_x][x]))
                except:
                    pass
                try:
                    needed_characters[empty].remove(int(game[y][_x]))
                except:
                    pass
        for key in needed_characters.keys():
            if len(needed_characters[key]) == 1:
                mylist = list(game[key[1]])
                mylist[key[0]] = str(next(iter(needed_characters[key])))
                game[key[1]] = "".join(mylist)
        # Solve
        for num in range(1, 10):
            found = 0
            for key in needed_characters.keys():
                if num in needed_characters[key]:
                    found += 1
            if found == 1:
                for key in needed_characters.keys():
                    if num in needed_characters[key]:
                        mylist = list(game[key[1]])
                        mylist[key[0]] = str(num)
                        game[key[1]] = "".join(mylist)

# Checks in all columns
def checkCols(game:list):
    for col in range(9):
        empty_characters = list()
        needed_characters = dict()
        # Find all empty characters
        for y in range(9):
            if game[y][col] == ' ':
                empty_characters.append((col, y))
        # Save needed numbers
        for empty in empty_characters:
            needed_characters[empty] = set(range(1, 10))
            for _x in range(9):
                x, y = empty
                try:
                    needed_characters[empty].remove(int(game[y][_x]))
                except:
                    pass
                try:
                    needed_characters[empty].remove(int(game[_x][x]))
                except:
                    pass
        # Solve
        for key in needed_characters.keys():
            if len(needed_characters[key]) == 1:
                mylist = list(game[key[1]])
                mylist[key[0]] = str(next(iter(needed_characters[key])))
                game[key[1]] = "".join(mylist)
        for num in range(1, 10):
            found = 0
            for key in needed_characters.keys():
                if num in needed_characters[key]:
                    found += 1
            if found == 1:
                for key in needed_characters.keys():
                    if num in needed_characters[key]:
                        mylist = list(game[key[1]])
                        mylist[key[0]] = str(num)
                        game[key[1]] = "".join(mylist)


# Checks in all 3x3 squares
def checkSquares(game:list):
    for i in range(9):
        # Find empty characters
        empty_characters = list()
        inth_square = getSquare(game, i)
        for j in range(len(inth_square)):
            if inth_square[j] == ' ':
                empty_characters.append((i, j % 3, j // 3)) # (i, xPos, yPos)
        avalible = dict()

        # Find needed numbers
        for k in empty_characters:
            needed_numbers = list(range(1, 10))
            avalible[k] = set()
            for s in inth_square:
                try:
                    needed_numbers.remove(int(s))
                except ValueError:
                    pass
            for l in list(range(1, 10)):
                x = (k[0] % 3) * 3 + k[1]
                y = (k[0] // 3) * 3 + k[2]
                for _x in range(9):
                    if game[_x][x] == str(l):
                        try:
                            needed_numbers.remove(l)
                        except ValueError:
                            pass
                    elif game[y][_x] == str(l):
                        try:
                            needed_numbers.remove(l)
                        except ValueError:
                            pass
            for _ in needed_numbers:
                avalible[k].add(_)
        # Solve
        for keys in avalible.keys():
            if len(avalible[keys]) == 1:
                x_pos = (keys[0] % 3) * 3 + keys[1]
                y_pos = (keys[0] // 3) * 3 + keys[2]
                my_list = list(game[y_pos])
                my_list[x_pos] = str(next(iter(avalible[keys])))
                game[y_pos] = "".join(my_list)

        for num in range(1, 10):
            found = 0
            for keys in avalible.keys():
                if num in avalible[keys]:
                    found += 1
            if found == 1:
                for keys in avalible.keys():
                    if num in avalible[keys]:
                        x_pos = (keys[0] % 3) * 3 + keys[1]
                        y_pos = (keys[0] // 3) * 3 + keys[2]
                        my_list = list(game[y_pos])
                        my_list[x_pos] = str(num)
                        game[y_pos] = "".join(my_list)

"""
Inputs:
- Input must be line by line
- Put spaces for characters that you don't know
 
Example input:
 6 8  5  
  5   367
37  658 9
6 9  21  
  14892  
   3 69  
 5    4  
 1 547  3
 96 38 51
"""
def getInput(game:list):
    # Getting Input
    for i in range(9):
        line = input()
        if len(line) != 9:
            print("Unresolved input!")
            exit(0)
        for c in line:
            if c.isalpha() or not (c.isspace() or c.isdigit()):
                print("Unresolved input!")
                exit(0)
        game.append(line)

def solve(game:list):
    checkCols(game)
    checkRows(game)
    checkSquares(game)

def main():
    print("Welcome to sudoku solver! Type your sudoku down below (space for unknown characters):")
    getInput(sudoku)
    i = 0
    maxTry = 100
    while True:
        solve(sudoku)
        solved = True
        for a in sudoku:
            if ' ' in a:
                solved = False
        if i >= maxTry or solved:
            break
        i += 1
    if i == maxTry:
        print("Unfortunately... I couldn't solve it.")
        for x in sudoku:
            for y in x:
                print(y, end = '')
            print()
        exit(0)
    print("There's the answer:")
    for i in sudoku:
        for j in i:
            print(j, end='')
        print()

if __name__ == "__main__":
    main()