import math

def my_sqrt(x:float):
    negative = True if x < 0 else False
    num = math.fabs(x)
    i = 0
    add = 1
    temp = 0
    while True:
        if i * i > num:
            i -= add
            add /= 10
            temp += 1
        elif i * i == num or temp > 7:
            return (i*1j if negative else i)
        i += add

a = float(input("Type a number: "))
c = None
print("My sqrt: ",my_sqrt(a))
if a < 0: c = a + 0j
else: c = a
print("Default sqrt: ",math.sqrt(c))
