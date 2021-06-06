import time 
start = time.time()
num = 1
num2 = 2
next = 3
total = 2
while next < 4000000:
  next = num+num2
  if next % 2 == 0:
    total += next
  num = num2
  num2 = next
elapsed = (time.time() - start)
print ("found %s in %s seconds" % (total,elapsed))