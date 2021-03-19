import sqlite3

"""liste = [i for i in range(1, 220//2 + 1) if 220 % i == 0]
print(liste)
print(sum(liste))"""

"""alfabe = "abcçdefgğıijklmnoöprsştuüvyz"
cumle = input("Bir paragraf giriniz: ")
for harf in alfabe:
    sayac=0
    for k in cumle:
        if k==harf:
            sayac+=1
    print("{} harfinden {} adet vardır".format(harf,sayac))"""

for a in range(2,1001):
	for b in range(2,a//2+1):
		if a%b==0:
			break
	else:
		print(a)