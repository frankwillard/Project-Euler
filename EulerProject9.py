import time 
start = time.time()
for c in range(335, 500, 1):
    for b in range(int(c/2), c-1):
        a = 1000 - b - c
        if (a * a) + (b * b) == (c*c):
            elapsed = (time.time() - start)
            print ("found %s in %s seconds" % (a*b*c,elapsed))
            