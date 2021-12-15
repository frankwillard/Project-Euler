import time 
start = time.time()

fifths = []
total = 0
for i in range(10, 6* 9**5):
  sum = 0
  for j in str(i):
    sum += int(j)**5
  if(sum == i):
    total+=i
elapsed = (time.time() - start)
print ("found %s in %s seconds" % (total,elapsed))
