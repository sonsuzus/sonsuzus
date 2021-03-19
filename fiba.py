"""fibanocci = [1,1]
for n in range(2,40):
    #fibanocci += [fibanocci[n-2]+fibanocci[n-1]]
    fibanocci.append(fibanocci[n-1]+fibanocci[n-2])

print(fibanocci)"""
#fibanocci dizisini hesaplayan program
#ilk 50 sayı için

fibonacci = [x for x in range(0,50)]

fibonacci[0] = 1
fibonacci[1] = 1

for i in range(0,48):
    fibonacci[i+2] = fibonacci[i] + fibonacci[i+1]

print(fibonacci)