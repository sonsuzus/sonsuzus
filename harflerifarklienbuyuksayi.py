# metinsel yazılımında harfleri farklı en büyük 3 haneli sayıyı bulur
def yaziya(sayi):
    birler = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
    onlar = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
    sayi=str(sayi)
    if sayi[0]=="1":
        return "yüz"+onlar[int(sayi[1])] + birler[int(sayi[2])]
    else:
        return birler[int(sayi[0])]+"yüz" + onlar[int(sayi[1])] + birler[int(sayi[2])]

for i in range(1,899):
    n = 1000-i
    if len(yaziya(n)) == len(set(yaziya(n))):
        print(yaziya(n))
        break