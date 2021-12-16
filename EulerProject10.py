import time 
start = time.time()
import math
total = 2
num = 3
primes = [2]
while num < 2000000:
    prime = 'true'
    upper = math.sqrt(num)
    for i in primes:
        if i > upper:
            break
        if num % i == 0:
            prime = 'false'
            break
        
    if prime == 'true':
        total += num
        primes.append(num)
        
    num +=2

elapsed = (time.time() - start)
print ("found %s in %s seconds" % (total,elapsed))
