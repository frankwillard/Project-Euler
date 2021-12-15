import time 
start = time.time()
num = 100
factorial = 1
while (num > 1):
  factorial *= num
  num-=1
sum = 0
for i in str(factorial):
  sum += int(i)
elapsed = (time.time() - start)
print ("found %s in %s seconds" % (sum,elapsed))
