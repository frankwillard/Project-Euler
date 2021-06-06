import time 
start = time.time()
primes = [2]
primeCount = 1
num = 3

while primeCount < 10001:
    prime = 'true'
    for i in primes:
        if num % i == 0:
            prime = 'false'
            break
    if prime == 'true':
        primeCount += 1
        primes.append(num)
    num += 2
elapsed = (time.time() - start)
print ("found %s in %s seconds" % (num-2,elapsed))