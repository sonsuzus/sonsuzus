import random
toplam=0
for deneme in range(1,10000):
    gerceklesti = 0
    for olay in range(0,24):
        a = random.randint(0,23)
        if a == 13:
            gerceklesti += 1
    if gerceklesti == 1:
        toplam += 1
print(toplam)


