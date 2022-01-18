import random
import time
s = time.time()
t = int(input("How many experiments? 10 flips per experiment ... "))
def flipten():
    flips = []
    for x in range(10):
        flips.append(random.randint(0,1))
    return sum(flips)

y = []
for z in range(t):
    y.append(flipten())
for z in range(0,11):
    print(z,"\t",y.count(z)/t*100,"%")
print("AVERAGE NUMBER OF HEADS:", sum(y)/len(y))
e = time.time()
print("TIME TAKEN:", round(e-s,2), "seconds")
