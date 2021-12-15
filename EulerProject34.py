import time 
start = time.time()
sum = 0
for i in range(10,100000):
  string = str(i)
  factsum = 0
  for j in range(len(string)):
    factorial = 1
    current = int(string[j])
    while current > 1:
      factorial *= current
      current-=1
    factsum+=factorial
  if factsum == i:
    sum+=i
elapsed = (time.time() - start)
print ("found %s in %s seconds" % (sum,elapsed))
