import time
start = time.time()
prime = []
for i in range (2,100000):
    for a in range (2,i//2):
        if (i%a)==0:
            break
    else:
        prime.append(i)
print(prime)
end = time.time()
print(end - start)
