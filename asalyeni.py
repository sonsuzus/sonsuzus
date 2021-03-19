asallar = [2]
for sayi in range(3,1000):
    for bolen in asallar:
        if sayi%bolen==0:
            break
    else:
        asallar.append(sayi)
print(asallar)