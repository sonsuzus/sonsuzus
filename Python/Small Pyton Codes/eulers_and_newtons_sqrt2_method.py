from math import sqrt

def F(y):
    return 1 / (2 * y)

def eulers(steps):
    y = 1
    h = 1 / steps
    for i in range(steps):
        y = y + h * F(y)
    return y

def newtons(steps):
    if steps == 0:
        return 1
    return 0.5 * (newtons(steps - 1) + (2 / newtons(steps - 1)))

print("Euler's 100:", eulers(100))
print("Newton's 100:", newtons(10))
print(sqrt(2))
