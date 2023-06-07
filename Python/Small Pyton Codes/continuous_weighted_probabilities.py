import numpy as np
import math
from math import *

def linearWeight(x):
    return x

def quadraticWeight(x):
    return x**2

def exponentialWeight(x):
    return math.exp(x)

def inverseWeight(x):
    return 1/x

def main():
    a = float(eval(input('a: ')))
    b = float(eval(input('b: ')))
    dx = 1e-5

    weight_func = linearWeight
    interval = np.arange(a, b+dx, dx)
    print(interval)
    weights = map(weight_func, interval)
    weights = np.array( list(weights) )
    total_weight = sum(weights)

    expectedValue = 0
    for i in range(len(interval)):
        expectedValue += interval[i] * weight_func(interval[i])

    expectedValue /= total_weight
    print("Expected values:", expectedValue)


if __name__ == '__main__':
    main()