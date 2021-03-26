import math
import random

i = 0
d = 0
y = 0

while i<10000:

    i += 1
  
    a = random.random()
    b = random.random()

    kenar1 = a
    kenar2 = b-a
    kenar3 = 1-b
    
    if kenar1 > kenar2 + kenar3 and kenar1 < abs(kenar3-kenar2):
        d += 1
    elif kenar2 > kenar1 + kenar3 and kenar2 < abs(kenar3-kenar1):
        d += 1
    elif kenar3 > kenar1 +kenar2 and kenar3 < abs(kenar2-kenar1):
        d += 1    
    else:
        y += 1

print("d",d)
print("y",y)

oran = d/i

print("oran",oran)
