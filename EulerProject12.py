import time 
start = time.time()
import math
j = 1
div = 1
num = 0
while div < 500:
  num += j
  # Only getting even numbers
  if num % 2 == 0:
    div = 0
    for i in range(1, int(math.sqrt(num))+1):
      if num % i == 0:
        div += 2
  j += 1
elapsed = (time.time() - start)
print ("found %s in %s seconds" % (num,elapsed))
  
