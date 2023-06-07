import math
import time

def my_log(x, base):
    addition = 1.0
    a = 0.0
    temp = 0
    tempmax = 17
    first = True
    while(True):
        if(math.pow(base, a) > x):
            a -= addition
            addition /= 10
            temp += 1
            if first:
                tempmax -= len(str(a))
                first = False
        if x == math.pow(base, a):
            return a
        if temp >= tempmax:
            return a
        a += addition

print("logx(y)")
x = float(input("x: "))
y = float(input("y: "))

print("My Logarithm Function:  ", my_log(y, x))
print("Real Logarithm:         ", math.log(y, x))
