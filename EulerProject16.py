import time 
start = time.time()
num = 2**1000
total = 0
for i in str(num):
  total += int(i)
elapsed = (time.time() - start)
print ("found %s in %s seconds" % (total,elapsed))
