import time 
start = time.time()
largenum = 28433* 2 ** 7830457+1
tendigmod = 10 ** 10
elapsed = (time.time() - start)
print ("found %s in %s seconds" % (largenum % tendigmod,elapsed))
