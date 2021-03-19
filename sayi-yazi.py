"""
birler = {"b0":"","b1":"bir","b2":"iki","b3":"üç","b4":"dört",
          "b5":"beş","b6":"altı","b7":"yedi","b8":"sekiz","b9":"dokuz"}
onlar = {"o0":"","o1":"on","o2":"yirmi","o3":"otuz","o4":"kırk","o5":"elli",
         "o6":"altmış","o7":"yetmiş","o8":"seksen","o9":"doksan"}
sayi = input("Bir sayı giriniz:")
while len(sayi)<3:
    sayi="0"+sayi
if sayi[0]=="0":
    print(onlar["o"+sayi[1]]+birler["b"+sayi[2]])
elif sayi[0]=="1":
    print("yüz"+onlar["o" + sayi[1]] + birler["b" + sayi[2]])
else:
    print(birler["b"+sayi[0]]+"yüz" + onlar["o" + sayi[1]] + birler["b" + sayi[2]])

#burak onur kod
sayi={1:"bir",2:"iki",3:"uc",4:"dört",5:"bes",6:"alti",7:"yedi",8:"sekiz",9:"dokuz",0:""}
onluk={0:"",1:"on",2:"yirmi",3:"otuz",4:"kirk",5:"elli",6:"altmis",7:"yetmis",8:"seksen",9:"doksan"}
while True:
    x=int(input("1 ile 999 arasinda bir sayi giriniz lütfen"))
    if 0<x<1000:
        break
if x<10:
    print(sayi[x])
if 9<x<100:
    print(onluk[x//10]+sayi[x%10])
if 99<x and x//100!=1:
    print(sayi[x//100]+"yüz"+onluk[(x%100)//10]+sayi[x%10])
elif x//100==1:
    print("yüz"+onluk[(x%100)//10]+sayi[x%10])

y=input()
"""
#girilen sayıyı yazıya çeviren program. 
# maksimum üç haneli sayılar için
birler =["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar =["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
sayi = input("Bir sayı giriniz:")
while len(sayi)<3:
    sayi="0"+sayi
if sayi[0]=="0":
    print(onlar[int(sayi[1])]+birler[int(sayi[2])])
elif sayi[0]=="1":
    print("yüz"+onlar[int(sayi[1])] + birler[int(sayi[2])])
else:
    print(birler[int(sayi[0])]+"yüz" + onlar[int(sayi[1])] + birler[int(sayi[2])])