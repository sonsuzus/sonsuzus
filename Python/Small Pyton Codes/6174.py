import random

def getNewRandom(digits:int):
    myList = list()
    a = 0
    for i in range(digits):
        a = random.randrange(0 if i != 0 else 1, 10)
        myList.append(a)

    if len(set(myList)) == 1:
        return getNewRandom(digits)
    return int(''.join(str(i) for i in myList))

def T(x:int):
    x_str = str(x)
    x_str = [char for char in x_str]
    b2k = x_str.copy()
    k2b = x_str.copy()
    b2k.sort(reverse=True)
    k2b.sort()
    ret_val = int(''.join(b2k)) - int(''.join(k2b))
    if len(str(ret_val)) < len(str(x)):
        ret_val *= 10
    return ret_val

def main():
    sets = list()
    temp_set = set()
    for k in range(8):
        myNumbers = list()
        for i in range(100):
            myNumbers.append(getNewRandom(2 + k))
        for i in range(100):
            myNumbers = list(map(T, myNumbers)).copy()
            temp_set = set(myNumbers)
        sets.append(temp_set)
    x = 2
    for i in sets:
        print(x, "basamaklılar:", i, len(i), "tane eleman")
        x += 1

if __name__ == '__main__':
    main()