import math
import time 
start = time.time()

num = 600851475143
prime = 'true'
first = []
for i in range(2,int(math.sqrt(num))):
  if num % i == 0:
    first.append(i)

for j in range(len(first)):
  for k in range(2,int(math.sqrt(first[j]))):
    if first[j] % k == 0:
      prime = 'false'
  if prime == 'true':
    highest = first[j]
elapsed = (time.time() - start)
print ("found %s in %s seconds" % (highest,elapsed))