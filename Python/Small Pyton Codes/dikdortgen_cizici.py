w = int(input("Width: "))
h = int(input("Height: "))

for i in range(h):
    for j in range(w):
        if i == 0 or j == 0 or i == h - 1 or j == w - 1: print("* ",end="")
        else: print("  ",end="")
    print()
