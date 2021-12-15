import math
import time 
start = time.time()

def factsum(n):
  factsum = 1
  for i in range(2,int(n/2)+1):
    if n % i == 0:
      factsum +=i
  return factsum


amisum = 0
amicable = []
for i in range (1,10000):
  current = factsum(i)
  if i == factsum(current) and i != current:
    amicable.append(i)
    amisum+=i
elapsed = (time.time() - start)
# About 12 seconds
print ("found %s in %s seconds" % (amisum,elapsed))



