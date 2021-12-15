import time 
start = time.time()
total = 0
for i in range(1,1000):
  total += i**i
elapsed = (time.time() - start)
print ("found %s in %s seconds" % (total,elapsed))
