import time 
start = time.time()
num = 2520
found = 'false'
while found  == 'false':
  for i in range(3,20):
    if(num % i != 0):
      break
    if(i == 19):
      found = 'true'
  num+=20
elapsed = (time.time() - start)
print ("found %s in %s seconds" % (num-20,elapsed))
