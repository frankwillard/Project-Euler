import time 
start = time.time()
sum = 0
for i in range(1000):
  if i % 5 == 0 or i % 3 == 0:
    sum += i
elapsed = (time.time() - start)
print ("found %s in %s seconds" % (sum,elapsed))