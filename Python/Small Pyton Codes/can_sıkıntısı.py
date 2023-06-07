from cmath import log
import sys

sys.setrecursionlimit(1500)

sqrt5 = 5**.5
phi = (1 + sqrt5)/2


def inv_fib_r1(x, rec):
	if rec == 1000:
		return 1
	return log( (x*sqrt5 + (5*x*x + 4*(-1)**inv_fib_r1(x, rec + 1))**.5) / 2, phi )
	
def inv_fib_r2(x, rec):
	if rec == 1000:
		return 1
	return log( (x*sqrt5 - (5*x*x + 4*(-1)**inv_fib_r1(x, rec + 1))**.5) / 2, phi )
	

def fib(x):
	return (phi**x - (-1/phi)**x)/sqrt5

inp = complex(input("> "))
r1 = inv_fib_r1(inp, 0)
r2 = inv_fib_r2(inp, 0)

print("x1:", r1)
print("x2:", r2)
print("fib(x1):", fib(r1))
print("fib(x2):", fib(r2))
