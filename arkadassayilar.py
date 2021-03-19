def bolenler(n):
  return sum([i for i in range(1,n//2+1) if n%i==0])

arkadas = dict()
for sayi in range(1,10000):
  bt = bolenler(sayi)
  if sayi==bolenler(bt) and sayi<bt:
    arkadas[sayi]=bt
print(arkadas)