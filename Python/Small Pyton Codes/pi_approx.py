import math

def calculateBest(n, start, end):
    best = 0
    start = math.floor(start)
    end = math.ceil(end)
    for i in range(start, end):
        result = i**(1/n)
        if math.fabs(result - math.pi) < math.fabs(best - math.pi):
            best = result
        else:
            return (i-1, (i-1)**(1/n))

def main():
    start = 3
    end = 3.2

    bestPossible = 0
    bestPower = 0
    bestNumber = 0

    for n in range(3, 17):
        result = calculateBest(n, start**n, end**n)
        number, approx = result
        if math.fabs(approx - math.pi) < math.fabs(bestPossible - math.pi):
            bestPossible = approx
            bestPower = n
            bestNumber = number
        print(f'{number}**(1/{n}): {approx}')

    print('-' * 20)
    print(f"Best: {bestNumber} ** (1/{bestPower}): {bestPossible}")

if __name__ == '__main__':
    main()
