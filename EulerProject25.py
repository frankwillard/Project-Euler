import time 
start = time.time()

num = 1
num2 = 2
next = 3
i = 3
while len(str(next)) < 1000:
  next = num+num2
  num = num2
  num2 = next
  i = i + 1
print(i)

elapsed = (time.time() - start)
print ("found %s in %s seconds" % (i,elapsed))
