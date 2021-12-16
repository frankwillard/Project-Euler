import time 
start = time.time()

total1 = 0
total2 = 0

for i in range(101):
    total1 += i * i
    total2 += i

total2 *= total2

elapsed = (time.time() - start)
print ("found %s in %s seconds" % (total2 - total1,elapsed))
