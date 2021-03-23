a = 0
b = 0
x = 1
y = 2
toplam = 0
while a + x < 2900:
	a += x
	b += y
	x += 2
	y += 2
	toplam = a + b
toplam += (2900 - a)
print("Başlangıçta", toplam, "şeker vardı.")
