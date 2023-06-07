def gcd(a:int, b:int):
    i = 0
    if a < b: i = a
    else: i = b 
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i -= 1

a = int(input())
print("-" * len(str(a)))
b = int(input())
print()
print()
print(a // gcd(a, b))
print(len(str(gcd(a, b) / a)) * "-")
print(b // gcd(a, b))