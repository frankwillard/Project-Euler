import time 
start = time.time()
import math
# Cheater method
size = 20
paths = math.factorial(size*2)/(math.factorial(size)* math.factorial(size))
elapsed = (time.time() - start)
print ("found %s in %s seconds" % (paths,elapsed))
